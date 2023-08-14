import joblib as joblib
import numpy as np
import pandas as pd
import sklearn
from flask import Flask, render_template, request, json, jsonify
from sqlalchemy import Column, Integer, DateTime, NVARCHAR, Boolean, Date, BOOLEAN, and_
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import warnings

warnings.filterwarnings("ignore")  # 不显示警告信息

# flask服务器
app = Flask(__name__)
# app.config['SECRET_KEY'] = '1456719640@qq.com'

# 连接数据库配置文件
engine = create_engine('mysql+pymysql://roblox:123456@localhost/roblox?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#  创建表格的类
class Users(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "users"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    ID = Column(Integer, primary_key=True)  # Column类创建一个字段
    nickname = Column(NVARCHAR(255),
                      nullable=False)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    username = Column(NVARCHAR(255), nullable=False)
    password = Column(NVARCHAR(255), nullable=False)
    sex = Column(NVARCHAR(255), nullable=False)
    age = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

    def __repr__(self):
        return '<users %r>' % self.ID


class Question(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "questionnaire_question"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    quesiton_id = Column(Integer, primary_key=True)  # Column类创建一个字段
    questionnaire_id = Column(Integer,
                              nullable=False)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index
    # 可以让系统自动根据这个字段为基础建立索引
    quesiton_text = Column(NVARCHAR(255), nullable=False)

    def __repr__(self):
        return '<questionnaire_question %r>' % self.ID


class Option(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "questionnaire_option"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    option_id = Column(Integer, primary_key=True)  # Column类创建一个字段
    quesiton_id = Column(Integer, nullable=False)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index
    # 可以让系统自动根据这个字段为基础建立索引
    option_text = Column(NVARCHAR(255), nullable=False)

    def __repr__(self):
        return '<questionnaire_option %r>' % self.ID


class Level(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "levels"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    ID = Column(Integer, primary_key=True)  # Column类创建一个字段
    username = Column(NVARCHAR(255),
                      nullable=False)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    scene1 = Column(BOOLEAN, nullable=False)
    scene2 = Column(BOOLEAN, nullable=False)
    scene3 = Column(BOOLEAN, nullable=False)
    scene4 = Column(BOOLEAN, nullable=False)
    scene5 = Column(BOOLEAN, nullable=False)

    def __repr__(self):
        return '<levels %r>' % self.ID


class Answer(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "answers_message"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    ID = Column(Integer, primary_key=True)  # Column类创建一个字段
    username = Column(NVARCHAR(255),
                      nullable=False)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    sex = Column(NVARCHAR(255), nullable=False)
    age = Column(Integer, nullable=False)
    exper = Column(NVARCHAR(255), nullable=False)
    cons = Column(Integer, nullable=False)
    per_type = Column(NVARCHAR(255), nullable=False)
    dim11 = Column(NVARCHAR(255), nullable=False)
    dim12 = Column(NVARCHAR(255), nullable=False)
    dim13 = Column(NVARCHAR(255), nullable=False)
    dim14 = Column(NVARCHAR(255), nullable=False)
    dim15 = Column(NVARCHAR(255), nullable=False)
    dim16 = Column(NVARCHAR(255), nullable=False)
    dim1 = Column(NVARCHAR(255), nullable=False)
    dim2 = Column(NVARCHAR(255), nullable=False)
    dim3 = Column(NVARCHAR(255), nullable=False)
    dim4 = Column(NVARCHAR(255), nullable=False)
    dim5 = Column(NVARCHAR(255), nullable=False)
    dim6 = Column(NVARCHAR(255), nullable=False)
    dim7 = Column(NVARCHAR(255), nullable=False)
    question_1 = Column(NVARCHAR(255), nullable=False)
    question_2 = Column(NVARCHAR(255), nullable=False)
    question_3 = Column(NVARCHAR(255), nullable=False)
    question_4 = Column(NVARCHAR(255), nullable=False)
    question_5 = Column(NVARCHAR(255), nullable=False)
    question_6 = Column(NVARCHAR(255), nullable=False)
    question_7 = Column(NVARCHAR(255), nullable=False)
    question_8 = Column(NVARCHAR(255), nullable=False)
    question_9 = Column(NVARCHAR(255), nullable=False)
    question_10 = Column(NVARCHAR(255), nullable=False)
    question_11 = Column(NVARCHAR(255), nullable=False)
    question_12 = Column(NVARCHAR(255), nullable=False)
    question_13 = Column(NVARCHAR(255), nullable=False)
    question_14 = Column(NVARCHAR(255), nullable=False)
    question_15 = Column(NVARCHAR(255), nullable=False)
    question_16 = Column(NVARCHAR(255), nullable=False)
    question_17 = Column(NVARCHAR(255), nullable=False)
    question_18 = Column(NVARCHAR(255), nullable=False)
    question_19 = Column(NVARCHAR(255), nullable=False)
    question_20 = Column(NVARCHAR(255), nullable=False)
    question_21 = Column(NVARCHAR(255), nullable=False)
    question_22 = Column(NVARCHAR(255), nullable=False)
    question_23 = Column(NVARCHAR(255), nullable=False)
    question_24 = Column(NVARCHAR(255), nullable=False)
    question_25 = Column(NVARCHAR(255), nullable=False)
    question_26 = Column(NVARCHAR(255), nullable=False)
    question_27 = Column(NVARCHAR(255), nullable=False)
    question_28 = Column(NVARCHAR(255), nullable=False)
    question_29 = Column(NVARCHAR(255), nullable=False)
    question_30 = Column(NVARCHAR(255), nullable=False)
    question_31 = Column(NVARCHAR(255), nullable=False)
    question_32 = Column(NVARCHAR(255), nullable=False)
    question_33 = Column(NVARCHAR(255), nullable=False)
    question_34 = Column(NVARCHAR(255), nullable=False)
    question_35 = Column(NVARCHAR(255), nullable=False)
    question_36 = Column(NVARCHAR(255), nullable=False)
    question_37 = Column(NVARCHAR(255), nullable=False)
    question_38 = Column(NVARCHAR(255), nullable=False)
    question_39 = Column(NVARCHAR(255), nullable=False)
    question_40 = Column(NVARCHAR(255), nullable=False)
    question_41 = Column(NVARCHAR(255), nullable=False)
    question_42 = Column(NVARCHAR(255), nullable=False)
    question_43 = Column(NVARCHAR(255), nullable=False)
    question_44 = Column(NVARCHAR(255), nullable=False)
    question_45 = Column(NVARCHAR(255), nullable=False)
    question_46 = Column(NVARCHAR(255), nullable=False)
    question_47 = Column(NVARCHAR(255), nullable=False)
    question_48 = Column(NVARCHAR(255), nullable=False)
    question_49 = Column(NVARCHAR(255), nullable=False)

    def __repr__(self):
        return '<answers_message %r>' % self.ID



class Systems(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "systems"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    ID = Column(Integer, primary_key=True)  # Column类创建一个字段
    game_id = Column(Integer,
                     nullable=False)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    score = Column(Integer, nullable=False)
    nickname = Column(NVARCHAR(255), nullable=False)
    username = Column(NVARCHAR(255), nullable=False)
    time = Column(Integer, nullable=False)

    def __repr__(self):
        return '<systems %r>' % self.ID


# flask架构服务器首页，直接访问网站
@app.route("/")
def home():
    return render_template('index.html')


# flask用于接受roblox登录数据，并反馈数据的接口
@app.route("/log", methods=['POST', 'GET', 'PUT'])
def getlogdata():
    if request.method == 'POST':
        logdata = request.get_json()  # 获取打包JSON数据
        print("登录访问成功")
    else:
        print("请以post请求进行访问")
        # username = int(request.args.get('username'))
        # password = int(request.args.get('password'))
    username = logdata['username']
    # 往MySQL数据进行条件查询
    logstatus = session.query(Users).filter(Users.username == username)
    # result = Users.query.filter(and_(Users.username == username, Users.password == password))
    time = 0
    for item in logstatus:
        time += 1
    # print("查询行数为："+str(time))
    status = 0
    if time > 0:
        status = 1  # 表示查询到结果，登录成功
        # print("存在")
    else:
        status = 0  # 表示没有查询到结果，登录失败
        # print("不存在")
    # print(username)
    # print(password)
    data = {
        "username": username,
        "status": status,
    }

    return jsonify(data)  # 返回布尔值


# flask用于接受roblox用户答卷信息，并反馈数据
@app.route("/que", methods=['POST', 'GET', 'PUT'])
def getans_data():
    ans_data = ""
    status = 1
    if request.method == 'POST':
        ans_data = request.get_json()  # 获取打包JSON数据
    else:
        print("请以post请求进行访问")
        # username = int(request.args.get('username'))
        # password = int(request.args.get('password'))
    md = joblib.load("roblox_model(2.0).pkl")  # 读取决策模型
    pre_list = []
    # 数据预处理
    try:
        pre_list = list(ans_data.values())
        if pre_list[38] == 1:
            pre_list[38] = 5
        elif pre_list[38] == 2:
            pre_list[38] = 4
        elif pre_list[38] == 4:
            pre_list[38] = 2
        elif pre_list[38] == 5:
            pre_list[38] = 1
        if pre_list[0] == '男':
            pre_list[0] = 1
        else:
            pre_list[0] = 0
        if pre_list[2] == '是':
            pre_list[2] = 1
        else:
            pre_list[2] = 0
        for th in range(39, 53):
            if pre_list[th] == "A":
                pre_list[th] = 1
            if pre_list[th] == "B":
                pre_list[th] = 2
            if pre_list[th] == "C":
                pre_list[th] = 3
            if pre_list[th] == "D":
                pre_list[th] = 4
    except:
        print("数据预处理报错")
    pr = np.array(pre_list[4:43]).reshape(1, 39)
    type = md.predict(pr)[0]  # 预测人格类型
    print(pre_list)

    def sum_dim(x, y):
        sum = 0
        for i in pre_list[x:y + 1]:
            sum += i
        return sum

    # 进行数据保存
    print(sum_dim(43, 44) * 0.625)
    print(pre_list[43:45])
    try:
        U = Answer(username=pre_list[3],
                   sex=pre_list[0],
                   age=pre_list[1],
                   exper=pre_list[2],
                   cons=sum_dim(32, 38) * 0.5 + 2.5 + sum_dim(43, 52) * 0.83,
                   per_type=type,
                   dim11=sum_dim(43, 44) * 0.83,  # 风险感知
                   dim12=sum_dim(45, 46) * 0.83,  # 信任
                   dim13=sum_dim(47, 48) * 0.83,  # 自我控制
                   dim14=sum_dim(49, 50) * 0.83,  # 社会易感
                   dim15=sum_dim(51, 52) * 0.83,  # 网络经验
                   dim16=sum_dim(32, 38) * 0.5 + 2.5,  # 信息加工
                   dim1=sum_dim(4, 13) / 2,  # 风险知觉水平
                   dim2=sum_dim(14, 21) / 2,  # 神经质水平
                   dim3=sum_dim(22, 25) / 2,  # 开放性水平
                   dim4=sum_dim(26, 28) / 2,  # 信任倾向水平
                   dim5=sum_dim(29, 31) / 2,  # 社会易感水平
                   dim6=sum_dim(32, 38) * 0.625 + 2.5,  # 信息加工能力水平
                   dim7=sum_dim(39, 42) / 2,  # 网络经验水平
                   question_1=pre_list[4],
                   question_2=pre_list[5],
                   question_3=pre_list[6],
                   question_4=pre_list[7],
                   question_5=pre_list[8],
                   question_6=pre_list[9],
                   question_7=pre_list[10],
                   question_8=pre_list[11],
                   question_9=pre_list[12],
                   question_10=pre_list[13],
                   question_11=pre_list[14],
                   question_12=pre_list[15],
                   question_13=pre_list[16],
                   question_14=pre_list[17],
                   question_15=pre_list[18],
                   question_16=pre_list[19],
                   question_17=pre_list[20],
                   question_18=pre_list[21],
                   question_19=pre_list[22],
                   question_20=pre_list[23],
                   question_21=pre_list[24],
                   question_22=pre_list[25],
                   question_23=pre_list[26],
                   question_24=pre_list[27],
                   question_25=pre_list[28],
                   question_26=pre_list[29],
                   question_27=pre_list[30],
                   question_28=pre_list[31],
                   question_29=pre_list[32],
                   question_30=pre_list[33],
                   question_31=pre_list[34],
                   question_32=pre_list[35],
                   question_33=pre_list[36],
                   question_34=pre_list[37],
                   question_35=pre_list[38],
                   question_36=pre_list[39],
                   question_37=pre_list[40],
                   question_38=pre_list[41],
                   question_39=pre_list[42],
                   question_40=pre_list[43],
                   question_41=pre_list[44],
                   question_42=pre_list[45],
                   question_43=pre_list[46],
                   question_44=pre_list[47],
                   question_45=pre_list[48],
                   question_46=pre_list[49],
                   question_47=pre_list[50],
                   question_48=pre_list[51],
                   question_49=pre_list[52], )
        session.add(U)
        session.commit()  # 不要忘了commit
        session.close()
        print("保存成功！")
    except:
        print("数据保存出错")
        status = 0

    data = {
        "status": status,
    }  # 返回数据，状态码1，保存成功；0保存失败
    return jsonify(data)  # 返回布尔值


# flask用于接受roblox的study数据，反馈个人类型，自动会去用户名，并将其保存
@app.route("/study", methods=['POST', 'GET', 'PUT'])
def getstudydata():
    # 获取人格类型，输入username，输出人格类型，利用了决策树模型
    def get_roblox_type(username):
        data_roblox_answer = session.query(Answer).filter(Answer.username == username)
        time = 0
        try:
            for item in data_roblox_answer:
                time += 1
            if time > 0:
                data_x = []
                for b in data_roblox_answer:
                    data_x.append(b.question_36)
                    data_x.append(b.question_37)
                    data_x.append(b.question_38)
                    data_x.append(b.question_39)
                    data_x.append(b.question_40)
                    data_x.append(b.question_41)
                    data_x.append(b.question_42)
                    data_x.append(b.question_43)
                    data_x.append(b.question_44)
                    data_x.append(b.question_45)
                    data_x.append(b.question_46)
                    data_x.append(b.question_47)
                    data_x.append(b.question_48)
                    data_x.append(b.question_49)
                data_x = np.array(data_x)
                data_x[data_x == "A"] = 1
                data_x[data_x == "B"] = 2
                data_x[data_x == "C"] = 3
                data_x[data_x == "D"] = 4
                data_x = pd.DataFrame(data_x)
                data_x = np.array(data_x).reshape(1, 14)

                md = joblib.load("roblox_model.pkl")
                print("项目读取成功")
                # pr=np.array([1,1,3,2,1,1,2,1,2,1,1,3,2,2])
                # pr=pr.reshape(1,14)
                type_r = md.predict(data_x)[0]
                re_type = type_r
                # if type_r == 1:
                #     re_type = "第一种类型"
                # elif type_r == 2:
                #     re_type = "第二种类型"
                # elif type_r == 3:
                #     re_type = "第三种类型"
                # elif type_r == 4:
                #     re_type = "第四种类型"
                # elif type_r == 5:
                #     re_type = "第五种类型"
                # elif type_r == 6:
                #     re_type = "第六种类型"
                # else:
                #     re_type = "类型返回错误"

                return re_type
            else:
                re_type = 0
                return re_type
        except  Exception as e:
            return "错误信息：", e

    if request.method == 'POST':
        studydata = request.get_json()
    else:
        print("请以post请求进行访问")
        # username = int(request.args.get('username'))
        # password = int(request.args.get('password'))
    username = studydata['username']
    data_re = session.query(Answer).filter(Answer.username == username)
    time = 0
    for item in data_re:
        time += 1
    status = 0
    if time > 0:
        status = 1  # 设置状态码
        for item in data_re:  # 此时说明存在用户端数据，可以进行数据读取与返回
            cons = item.cons
            dim11 = item.dim11
            dim12 = item.dim12
            dim13 = item.dim13
            dim14 = item.dim14
            dim15 = item.dim15
            dim16 = item.dim16
            dim1 = item.dim1
            dim2 = item.dim2
            dim3 = item.dim3
            dim4 = item.dim4
            dim5 = item.dim5
            dim6 = item.dim6
            dim7 = item.dim7
            types = int(float(item.per_type))

        # 数据库中是否存在用户，返回数据不一样
        data = {
            "status": status,
            "username": username,
            "cons": cons,
            "dim11": dim11,
            "dim12": dim12,
            "dim13": dim13,
            "dim14": dim14,
            "dim15": dim15,
            "dim16": dim16,
            "dim1": dim1,
            "dim2": dim2,
            "dim3": dim3,
            "dim4": dim4,
            "dim5": dim5,
            "dim6": dim6,
            "dim7": dim7,
            "types": str(types),
        }
    else:
        status = 0  # 设置状态码
        # 数据库中是否存在用户，返回数据不一样
        data = {
            "status": status,
            "username": username,
        }

    return jsonify(data)  # 返回json数据


# flask用于接受roblox的测验数据，计算得分
@app.route("/test_5", methods=['POST', 'GET', 'PUT'])
def gettestdata():
    if request.method == 'POST':
        testdata = request.get_json()
        print("测验数据获取成功")
    else:
        print("请以post请求进行访问")
        # username = int(request.args.get('username'))
        # password = int(request.args.get('password'))
    print(testdata)
    scene_number = testdata['scene_number']  # 子场景编号 1-- 2--医美整容
    # 进行一个预处理，放置提交出问题
    try:
        answer_1 = testdata['answer_1']
    except:
        answer_1 = "0"
    try:
        answer_2 = testdata['answer_2']
    except:
        answer_2 = "0"
    try:
        answer_3 = testdata['answer_3']
    except:
        answer_3 = "0"
    try:
        answer_4 = testdata['answer_4']
    except:
        answer_4 = "0"
    username = testdata['username']
    re_str = ""
    if scene_number == 2:  # 医美整容，子场景二,测试维度包括网络经验BB、信任 BC
        dim15 = 0  # 网络经验
        dim12 = 0  # 信任
        dim11 = 0  # 风险感知
        dim13 = 0  # 自我控制
        dim14 = 0  # 社会易感
        if answer_1 == "B":
            dim15 += 2.5
        if answer_2 == "B":
            dim15 += 2.5
        if answer_3 == "B":
            dim12 += 2.5
        if answer_4 == "C":
            dim14 += 2.5
        re_str = "恭喜你，信任、社会易感和网络经验各提升" + str(dim12) + "、" + str(dim14) + "、" + str(dim15) + "分。请在主场景学习进度中查看详情"
        data_re = session.query(Answer).filter(Answer.username == username)
        time = 0
        for item in data_re:
            time += 1
        try:
            if time > 0:  # 表明数据库中有数据，用户登录微信小程序了
                for item in data_re:
                    old_dim11 = float(item.dim11)
                    old_dim13 = float(item.dim13)
                    old_dim12 = float(item.dim12)
                    old_dim14 = float(item.dim14)
                    old_dim15 = float(item.dim15)
                    old_dimv_1 = (float(item.question_40) + float(item.question_41)) * 0.83
                    old_dimv_2 = (float(item.question_42) + float(item.question_43)) * 0.83
                    old_dimv_3 = (float(item.question_44) + float(item.question_45)) * 0.83
                    old_dimv_4 = (float(item.question_46) + float(item.question_47)) * 0.83
                    old_dimv_5 = (float(item.question_48) + float(item.question_49)) * 0.83
                print("old_dim11", old_dim11)
                print("old_dimv_1", old_dimv_1)
                if dim11 > (old_dim11 - old_dimv_1):
                    m = dim11 + old_dimv_1
                    dim11 = m
                    print("dim11", dim11)
                else:
                    dim11 = old_dim11
                if dim12 > (old_dim12 - old_dimv_2):
                    m = dim12 + old_dimv_2
                    dim12 = m
                else:
                    dim12 = old_dim12
                if dim13 > (old_dim13 - old_dimv_3):
                    m = dim13 + old_dimv_3
                    dim13 = m
                else:
                    dim13 = old_dim13
                if dim14 > (old_dim14 - old_dimv_4):
                    m = dim14 + old_dimv_4
                    dim14 = m
                else:
                    dim14 = old_dim14
                if dim15 > (old_dim15 - old_dimv_5):
                    m = dim15 + old_dimv_5
                    dim15 = m
                else:
                    dim15 = old_dim15
                cons = dim11 + dim12 + dim13 + dim14 + dim15
                # 将数据更新到数据库
                session.query(Answer).filter_by(username=username).update(
                    {'dim11': dim11, 'dim12': dim12, 'dim13': dim13, 'dim14': dim14, 'dim15': dim15,'cons':cons})
                session.commit()  # 不要忘了commit
                session.close()
                print("数据更新成功")
        except:
            print("数据更新失败")

        status = 0
    if scene_number == 1:  # 冒充客服人员，子场景一,测试维度包括风险感知CA、社会易感 BC
        dim15 = 0  # 网络经验
        dim12 = 0  # 信任
        dim11 = 0  # 风险感知##
        dim13 = 0  # 自我控制
        dim14 = 0  # 社会易感###

        if answer_1 == "C":
            dim11 += 2.5
        if answer_2 == "A":
            dim11 += 2.5
        if answer_3 == "B":
            dim14 += 2.5
        if answer_4 == "C":
            dim14 += 2.5
        re_str = "恭喜你，风险感知和社会易感各提升" + str(dim11) + "、" + str(dim14) + "分。请在主场景学习进度中查看详情"
        data_re = session.query(Answer).filter(Answer.username == username)
        time = 0
        for item in data_re:
            time += 1
        try:
            if time > 0:  # 表明数据库中有数据，用户登录微信小程序了
                for item in data_re:
                    old_dim11 = float(item.dim11)
                    old_dim13 = float(item.dim13)
                    old_dim12 = float(item.dim12)
                    old_dim14 = float(item.dim14)
                    old_dim15 = float(item.dim15)
                    old_dimv_1 = (float(item.question_40) + float(item.question_41)) * 0.83
                    old_dimv_2 = (float(item.question_42) + float(item.question_43)) * 0.83
                    old_dimv_3 = (float(item.question_44) + float(item.question_45)) * 0.83
                    old_dimv_4 = (float(item.question_46) + float(item.question_47)) * 0.83
                    old_dimv_5 = (float(item.question_48) + float(item.question_49)) * 0.83
                print("old_dim11", old_dim11)
                print("old_dimv_1", old_dimv_1)
                if dim11 > (old_dim11 - old_dimv_1):
                    m = dim11 + old_dimv_1
                    dim11 = m
                    print("dim11", dim11)
                else:
                    dim11 = old_dim11
                if dim12 > (old_dim12 - old_dimv_2):
                    m = dim12 + old_dimv_2
                    dim12 = m
                else:
                    dim12 = old_dim12
                if dim13 > (old_dim13 - old_dimv_3):
                    m = dim13 + old_dimv_3
                    dim13 = m
                else:
                    dim13 = old_dim13
                if dim14 > (old_dim14 - old_dimv_4):
                    m = dim14 + old_dimv_4
                    dim14 = m
                else:
                    dim14 = old_dim14
                if dim15 > (old_dim15 - old_dimv_5):
                    m = dim15 + old_dimv_5
                    dim15 = m
                else:
                    dim15 = old_dim15
                cons = dim11 + dim12 + dim13 + dim14 + dim15
                # 将数据更新到数据库
                session.query(Answer).filter_by(username=username).update(
                    {'dim11': dim11, 'dim12': dim12, 'dim13': dim13, 'dim14': dim14, 'dim15': dim15,'cons':cons})
                session.commit()  # 不要忘了commit
                session.close()
                print("数据更新成功")
        except:
            print("数据更新失败")

        status = 0
    if scene_number == 4:  # 刷单返利，子场景四,测试维度包括信息加工（经验因素）CC、风险感知 BA
        dim15 = 0  # 网络经验
        dim12 = 0  # 信任
        dim11 = 0  # 风险感知##
        dim13 = 0  # 自我控制
        dim14 = 0  # 社会易感###
        message = 0  # 信息加工

        if answer_1 == "C":
            message += 2.5
        if answer_2 == "C":
            message += 2.5
        if answer_3 == "B":
            dim11 += 2.5
        if answer_4 == "A":
            dim11 += 2.5
        re_str = "恭喜你，信息加工和风险感知各提升" + str(message) + "、" + str(dim11) + "分。请在主场景学习进度中查看详情"
        data_re = session.query(Answer).filter(Answer.username == username)
        time = 0
        for item in data_re:
            time += 1
        try:
            if time > 0:  # 表明数据库中有数据，用户登录微信小程序了
                for item in data_re:
                    old_dim11 = float(item.dim11)
                    old_dim13 = float(item.dim13)
                    old_dim12 = float(item.dim12)
                    old_dim14 = float(item.dim14)
                    old_dim15 = float(item.dim15)
                    old_dim16 = float(item.dim16)  # 该点比较特殊
                    old_dimv_1 = (float(item.question_40) + float(item.question_41)) * 0.25 * 2.5
                    old_dimv_2 = (float(item.question_42) + float(item.question_43)) * 0.25 * 2.5
                    old_dimv_3 = (float(item.question_44) + float(item.question_45)) * 0.25 * 2.5
                    old_dimv_4 = (float(item.question_46) + float(item.question_47)) * 0.25 * 2.5
                    old_dimv_5 = (float(item.question_48) + float(item.question_49)) * 0.25 * 2.5
                    old_dimv_6 = (float(item.question_29) + float(item.question_30) + float(item.question_31) + float(
                        item.question_32) + float(item.question_33) + float(item.question_34) + float(
                        item.question_35)) * 0.2 * 2.5+2.5
                print("old_dim11", old_dim11)
                print("old_dimv_1", old_dimv_1)
                if message > (old_dim16 - old_dimv_6):
                    m = message + old_dimv_6
                    message = m
                    print("message5", message)
                else:
                    message = old_dim16
                    print("message", message)
                if dim11 > (old_dim11 - old_dimv_1):
                    m = dim11 + old_dimv_1
                    dim11 = m
                    print("dim11", dim11)
                else:
                    dim11 = old_dim11
                if dim12 > (old_dim12 - old_dimv_2):
                    m = dim12 + old_dimv_2
                    dim12 = m
                else:
                    dim12 = old_dim12
                if dim13 > (old_dim13 - old_dimv_3):
                    m = dim13 + old_dimv_3
                    dim13 = m
                else:
                    dim13 = old_dim13
                if dim14 > (old_dim14 - old_dimv_4):
                    m = dim14 + old_dimv_4
                    dim14 = m
                else:
                    dim14 = old_dim14
                if dim15 > (old_dim15 - old_dimv_5):
                    m = dim15 + old_dimv_5
                    dim15 = m
                else:
                    dim15 = old_dim15
                cons=dim11+dim12+dim13+dim14+dim15+message
                # 将数据更新到数据库
                session.query(Answer).filter_by(username=username).update(
                    {'dim11': dim11, 'dim12': dim12, 'dim13': dim13, 'dim14': dim14, 'dim15': dim15, 'dim16': message,'cons':cons})
                session.commit()  # 不要忘了commit
                session.close()
                print("数据更新成功")
        except:
            print("数据更新失败")

        status = 0
    if scene_number == 3:  # 网络游戏虚拟交易，子场景三,测试维度包括网络经验AB、风险感知 BC
        dim15 = 0  # 网络经验###
        dim12 = 0  # 信任###
        dim11 = 0  # 风险感知##
        dim13 = 0  # 自我控制
        dim14 = 0  # 社会易感

        if answer_1 == "A":
            dim11 += 2.5
        if answer_2 == "B":
            dim12 += 2.5
        if answer_3 == "B":
            dim12 += 2.5
        if answer_4 == "C":
            dim15 += 2.5
        re_str = "恭喜你，风险感知、信任和网络经验各提升" + str(dim11) + "、" + str(dim12) + "、" + str(dim15) +"分。请在主场景学习进度中查看详情"
        data_re = session.query(Answer).filter(Answer.username == username)
        time = 0
        for item in data_re:
            time += 1
        try:
            if time > 0:  # 表明数据库中有数据，用户登录微信小程序了
                for item in data_re:
                    old_dim11 = float(item.dim11)
                    old_dim13 = float(item.dim13)
                    old_dim12 = float(item.dim12)
                    old_dim14 = float(item.dim14)
                    old_dim15 = float(item.dim15)
                    old_dimv_1 = (float(item.question_40) + float(item.question_41)) * 0.83
                    old_dimv_2 = (float(item.question_42) + float(item.question_43)) * 0.83
                    old_dimv_3 = (float(item.question_44) + float(item.question_45)) * 0.83
                    old_dimv_4 = (float(item.question_46) + float(item.question_47)) * 0.83
                    old_dimv_5 = (float(item.question_48) + float(item.question_49)) * 0.83
                print("old_dim11", old_dim11)
                print("old_dimv_1", old_dimv_1)
                if dim11 > (old_dim11 - old_dimv_1):
                    m = dim11 + old_dimv_1
                    dim11 = m
                    print("dim11", dim11)
                else:
                    dim11 = old_dim11
                if dim12 > (old_dim12 - old_dimv_2):
                    m = dim12 + old_dimv_2
                    dim12 = m
                else:
                    dim12 = old_dim12
                if dim13 > (old_dim13 - old_dimv_3):
                    m = dim13 + old_dimv_3
                    dim13 = m
                else:
                    dim13 = old_dim13
                if dim14 > (old_dim14 - old_dimv_4):
                    m = dim14 + old_dimv_4
                    dim14 = m
                else:
                    dim14 = old_dim14
                if dim15 > (old_dim15 - old_dimv_5):
                    m = dim15 + old_dimv_5
                    dim15 = m
                else:
                    dim15 = old_dim15
                cons = dim11 + dim12 + dim13 + dim14 + dim15
                # 将数据更新到数据库
                session.query(Answer).filter_by(username=username).update(
                    {'dim11': dim11, 'dim12': dim12, 'dim13': dim13, 'dim14': dim14, 'dim15': dim15,'cons':cons})
                session.commit()  # 不要忘了commit
                session.close()
                print("数据更新成功")
        except:
            print("数据更新失败")

        status = 0
    if scene_number == 5:  # 理财投资，子场景五,测试维度包括风险感知BB、信任 AC
        dim15 = 0  # 网络经验
        dim12 = 0  # 信任###
        dim11 = 0  # 风险感知##
        dim13 = 0  # 自我控制
        dim14 = 0  # 社会易感

        if answer_1 == "B":
            dim11 += 2.5
        if answer_2 == "B":
            dim11 += 2.5
        if answer_3 == "A":
            dim12 += 2.5
        if answer_4 == "C":
            dim12 += 2.5
        re_str = "恭喜你，风险感知和信任各提升" + str(dim11) + "、" + str(dim12) + "分。请在主场景学习进度中查看详情"
        data_re = session.query(Answer).filter(Answer.username == username)
        time = 0
        for item in data_re:
            time += 1
        try:
            if time > 0:  # 表明数据库中有数据，用户登录微信小程序了
                for item in data_re:
                    old_dim11 = float(item.dim11)
                    old_dim13 = float(item.dim13)
                    old_dim12 = float(item.dim12)
                    old_dim14 = float(item.dim14)
                    old_dim15 = float(item.dim15)
                    old_dimv_1 = (float(item.question_40) + float(item.question_41)) * 0.83
                    old_dimv_2 = (float(item.question_42) + float(item.question_43)) * 0.83
                    old_dimv_3 = (float(item.question_44) + float(item.question_45)) * 0.83
                    old_dimv_4 = (float(item.question_46) + float(item.question_47)) * 0.83
                    old_dimv_5 = (float(item.question_48) + float(item.question_49)) * 0.83
                print("old_dim11", old_dim11)
                print("old_dimv_1", old_dimv_1)
                if dim11 > (old_dim11 - old_dimv_1):
                    m = dim11 + old_dimv_1
                    dim11 = m
                    print("dim11", dim11)
                else:
                    dim11 = old_dim11
                if dim12 > (old_dim12 - old_dimv_2):
                    m = dim12 + old_dimv_2
                    dim12 = m
                else:
                    dim12 = old_dim12
                if dim13 > (old_dim13 - old_dimv_3):
                    m = dim13 + old_dimv_3
                    dim13 = m
                else:
                    dim13 = old_dim13
                if dim14 > (old_dim14 - old_dimv_4):
                    m = dim14 + old_dimv_4
                    dim14 = m
                else:
                    dim14 = old_dim14
                if dim15 > (old_dim15 - old_dimv_5):
                    m = dim15 + old_dimv_5
                    dim15 = m
                else:
                    dim15 = old_dim15
                cons = dim11 + dim12 + dim13 + dim14 + dim15
                # 将数据更新到数据库
                session.query(Answer).filter_by(username=username).update(
                    {'dim11': dim11, 'dim12': dim12, 'dim13': dim13, 'dim14': dim14, 'dim15': dim15,'cons':cons})
                session.commit()  # 不要忘了commit
                session.close()
                print("数据更新成功")
        except:
            print("数据更新失败")

        status = 0
    data = {
        "username": username,
        "re_str": re_str,
    }
    return jsonify(data)  # 返回布尔值


# 进行本地测试代码
@app.route("/cj", methods=['POST', 'GET', 'PUT'])
def bdcj():
    if request.method == 'POST':
        studydata = request.get_json()
        print("测验数据获取成功")
    else:
        print("请以post请求进行访问")
        # username = int(request.args.get('username'))
        # password = int(request.args.get('password'))
    print(studydata)
    return jsonify(studydata)  # 返回布尔值


# 进行随时保存用户信息
@app.route("/cv", methods=['POST', 'GET', 'PUT'])
def user_cv():

    if request.method == 'POST':
        users_data = request.get_json()
    else:
        print("请以post请求进行访问")
        users_data = 0
        # username = int(request.args.get('username'))
        # password = int(request.args.get('password'))
    print(users_data)
    username=users_data["username"]
    # 往MySQL数据进行条件查询
    logstatus = session.query(Users).filter(Users.username == username)
    time = 0
    for item in logstatus:
        time += 1
    # print("查询行数为："+str(time))
    status = 0
    if time > 0:
        status = 1  # 表示查询到结果，登录成功
    else:#对用户进行保存
        # add_user = Users("test", "test123@qq.com")
        # session.add(add_user)
        # session.commit()
        U=Users(username=username,nickname='罗布乐思',password=123456,sex=0,age=0,score=0)
        session.add(U)
        session.commit()  # 不要忘了commit
        session.close()
        status = 0  # 表示没有查询到结果，登录失败
    print(time,status,username)
    return jsonify(username)  # 返回布尔值

Base.metadata.create_all(engine)  # 这就是为什么表类一定要继承Base，因为Base会通过一些方法来通过引擎初始化数据库结构。不继承Base自然就没有办法和数据库发生联系了。
session = Session()  # 创建session对象
# #
# # 模拟部分数据进行保存到数据库
# for i in range(5):
#     U = Answer(username="smilepython",questionnaire_id=1,cons=666,dim1=55,dim2=55,dim3=55,
#                question_1=4,
#                question_2=4,
#                question_3=4,
#                question_4=4,
#                question_5=4,
#                question_6=4,
#                question_7=4,
#                question_8=4,
#                question_9=4,
#                question_10=4,
#                question_11=4,
#                question_12=4,
#                question_13=4,
#                question_14=4,
#                question_15=4,
#                question_16=4,
#                question_17=4,
#                question_18=4,
#                question_19=4,
#                question_20=4,
#                question_21=4,
#                question_22=4,
#                question_23=4,
#                question_24=4,
#                question_25=4,
#                question_26=4,
#                question_27=4,
#                question_28=4,
#                question_29=4,
#                question_30=4,
#                question_31=4,
#                question_32=4,
#                question_33=4,
#                question_34=4,
#                question_35=4,
#                question_36='A',
#                question_37='A',
#                question_38='A',
#                question_39='A',
#                question_40='A',
#                question_41='A',
#                question_42='A',
#                question_43='A',
#                question_44='A',
#                question_45='A',
#                question_46='A',
#                question_47='A',
#                question_48='A',
#                question_49='A',)
#     session.add(U)
#     session.commit()  # 不要忘了commit
#     session.close()
#
#     print("保存成功！")

# if __name__ == '__main__':
#     # app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
#     app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)

if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
    app.run(host="0.0.0.0", port=5000,ssl_context=('8427159_rbxerg.top.pem', '8427159_rbxerg.top.key'))
    
    
    
    
    