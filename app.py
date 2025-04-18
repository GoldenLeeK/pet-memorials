from flask import Flask, render_template, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

def load_pet_info(pet_dir):
    meta_path = os.path.join('pets', pet_dir, 'meta.json')
    if not os.path.exists(meta_path):
        return None
        
    with open(meta_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # 添加目录名作为ID
    data['id'] = pet_dir
    
    # 计算年龄
    birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
    pass_date = datetime.strptime(data['pass_date'], '%Y-%m-%d')
    data['age'] = (pass_date - birth_date).days // 365
    
    # 加载故事内容
    stories = []
    for story_file in data.get('stories', []):
        story_path = os.path.join('pets', pet_dir, 'stories', story_file)
        if os.path.exists(story_path):
            with open(story_path, 'r', encoding='utf-8') as f:
                stories.append({
                    'title': story_file.replace('.md', ''),
                    'content': f.read()
                })
    data['stories_content'] = stories
    
    return data

@app.route('/')
def index():
    pets = []
    for pet_dir in os.listdir('pets'):
        if os.path.isdir(os.path.join('pets', pet_dir)):
            pet_info = load_pet_info(pet_dir)
            if pet_info:
                pets.append(pet_info)
    
    # 按去世日期排序
    pets.sort(key=lambda x: x['pass_date'], reverse=True)
    return render_template('index.html', pets=pets)

@app.route('/pet/<pet_id>')
def pet_detail(pet_id):
    pet_info = load_pet_info(pet_id)
    if not pet_info:
        return "宠物信息不存在", 404
    return render_template('pet_detail.html', pet=pet_info)

if __name__ == '__main__':
    app.run(debug=True) 