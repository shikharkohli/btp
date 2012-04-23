import allimports

user_id = ['anil', 'shikhar', 'ajit']
password = ['pwd1', 'pwd2', 'pwd3']
mask=[1,3,2]

def register_user(user_id, user_pwd, user_mask):
    user_name=user_id
    user_weight=0
    user_attr={'user_pwd': user_pwd, 'user_mask':user_mask, 'weight':user_weight}
    flag=allimports.dom_user.put_attributes(user_name, user_attr)
    while(flag==False):
        print "looping..\n"
    print "username: " + user_name,
    print "password: " + user_pwd,
    print "mask ",
    print user_mask
    print "inserted..\n"

def like(user_id, url_id):
    u=allimports.dom_user.get_item(user_id)
    mask=u['user_mask']
    name=mask
    attr={'url_ids':url_id}
    flag=allimports.dom_likes.put_attributes(name,attr)
    while(flag==False):
        print "looping..\n"
    print "inserted"
     

for i in range(0,3):
    register_user(user_id[i],password[i],mask[i])
