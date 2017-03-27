from bottle import route, run, template, request, hook, error, redirect, response
from peewee import *
import jwt


db = SqliteDatabase('domru.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    """  ласс пользователей """ 
    name = CharField(30)
    role = CharField(15)
    password = CharField(8)

    # метод добавлени€ пользовател€
    def editUser(self,n,r,p):
        self.name = n
        self.role = r
        self.password = p

class Gift(BaseModel):
    """  ласс подарков """
    gType = CharField(20)

    # метод добавлени€ подарка
    def editGift(self,t):
        self.gType = t

class GiftList(BaseModel):
    """ —водный список подарков пользователей """
    owner = ForeignKeyField(User, related_name='Gifts')
    gifType = ForeignKeyField(Gift, related_name='Users')

class AuthData(BaseModel):
    '''ћодель дл€ авторизации пользователей'''
    user = CharField(30)
    token = CharField()

try:
    User.create_table()
    #User.create(name='Admin',role='Admin',password='admin')
except OperationalError:
    print "User table already exists!"
 
try:
    Gift.create_table()
except OperationalError:
    print "Gift table already exists!"

try:
    GiftList.create_table()
except OperationalError:
    print "GiftList table already exists!"

try:
    AuthData.create_table()
    #encoded = jwt.encode({'Admin':'admin'},'secret',algorithm='HS256')
    #AuthData.create(user='Admin',token=encoded)
except OperationalError:
    print "Auth table already exists!" 

def dlist():
    '''Return list of dict for Gift_List table'''
    bbn=[]
    for gl in GiftList.select():
        bbn.append([{'uname':gl.owner.name,'idu':gl.owner.id,'gtype':gl.gifType.gType,'idg':gl.gifType.id}])
    return bbn

def gift_info(gid):
    '''Return Gift for Web'''
    gft = Gift.get(Gift.id == gid)
    return gft

def user_info(name):
    '''Return User for Web'''
    usr = User.get(User.name == name)
    return usr

def user_gifts(name):
    '''Return list of gifts for current user'''
    lst=[]
    for gf in Gift.select().join(GiftList).where(GiftList.owner == User.get(User.name == name)):
        lst.append({'gid':gf.id,'gtype':gf.gType})
    return lst

def get_user_list():
    '''Return all users in DB'''
    lst2=[]
    for us in User.select():
        lst2.append({'uname':us.name,'urole':us.role})
    return lst2

def get_gift_list():
    '''Return all type of gifts in DB'''
    ls = [] 
    for gft in Gift.select():
        ls.append({'gid':gft.id,'gtype':gft.gType})
    return ls

def get_giftlist_item(name,gid):
    '''Return item in GiftList table for user'''
    usr = user_info(name)
    gft = gift_info(gid)
    ls = []
    ls.append({'uname':usr.name,'urole':usr.role,'gtype':gft.gType, 'gid':gft.id})
    return ls

def get_auth():
    '''Get Auth User Role'''
    try:
        user = 'None'
        tkn = request.get_cookie("token")
        ad = AuthData.get(AuthData.token==tkn)
        if not ad is None :
            user = user_info(ad.user).role
    except:
        user = 'None'
    return user    

@route('/')
@route('/login')
def do_login():
    if request.get_cookie("token") is None:
        output = template('login')
    else:
        output = redirect('/presents')
    return  output

@route('/', method='POST')
@route('/login', method='POST')
def index():
    '''main page of project'''
    unm = request.POST.get('name','').strip()
    psswrd = request.POST.get('password','').strip()
    try:
        auth = AuthData.get(AuthData.user==unm)
    except:
        return '<p>User does not exist</p><a href=''/login''>Return to login</a>'
    encoded = jwt.encode({unm:psswrd},'secret',algorithm='HS256')
    if request.POST.get('login','').strip():
        if encoded == auth.token:
            response.set_cookie("token", encoded)
            output = '<p>User is authorized</p><a href=''/presents''>Go to Presents List</a>'
        else:
            output = '<p>User does not exist</p><a href=''/login''>Return to login</a>'
        return output 

@route('/presents')
def presents():
    '''main page of project'''
    try:
        rtt = dlist()
    except:
        rtt = 'nothing'
    user = get_auth()
    output = template('make_table', rows=rtt,usr=user)
    return output

@route('/addpresent', method='GET')
def add_present():
    '''Add new present in DB'''
    if request.GET.get('save','').strip():
        unm = request.GET.get('name','').strip()
        gid = request.GET.get('gid','').strip()
        try:
            usr = user_info(unm)
            gft = gift_info(gid)
            GiftList.create(owner=usr,gifType=gft)
            output = template('<p>New present {{gtype}} for user {{name}} has inserted in DB</p><a href=''/''>Return to main page</a>', gtype=gft.gType, name=unm)
        except:
            output = '<p>have some problems</p><a href=''/users''>Return to User list</a>'
    else:
        ulst = get_user_list()
        glst =get_gift_list()
        user = get_auth()
        output = template('add_present',usrs=ulst,gfts=glst,usr=user)        
    return output

@route('/users')
def user_list():
    '''Return list of all users'''
    lst1 = get_user_list()
    user = get_auth()
    output = template('user_list', lst=lst1,usr=user)
    return output

@route('/users/new', method='GET')
def new_user():
    '''Add new user to DB'''
    if request.GET.get('save','').strip():
        unm = request.GET.get('name','').strip()
        url = request.GET.get('role','').strip()
        psswrd = request.GET.get('password','').strip()
        encoded = jwt.encode({unm:psswrd},'secret',algorithm='HS256')
        try:
            User.create(name=unm,role=url,password=psswrd)
            AuthData.create(user=unm,token=encoded)
            output = '<p>New user has inserted in DB</p><a href=''/users''>Return to User list</a>'
        except:
            output = '<p>have some problems</p><a href=''/users''>Return to User list</a>'
        return output
    else:
        user = get_auth() 
        output = template('new_user',usr=user)
        return output

@route('/users/<name>')
def user_id(name):
    '''Show info for current user'''
    nm = str(name)
    usr1 = user_info(nm)
    lst1 = user_gifts(nm)
    user = get_auth()
    output = template('user_info', usr=usr1, glist=lst1, usr1=user)
    return output

@route('/users/<name>/edit', method='GET')
def user_id(name):
    '''Edit current user info'''
    usr2 = user_info(name)
    if request.GET.get('save','').strip():
        unm = request.GET.get('name','').strip()
        url = request.GET.get('role','').strip()
        password = request.GET.get('password','').strip()
        try:
            usr2.editUser(unm,url,password)
            usr2.save()
            output = '<p>User edited</p><a href=''/users''>Return to User list</a>'
        except:
            output = '<p>have some problems</p><a href=''/users''>Return to User list</a>'
        return output
    else:
        user = get_auth()
        output = template('user_edit', usr=usr2, usr1=user)
        return output

@route('/users/<name>/present/<gid>')
def user_gift(name,gid):
    '''Show present info for current user'''
    ls = []
    ls = get_giftlist_item(name,gid)
    output = template('gl_info',lsinfo=ls)
    return output

@route('/gifts')
def gift_list():
    '''Return list of all gifts'''
    ls3 = get_gift_list()
    user = get_auth()
    output = template('gift_list', glst=ls3, usr=user)
    return output


@route('/gifts/new', method="GET")
def gift_list():
    '''Add new gift'''
    if request.GET.get('save','').strip():
        gtype = request.GET.get('gtype','').strip()
        try:
            Gift.create(gType=gtype)
            output = '<p>New gift has inserted in DB</p><a href=''/gifts''>Return to gift list</a>'
        except:
            output = '<p>have some problems</a><a href=''/gifts''>Return to gift list</a>'
        return output
    else:
        user = get_auth()
        output = template('new_gift', usr=user)
        return output

@route('/gifts/<gid>')
def type_gift(gid):
    '''Show info of current gift'''
    gft = gift_info(gid)
    gls=[]
    gls.append({'gtype':gft.gType,'gid':gft.id}) 
    output = template('gift_info',gf=gls)
    return output

from bottle import error
@error(404)
@error(403)
def mistake(code):
    return 'There is something wrong! <a href="/">Go to main page</a>'

run(host='localhost', port=8080, debug=True)
