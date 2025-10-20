# Django 环境配置指南

## 项目结构
```
github1/
├── django_env/          # Python虚拟环境
├── myproject/           # Django项目
│   ├── manage.py       # Django管理脚本
│   └── myproject/      # 项目配置目录
├── requirements.txt    # 项目依赖
└── README.md          # 说明文档
```

## 环境配置步骤

### 1. 激活虚拟环境
```bash
# Windows PowerShell
django_env\Scripts\Activate.ps1
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行Django项目
```bash
cd myproject
python manage.py runserver
```

### 4. 访问应用
打开浏览器访问: http://127.0.0.1:8000/

## 已安装的包
- Django 5.2.7
- asgiref 3.10.0
- sqlparse 0.5.3
- tzdata 2025.2

## 常用Django命令
```bash
# 创建新应用
python manage.py startapp app_name

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 收集静态文件
python manage.py collectstatic
```

## 注意事项
- 确保在虚拟环境中运行所有Django命令
- 开发服务器仅用于开发环境，生产环境需要使用WSGI或ASGI服务器
- 数据库默认使用SQLite，位于项目根目录的db.sqlite3文件