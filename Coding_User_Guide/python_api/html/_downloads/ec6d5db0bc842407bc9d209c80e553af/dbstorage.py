import ansa
import pickle
from ansa import base
from ansa import constants
from ansa import session

def save_ansa_db():
    session.New('discard')

    dbs = base.DBStorage()

    dbs.set('ia', 15)
    dbs.set('ib', 16)

    dbs.set('da', 17.)
    dbs.set('db', 18.)

    dbs.set('sa', 'earth')
    dbs.set('sb', 'moon')
    node = base.CreateEntity(constants.ABAQUS, 'NODE', {'Name': 'User node'})
    my_dict = {'name': 'Bob', 'company': 'BETA CAE', 'node': node}
    p_my_dict = pickle.dumps(my_dict)
    dbs.set('my_info', p_my_dict)

    base.SaveAs('/home/Desktop/db.ansa')

    del dbs

def read_ansa_db():

    session.New('discard')

    base.Open('/home/Desktop/db.ansa')

    dbs = base.DBStorage()

    ia = dbs.get('ia', 0)
    print('ia:', ia)
    ib = dbs.get('ib', 0)
    ic = dbs.get('ic', 0)

    dbs.remove('ia')

    da = dbs.get('da', 0.)
    db = dbs.get('db', 0.)
    dc = dbs.get('dc', 0.)

    sa = dbs.get('sa', 'default')
    print('sa:', sa)
    sb = dbs.get('sb', 'default')
    dc = dbs.get('dc', 'default')
    v = dbs.get('my_info')
    my_info = pickle.loads(v)
    print('my info:', my_info)
    print('my info: node:', my_info['node'])
