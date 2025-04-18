# 电子宠物墓园 | Pet Memorials

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

[English](#english) | [中文](#chinese)

<a name="chinese"></a>
## 🇨🇳 中文

### 项目简介

这是一个基于GitHub的电子宠物墓园项目，让您可以永久保存和纪念您心爱的宠物。通过简单的操作，您可以创建一个专属于您宠物的纪念页面，上传照片和故事，与世界分享您与宠物之间的美好回忆。

### 功能特点

- **永久保存**：基于GitHub的可靠存储，确保您的宠物信息永久保存
- **照片与故事**：支持上传多张照片和多篇故事，全面展示宠物生平
- **简单操作**：通过简单的JSON文件配置，轻松创建和更新宠物信息
- **美观界面**：精心设计的Web界面，优雅展示每一个宠物的纪念页
- **完全免费**：开源项目，永久免费使用
- **数据安全**：自动清理长期未更新的信息，保持数据整洁

<a name="english"></a>
## 🇬🇧 English

### Project Description

This is a GitHub-based pet memorial project that allows you to permanently preserve and commemorate your beloved pets. With simple operations, you can create a dedicated memorial page for your pet, upload photos and stories, and share your beautiful memories with the world.

### Features

- **Permanent Storage**: Reliable GitHub-based storage ensures your pet information is preserved forever
- **Photos & Stories**: Support for multiple photos and stories to fully showcase your pet's life
- **Simple Operation**: Easy creation and updating of pet information through simple JSON file configuration
- **Beautiful Interface**: Carefully designed web interface elegantly displays each pet's memorial page
- **Completely Free**: Open source project, free to use forever
- **Data Security**: Automatic cleaning of long-term inactive information to keep data tidy

## 使用指南 | Usage Guide

<a name="chinese-usage"></a>
### 🇨🇳 中文使用指南

#### 创建新的宠物纪念页

1. **Fork 本项目**：点击GitHub页面右上角的 "Fork" 按钮
2. **创建宠物目录**：在 `pets` 目录下创建一个新的目录，命名格式为 `宠物名字-主人名字`
3. **创建子目录**：在您的宠物目录下创建 `photos` 和 `stories` 两个子目录
4. **创建元数据文件**：在宠物目录中创建 `meta.json` 文件，按下面的格式填写宠物信息
5. **上传照片**：将宠物的照片上传到 `photos` 目录
6. **添加故事**：在 `stories` 目录中创建 Markdown 格式的故事文件
7. **提交 Pull Request**：将您的更改提交到主项目

#### 更新现有宠物信息

1. **找到宠物目录**：在 `pets` 目录下找到您的宠物目录
2. **修改文件**：更新 `meta.json` 文件或添加新的照片、故事
3. **提交 Pull Request**：将您的更改提交到主项目

#### 本地运行Web应用

1. **克隆项目**
```bash
git clone https://github.com/your-username/pet-memorials.git
cd pet-memorials
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行应用**
```bash
python app.py
```

4. **访问网站**：打开浏览器访问 http://localhost:5000

<a name="english-usage"></a>
### 🇬🇧 English Usage Guide

#### Creating a New Pet Memorial

1. **Fork this project**: Click the "Fork" button in the top right corner of the GitHub page
2. **Create a pet directory**: Create a new directory under the `pets` folder, naming it in the format `pet-name-owner-name`
3. **Create subdirectories**: Create two subdirectories named `photos` and `stories` in your pet directory
4. **Create metadata file**: Create a `meta.json` file in the pet directory and fill in your pet's information according to the format below
5. **Upload photos**: Add your pet's photos to the `photos` directory
6. **Add stories**: Create Markdown format story files in the `stories` directory
7. **Submit a Pull Request**: Submit your changes to the main project

#### Updating Existing Pet Information

1. **Locate the pet directory**: Find your pet's directory under the `pets` folder
2. **Modify files**: Update the `meta.json` file or add new photos and stories
3. **Submit a Pull Request**: Submit your changes to the main project

#### Running the Web Application Locally

1. **Clone the project**
```bash
git clone https://github.com/your-username/pet-memorials.git
cd pet-memorials
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the website**: Open your browser and visit http://localhost:5000

## 数据格式 | Data Format

<a name="chinese-format"></a>
### 🇨🇳 宠物信息格式

每个宠物的信息存储在 `meta.json` 文件中，格式如下：

```json
{
  "name": "宠物名字",
  "owner": "主人名字",
  "birth_date": "YYYY-MM-DD",
  "pass_date": "YYYY-MM-DD",
  "species": "物种",
  "breed": "品种",
  "description": "描述",
  "photos": ["photo1.jpg", "photo2.jpg"],
  "stories": ["story1.md", "story2.md"]
}
```

<a name="english-format"></a>
### 🇬🇧 Pet Information Format

Each pet's information is stored in a `meta.json` file with the following format:

```json
{
  "name": "Pet Name",
  "owner": "Owner Name",
  "birth_date": "YYYY-MM-DD",
  "pass_date": "YYYY-MM-DD",
  "species": "Species",
  "breed": "Breed",
  "description": "Description",
  "photos": ["photo1.jpg", "photo2.jpg"],
  "stories": ["story1.md", "story2.md"]
}
```

## 项目结构 | Project Structure

```
pet-memorials/
├── app.py                 # Flask application main file / Flask应用主文件
├── requirements.txt       # Python dependencies / Python依赖
├── templates/            # HTML templates / HTML模板
│   ├── base.html
│   ├── index.html
│   └── pet_detail.html
├── static/              # Static files / 静态文件
│   └── css/
│       └── style.css
├── pets/               # Pet information directory / 宠物信息目录
│   └── example-pet-owner/
│       ├── meta.json
│       ├── photos/
│       └── stories/
├── scripts/           # Utility scripts / 工具脚本
│   ├── validate.py
│   └── cleanup.py
└── .github/          # GitHub configuration / GitHub配置
    └── workflows/
        └── pet-memorials.yml
```

## 贡献与支持 | Contributing & Support

### 🇨🇳 贡献指南

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目。如果您有任何问题或建议，请创建 Issue 或联系项目维护者。

### 🇬🇧 Contributing Guide

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to participate in the project. If you have any questions or suggestions, please create an issue or contact the project maintainers.

## 许可证 | License

### 🇨🇳 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

### 🇬🇧 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.