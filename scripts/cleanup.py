# scripts/cleanup.py
import os
import json
import shutil
from datetime import datetime, timedelta

def create_archive_dir():
    if not os.path.exists('archived'):
        os.makedirs('archived')

def move_to_archive(pet_dir):
    src_path = os.path.join('pets', pet_dir)
    dst_path = os.path.join('archived', pet_dir)
    
    try:
        shutil.move(src_path, dst_path)
        print(f"已将 {pet_dir} 移动到归档目录")
    except Exception as e:
        print(f"移动 {pet_dir} 时出错: {str(e)}")

def cleanup_pets():
    create_archive_dir()
    
    if not os.path.exists('pets'):
        print("pets 目录不存在")
        return
        
    current_time = datetime.now()
    moved_count = 0
    
    for pet_dir in os.listdir('pets'):
        meta_path = os.path.join('pets', pet_dir, 'meta.json')
        
        if not os.path.exists(meta_path):
            print(f"警告: {pet_dir} 目录中缺少 meta.json 文件")
            continue
            
        try:
            last_modified = datetime.fromtimestamp(os.path.getmtime(meta_path))
            if (current_time - last_modified) > timedelta(days=365*5):
                move_to_archive(pet_dir)
                moved_count += 1
        except Exception as e:
            print(f"处理 {pet_dir} 时出错: {str(e)}")
            
    print(f"\n清理完成，共移动 {moved_count} 个宠物信息到归档目录")

if __name__ == "__main__":
    cleanup_pets()