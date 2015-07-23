# coding:utf-8

from hello import db
from hello import Role, User


db.create_all()
db.drop_all()
db.create_all()
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_dada = User(username='dada', role=mod_role)

print(admin_role.id)
print(mod_role.id)
print(user_role.id)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_dada)
db.session.add(user_susan)

db.session.commit()
# 数据库会话 db.session 与 Flask session 对象没有关系。数据库会话也称为事务。
print(admin_role.id)
print(mod_role.id)
print(user_role.id)

# 修改行
admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()
print admin_role

# delete
db.session.delete(mod_role)
db.session.commit()
print db.session
print db

# query
roles = Role.query.all()
print roles
users = User.query.all()
print users

# filter
print User.query.filter_by(role=user_role).all()
temp_role = Role.query.filter_by(name='User').first()
print temp_role

# sql text
sqltext = str(User.query.filter_by(role=user_role))
print sqltext

print user_role.users
print users[0].role