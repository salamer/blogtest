# blogtest
a blog system bases on django
这是一个我的用django做的类似贴吧的博客系统，因为它支持django auth的注册，并且文章有自己的category搜索和作者的editor搜索，分类清晰，算是我的django的练手项目

并且该项目使用了bootstrap的admin系统，添加了markdown富文本编辑器，使用的是mysql数据库，再使用前请建好mysql数据库，并在setting.py里做好相关配置。

使用：

pip install django
pip install django-bootstrap
pip install django-markdown-duex
cd blogtest
python manage.py runserver
