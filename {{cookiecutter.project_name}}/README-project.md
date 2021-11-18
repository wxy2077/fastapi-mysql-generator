# FastAPI and MySQL - 项目生成器

## 如何使用

进入你想要生成项目的文件夹下，并且运行以下命令。

```
pip install cookiecutter
cookiecutter https://github.com/youth1996/fastapi-mysql-generator

cd your_project/
# 安装依赖库
pip install -r requirements.txt

# 建议使用 --upgrade 安装最新版 (windows系统下uvloop当前版本可能有问题  https://github.com/MagicStack/uvloop/issues/14)
pip install --upgrade -r requirements-dev.txt
```

## 配置你的数据库环境

在这个文件下 `project/app/core/config/development_config.py` 或者 `production_config.py`。

配置MySQL和Redis信息

## 迁移数据库

```
# 进入项目下
cd your_project/

# 生成关系映射 (第二次生成映射记得修改提交注释 init commit)
alembic revision --autogenerate -m "init commit"

# 生成表 (注意初次生成表会删除其他的表 建议在一个空数据库测试)
alembic upgrade head
```

<details>
<summary>迁移由于项目路径可能失败</summary>

```python

# 在 alembic/env.py文件里面
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"当前路径:{BASE_DIR}")


sys.path.insert(0, BASE_DIR) 
# 如果还不行，那就简单直接点 直接写固定
# sys.path.insert(0, "/你的路径/you_project/") 

```
</details>

## 创建用户
> 会默认创建两个角色一个为超级管理员角色，一个为普通角色，
超级管理员拥有目前接口的所有调用权限，普通用户只能登录和获取自身用户信息.
```
cd your_project/
python init_db.py
```

## 运行启动

```
# 进入项目文件夹下
cd your_project/

# 命令行运行(开发模式)
uvicorn main:app --host=127.0.0.1 --port=8010 --reload

# 直接运行main文件(会打印两次路由)
python main.py
```

<details>
<summary>可能会出现的常见路径倒入问题</summary>

```
# 如下两种解决方式

# pycharm中设置 标记为sources root
https://www.jetbrains.com/help/pycharm/configuring-content-roots.html#specify-folder-categories

# 命令行中标记为 sources root
https://stackoverflow.com/questions/30461982/how-to-provide-make-directory-as-source-root-from-pycharm-to-terminal

```
</details>

在线文档地址(在配置文件里面设置路径或者关闭)
```
http://127.0.0.1:8010/api/docs
```

## 接口测试

需要安装

```shell
pip install pytest
```

在项目下 启动测试用例
```
cd your_project/
pytest

# 接口测试结果
collected 10 items                                                                                                                             

tests/api/v1/test_casbin.py ....                                                                                                         [ 40%]
tests/api/v1/test_cron.py ...                                                                                                            [ 70%]
tests/api/v1/test_user.py ...                                                                                                            [100%]

============================================================== 10 passed in 1.77s ==============================================================
```


## 部署

部署的时候，可以关闭在线文档，见学习文章一配置篇。

```shell
在main.py同文件下下启动 去掉 --reload 选项 增加 --workers
uvicorn main:app --host=127.0.0.1 --port=8010 --workers=4

# 同样可以也可以配合gunicorn多进程启动  main.py同文件下下启动 默认127.0.0.1:8010端口 gunicorn需要安装
# 参考http://www.uvicorn.org/#running-with-gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8010
```
<details>
<summary>点击查看托管到后台运行</summary>
  
```shell
# 1 如果为了简单省事 可以直接使用 nohup 命令 如下: run.log文件需要自行创建
nohup /env_path/uvicorn main:app --host=127.0.0.1 --port=8010 --workers=4 > run.log 2>&1 &

# 2 可以使用supervisor托管后台运行部署, 当然也可以使用其他的
# supervisor可以参考我总结的文章 https://www.cnblogs.com/CharmCode/p/14210280.html
```
</details>
