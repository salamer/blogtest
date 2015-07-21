# blogtest

>这是一个我的用django做的类似贴吧的博客系统，因为它支持django >auth的注册，并且文章有自己的category搜索和作者的editor搜索，分类清晰，算是我的django的练手项目

>前端用的是yahoo的pure框架，但它最近好像有点抽，见谅```

>并且该项目使用了bootstrap的admin系统，添加了markdown富文本编辑器，使用的是mysql数据库，再使用前请建好mysql数据库，并在>setting.py里做好相关配置。

>他的数据库在setting.py文件夹中，用的是mysql，请自行输入一个数据库

>使用前请先装好pip

#使用：
>创建mysql数据库：

    create database [databasename]  
    
>注意要把这个写在setting.py里面


>安装扩展库和django

    pip install django

    pip install django-bootstrap

    pip install django-markdown-duex

    cd blogtest
>创建数据库
    
    python manage.py migrate

    python manage.py makemigrations

    python manage.py runserver

