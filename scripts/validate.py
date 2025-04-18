import os
import json
import jsonschema
from datetime import datetime

# 定义JSON Schema
schema = {
    "type": "object",
    "required": ["name", "owner", "birth_date", "pass_date", "species"],
    "properties": {
        "name": {"type": "string"},
        "owner": {"type": "string"},
        "birth_date": {"type": "string", "format": "date"},
        "pass_date": {"type": "string", "format": "date"},
        "species": {"type": "string"},
        "breed": {"type": "string"},
        "description": {"type": "string"},
        "photos": {
            "type": "array",
            "items": {"type": "string"}
        },
        "stories": {
            "type": "array",
            "items": {"type": "string"}
        }
    }
}

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_pet_info(pet_dir):
    meta_path = os.path.join('pets', pet_dir, 'meta.json')
    
    if not os.path.exists(meta_path):
        print(f"错误: {pet_dir} 目录中缺少 meta.json 文件")
        return False
        
    try:
        with open(meta_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # 验证JSON Schema
        jsonschema.validate(instance=data, schema=schema)
        
        # 验证日期格式
        if not validate_date(data['birth_date']):
            print(f"错误: {pet_dir} 的出生日期格式不正确")
            return False
            
        if not validate_date(data['pass_date']):
            print(f"错误: {pet_dir} 的去世日期格式不正确")
            return False
            
        # 验证照片文件是否存在
        for photo in data.get('photos', []):
            photo_path = os.path.join('pets', pet_dir, 'photos', photo)
            if not os.path.exists(photo_path):
                print(f"错误: {pet_dir} 的照片文件 {photo} 不存在")
                return False
                
        # 验证故事文件是否存在
        for story in data.get('stories', []):
            story_path = os.path.join('pets', pet_dir, 'stories', story)
            if not os.path.exists(story_path):
                print(f"错误: {pet_dir} 的故事文件 {story} 不存在")
                return False
                
        return True
        
    except json.JSONDecodeError:
        print(f"错误: {pet_dir} 的 meta.json 文件格式不正确")
        return False
    except jsonschema.exceptions.ValidationError as e:
        print(f"错误: {pet_dir} 的数据验证失败: {str(e)}")
        return False

def main():
    if not os.path.exists('pets'):
        print("错误: pets 目录不存在")
        return
        
    has_errors = False
    for pet_dir in os.listdir('pets'):
        if not validate_pet_info(pet_dir):
            has_errors = True
            
    if has_errors:
        print("\n验证失败，请修复上述错误")
        exit(1)
    else:
        print("\n所有宠物信息验证通过")

if __name__ == "__main__":
    main() 