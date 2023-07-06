# bell
A simple blog based on django



### 特性

基本博客功能（文章、页面、归档、分类、标签、搜索）

搜索（使用基于 go 的 zincsearch 搜索引擎，中文搜索效果不错）

目录简洁明了，模板文件爽心悦目

采用 ORM 操作数据库，目前默认使用 sqlite3 

采用 django 自带 admin，不想写，用现成的

...

### 依赖

```
django # 不必多说
requests # 不必多说，用于 zincsearch api 接口请求
marko # 纯 python 实现的 markdown 解析模块
pillow # 不必多说，django后台需用到
pipenv # python虚拟环境
```

### 运行

安装pipenv

```
pip install pipenv
```

拉取项目

```
git clone git@github.com:daifiyum/bell.git
```

安装 zincsearch 搜索引擎（docker安装）

```
docker-compose.yml

version: '3.3'
services:
    zinclabs:
        container_name: Zincsearch
        network_mode: bridge
          # volumes:
          # - './volume:/data'
        environment:
            - ZINC_DATA_PATH=/data
            - ZINC_FIRST_ADMIN_USER=admin # 改动徐改 settings.py
            - ZINC_FIRST_ADMIN_PASSWORD=1234567890d # 改动徐改 settings.py
        ports:
            - '4080:4080'
        image: 'public.ecr.aws/zinclabs/zincsearch:latest'
```

```
如何想要自定义 zincsearch 的账号密码等参数，不要忘记更改项目目录下的 settings.py 配置文件
settings.py 里的 zincsearch 配置项：
# zincsearch 搜索引擎配置
ZINCSEARCH = {
    'user': 'admin', # 账户
    'password': '1234567890d', # 密码
    'index': 'blog', # 索引数据库目录，默认即可
    'zinc_host': 'http://localhost:4080', # zincsearch 请求链接
}
```

安装依赖

```
cd <项目>

pipenv install
```

数据库和索引初始化

```
python manage.py makemigrations
python manage.py migrate
```

创建后台管理员账户

```
python manage.py createsuperuser
```

运行博客

```
pipenv run python manage.py runserver
```

