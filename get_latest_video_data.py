#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
从 TikTokDownloader 生成的 CSV 文件中获取视频的最新数据
支持根据视频ID查找最新的点赞数、评论数等互动数据
"""

import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
import argparse


class VideoDataReader:
    """从CSV文件中读取和查询视频数据"""
    
    def __init__(self, csv_file_path: str):
        """
        初始化数据读取器
        
        Args:
            csv_file_path: CSV文件路径
        """
        self.csv_path = Path(csv_file_path)
        self.df = None
        self._load_data()
    
    def _load_data(self):
        """加载CSV数据"""
        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV文件不存在: {self.csv_path}")
        
        try:
            # 读取CSV文件，处理编码问题
            self.df = pd.read_csv(self.csv_path, encoding='utf-8-sig')
            print(f"成功加载CSV文件: {self.csv_path}")
            print(f"总记录数: {len(self.df)}")
            
            # 转换采集时间为datetime类型
            if 'collection_time' in self.df.columns:
                self.df['collection_time'] = pd.to_datetime(self.df['collection_time'])
            
        except Exception as e:
            raise Exception(f"读取CSV文件失败: {e}")
    
    def get_latest_video_data(self, video_id: str) -> Optional[Dict[str, Any]]:
        """
        根据视频ID获取最新的视频数据
        
        Args:
            video_id: 视频ID
            
        Returns:
            包含最新数据的字典，如果未找到则返回None
        """
        if self.df is None:
            return None
        
        # 筛选指定ID的所有记录
        video_records = self.df[self.df['作品ID'] == video_id]
        
        if video_records.empty:
            return None
        
        # 按采集时间排序，获取最新记录
        latest_record = video_records.sort_values('采集时间', ascending=False).iloc[0]
        
        return latest_record.to_dict()
    
    def get_latest_digg_count(self, video_id: str) -> Optional[int]:
        """
        获取视频的最新点赞数量
        
        Args:
            video_id: 视频ID
            
        Returns:
            最新点赞数量，如果未找到则返回None
        """
        latest_data = self.get_latest_video_data(video_id)
        if latest_data and '点赞数量' in latest_data:
            return int(latest_data['点赞数量']) if latest_data['点赞数量'] != '' else 0
        return None
    
    def get_latest_comment_count(self, video_id: str) -> Optional[int]:
        """
        获取视频的最新评论数量
        
        Args:
            video_id: 视频ID
            
        Returns:
            最新评论数量，如果未找到则返回None
        """
        latest_data = self.get_latest_video_data(video_id)
        if latest_data and '评论数量' in latest_data:
            return int(latest_data['评论数量']) if latest_data['评论数量'] != '' else 0
        return None
    
    def get_video_history(self, video_id: str) -> pd.DataFrame:
        """
        获取视频的历史数据变化
        
        Args:
            video_id: 视频ID
            
        Returns:
            包含该视频所有历史记录的DataFrame
        """
        if self.df is None:
            return pd.DataFrame()
        
        video_records = self.df[self.df['作品ID'] == video_id]
        return video_records.sort_values('采集时间', ascending=True)
    
    def get_videos_with_min_digg_count(self, min_digg_count: int) -> pd.DataFrame:
        """
        获取点赞数大于指定数量的视频（基于最新数据）
        
        Args:
            min_digg_count: 最小点赞数量
            
        Returns:
            符合条件的视频DataFrame
        """
        if self.df is None:
            return pd.DataFrame()
        
        # 按视频ID分组，获取每个视频的最新记录
        latest_records = self.df.sort_values('采集时间').groupby('作品ID').tail(1)
        
        # 筛选点赞数大于指定值的视频
        filtered_videos = latest_records[
            pd.to_numeric(latest_records['点赞数量'], errors='coerce') >= min_digg_count
        ]
        
        return filtered_videos.sort_values('点赞数量', ascending=False)
    
    def print_video_summary(self, video_id: str):
        """
        打印视频的详细信息摘要
        
        Args:
            video_id: 视频ID
        """
        latest_data = self.get_latest_video_data(video_id)
        if not latest_data:
            print(f"未找到视频ID: {video_id}")
            return
        
        print(f"\n=== 视频 {video_id} 最新数据 ===")
        print(f"作品描述: {latest_data.get('作品描述', 'N/A')}")
        print(f"账号昵称: {latest_data.get('账号昵称', 'N/A')}")
        print(f"发布时间: {latest_data.get('发布时间', 'N/A')}")
        print(f"采集时间: {latest_data.get('采集时间', 'N/A')}")
        print(f"点赞数量: {latest_data.get('点赞数量', 'N/A')}")
        print(f"评论数量: {latest_data.get('评论数量', 'N/A')}")
        print(f"收藏数量: {latest_data.get('收藏数量', 'N/A')}")
        print(f"分享数量: {latest_data.get('分享数量', 'N/A')}")
        print(f"播放数量: {latest_data.get('播放数量', 'N/A')}")
        
        # 显示历史记录数量
        history = self.get_video_history(video_id)
        print(f"历史记录数: {len(history)} 条")


def main():
    """命令行使用示例"""
    parser = argparse.ArgumentParser(description='从CSV文件中获取视频最新数据')
    parser.add_argument('csv_file', help='CSV文件路径')
    parser.add_argument('--video-id', '-v', help='要查询的视频ID')
    parser.add_argument('--min-digg', '-d', type=int, help='筛选点赞数大于指定值的视频')
    parser.add_argument('--list-top', '-t', type=int, default=10, help='显示前N个热门视频')
    
    args = parser.parse_args()
    
    try:
        reader = VideoDataReader(args.csv_file)
        
        if args.video_id:
            # 查询特定视频
            reader.print_video_summary(args.video_id)
            
        elif args.min_digg:
            # 筛选高点赞视频
            filtered_videos = reader.get_videos_with_min_digg_count(args.min_digg)
            print(f"\n点赞数 >= {args.min_digg} 的视频:")
            print(filtered_videos[['作品ID', '作品描述', '账号昵称', '点赞数量', '采集时间']].head(args.list_top))
            
        else:
            # 显示基本统计信息
            print(f"\nCSV文件统计信息:")
            print(f"总记录数: {len(reader.df)}")
            print(f"唯一视频数: {reader.df['作品ID'].nunique()}")
            print(f"数据时间范围: {reader.df['采集时间'].min()} 到 {reader.df['采集时间'].max()}")
            
    except Exception as e:
        print(f"错误: {e}")


if __name__ == "__main__":
    # 使用示例
    print("=== TikTokDownloader CSV 数据查询工具 ===\n")
    
    # 示例1: 直接使用类
    # reader = VideoDataReader("path/to/DetailData.csv")
    # digg_count = reader.get_latest_digg_count("7123456789")
    # print(f"最新点赞数: {digg_count}")
    
    # 示例2: 命令行使用
    main()
