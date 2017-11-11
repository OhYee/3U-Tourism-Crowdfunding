import application.database as db


def get_test():
    res = [
        {
            'title': '往期精品',
            'url': '#',
            'projects': [
                {
                    'img': '/static/img/test.jpg',
                    'title': '黄山黄山黄山黄山黄山黄山黄山黄山黄山',
                    'abstract': '简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介',
                    'money': '10005.05',
                    'people': '100',
                    'pre': '70',
                    'tags': [
                        {
                            'href': '/',
                            'text': '标签1'
                        }
                    ]
                }
            ]
        },
        {
            'title': '正在进行',
            'url': '#',
            'projects': [
                {
                    'img': '/static/img/test.jpg',
                    'title': '标题标题标题',
                    'abstract': '26年的餐饮“老炮”，从零开始要做一款上海风味的小火锅他曾参与打造：盘湾方舟、清水兰轩、虾满堂、李主厨系列等众多餐饮品牌。这一次他要用..',
                    'money': '10005.05',
                    'people': '100',
                    'pre': '70',
                    'tags': [
                        {
                            'href': '/',
                            'text': '标签1'
                        }
                    ]
                },
                {
                    'img': '/static/img/test.jpg',
                    'title': '标题标题标题',
                    'abstract': '26年的餐饮“老炮”，从零开始要做一款上海风味的小火锅他曾参与打造：盘湾方舟、清水兰轩、虾满堂、李主厨系列等众多餐饮品牌。这一次他要用..',
                    'money': '10005.05',
                    'people': '100',
                    'pre': '70',
                    'tags': [
                        {
                            'href': '/',
                            'text': '标签1'
                        }
                    ]
                },
                {
                    'img': '/static/img/test.jpg',
                    'title': '',
                    'abstract': '123123',
                    'money': '1.05',
                    'people': '100',
                    'pre': '0',
                    'tags': [
                        {
                            'href': '/',
                            'text': '标签1'
                        }
                    ]
                }
            ]
        }
    ]

    return res


def get_projects():
    res = db.query_db(
        'select * from projects where deleted = 0 order by pid DESC;')
    return res


def get_project(pid):
    res = db.query_db('select * from projects where pid=?;', [pid], True)
    return res


def get_last_pid():
    res = db.query_db(
        "select pid from projects order by id DESC limit 1;", [], True)
    Id = 0
    if len(res) != 0:
        Id = res['pid']
    return Id


def add_project(uid, content, title, time):
    pid = get_last_pid() + 1
    db.query_db("insert into projects(pid,uid,title,content,time,deleted) values(%s,%s,'%s','%s','%s',0);", [
                pid, uid, title, content, time])


def delete_project(pid, deleted):
    db.query_db("update projects set deleted=%s where pid=%s;", [deleted, pid])


def update_project(pid,  title, content, time):
    db.query_db("update projects set title='%s',content='%s',time='%s',deleted=%s where pid=%s;", [
                title, content, time, pid])
