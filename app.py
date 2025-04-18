from flask import Flask, render_template, jsonify, send_from_directory
import os
import json
from datetime import datetime

app = Flask(__name__)

def load_pet_info(pet_dir):
    """加载宠物信息"""
    try:
        meta_path = os.path.join('pets', pet_dir, 'meta.json')
        if not os.path.exists(meta_path):
            return None
            
        with open(meta_path, 'r', encoding='utf-8') as f:
            pet_info = json.load(f)
            pet_info['id'] = pet_dir  # 添加ID用于URL
            return pet_info
    except Exception as e:
        print(f"Error loading pet info for {pet_dir}: {str(e)}")
        return None

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

@app.route('/readme')
def readme():
    return render_template('readme.html')

@app.route('/pet/<pet_id>')
def pet_detail(pet_id):
    pet_info = load_pet_info(pet_id)
    if not pet_info:
        return "宠物信息不存在", 404
    return render_template('pet_detail.html', pet=pet_info)

if __name__ == '__main__':
    app.run(debug=True) 
