import sqlite3

db = sqlite3.connect("theo.db")
dbc = db.cursor()


dbc.execute("""CREATE TABLE IF NOT EXISTS groups (chat_id INTEGER PRIMARY KEY,
                                                  welcome,
                                                  welcome_enabled INTEGER,
                                                  rules,
                                                  goodbye,
                                                  goodbye_enabled INTEGER,
                                                  warns_limit INTEGER,
                                                  chat_lang,
                                                  start,
                                                  cached_admins)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY,
                                                 start,
                                                 chat_lang)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS channels (chat_id INTEGER PRIMARY KEY)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS generalban (user_id INTEGER PRIMARY KEY,
                                                 firstname)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS generalmute (user_id INTEGER PRIMARY KEY,
                                                 firstname)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS generalreply (text, reply)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS wait (key,
                                                 user_id INTEGER, chat_id INTEGER)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS waitg (key,
                                                 gamekey, chat_id INTEGER)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS botname (name)""")

##################################################################################
##################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS ban (user_id,
                                                 firstname, chat_id INTEGER)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS mute (user_id,
                                                 firstname, chat_id INTEGER)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS priban (user_id,
                                                 firstname, chat_id INTEGER)""")

##################################################################################
##################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS groupcheck (key, chat_id, name)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS usercheck (key, user_id, name)""")

##################################################################################
##################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS developer (user_id INTEGER PRIMARY KEY,
                                                     firstname)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS secdeveloper (user_id INTEGER PRIMARY KEY,
                                                     firstname)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS genspecial (user_id INTEGER PRIMARY KEY,
                                                     firstname)""")

##################################################################################
##################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS manager (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS constructor (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS admin (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS special (firstname,
                                                        user_id, chat_id)""")

#################################################################################
#################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS replygroup (text, reply, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locktext (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockmnshn (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locklink (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locklinkban (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locklinkmute (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockphoto (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockvideo (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locksticker (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockanimation (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockaudio (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockvoice (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockforward (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockforwardban (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockforwardmute (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockdocument (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockcontact (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockreply (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockfshar (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockfsharban (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockfsharmute (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockzhrafa (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockmusic (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockaflam (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockyoutube (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locktranslate (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS blocktext (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS blocktextban (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS blocktextmute (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locknotification (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockupper (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockazkar (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockazkar2 (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockgames (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locktag (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockdeletelink (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockkickme (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockmeendafny (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockrwayat (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS kickbotatban (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS namemeaning (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS abrag (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS locklinggroup (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS idgroup (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS idgroup2 (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS myphoto (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS entrygp (key, chat_id)""")

#################################################################################
#################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS locksendmsg (key)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockbroadcast (key)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockgenyoutube (key)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockgenmnshn (key)""")

#################################################################################
#################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS addlinkgroup (link, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockwelcome (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS addwelcomegroup (welcome, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS lockbye (key, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS addbyegroup (bye, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS addcomand (command, newcommand, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS addcustomid (customid, chat_id)""")

#################################################################################
#################################################################################


dbc.execute("""CREATE TABLE IF NOT EXISTS lonely (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS caw (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS stupid (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS donkey (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS dog (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS monkey (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS hours (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS naked (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS mywife (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS myheart (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS bestfriend (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS abit (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS abny (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS bnty (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS dakry (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS fashel (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS hyawan (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS khain (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS khaina (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS khazok (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS mohzaa (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS otty (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS rkasa (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS wtka (firstname,
                                                        user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS zogy (firstname,
                                                        user_id, chat_id)""")

#################################################################################
#################################################################################

dbc.execute("""CREATE TABLE IF NOT EXISTS meendafny (user_id_add INTEGER, firstname_add,
                                                 user_id_added INTEGER, chat_id INTEGER)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS mycontact (counter INTEGER, user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS mypointgame (counter INTEGER, user_id, chat_id)""")

dbc.execute("""CREATE TABLE IF NOT EXISTS mymessage (counter INTEGER, user_id, chat_id)""")

db.commit()


#######################################################################################################
#######################################################################################################


def set_db_checkgroup(key: str, chat_id: int, name: str):
    dbc.execute("INSERT INTO groupcheck(key, chat_id, name) VALUES (?, ?, ?)", (key, chat_id, name))
    db.commit()


def del_db_checkgroup(chat_id: int):
    dbc.execute("DELETE FROM groupcheck WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_checkgroup(chat_id: int):
    dbc.execute("SELECT key FROM groupcheck WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def get_db_checkgroupall():
    dbc.execute("SELECT * FROM groupcheck")
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_checkuser(key: str, user_id: int, name: str):
    dbc.execute("INSERT INTO usercheck(key,user_id,name) VALUES(?,?,?)", (key, user_id, name))
    db.commit()


def del_db_checkuser(chat_id: int):
    dbc.execute("DELETE FROM usercheck WHERE user_id = ? ", (chat_id,))
    db.commit()


def get_db_checkuser(user_id: int):
    dbc.execute("SELECT key FROM usercheck WHERE user_id = ?", (user_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def get_db_checkuserall():
    dbc.execute("SELECT * FROM usercheck")
    ul = dbc.fetchall()
    return ul if ul else None
  
#######################################################################################################
#######################################################################################################

active = []
stream = {} 
ddb = {}


async def is_active(chat_id: int) -> bool:
    if chat_id not in active:
        return False
    else:
        return True


async def add_active(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)


async def remove_active(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)


async def is_streaming(chat_id: int) -> bool:
    run = stream.get(chat_id)
    if not run:
        return False
    return run


async def stream_on(chat_id: int):
    stream[chat_id] = True


async def stream_off(chat_id: int):
    stream[chat_id] = False


async def clear(chat_id: int):
    try:
        ddb[chat_id] = []
    except:
        pass
    try:
        await remove_active(chat_id)
    except:
        pass
    try:
        await stream_off(chat_id)
    except:
        pass

#######################################################################################################
#######################################################################################################

async def add(
    chat_id,
    file_path,
    link,
    title,
    duration,
    videoid,
    type,
    user_id):
    put = {
        "title": title,
        "duration": duration,
        "user_id": user_id,
        "chat_id": chat_id,
        "type": type,
        "file_path": file_path,
        "link": link,
        "videoid": videoid,
        "played": 0,
    }
    i = ddb.get(chat_id)
    if not i:
        ddb[chat_id] = []
    ddb[chat_id].append(put)
    return

#######################################################################################################
#######################################################################################################

def set_db_gban(user_id: int, firstname: str):
    dbc.execute("INSERT INTO generalban(user_id,firstname) VALUES(?,?)", (user_id, firstname))
    db.commit()


def del_db_gban(user_id: int):
    dbc.execute("DELETE FROM generalban WHERE user_id = ?", (user_id,))
    db.commit()


def del_db_gbanall():
    dbc.execute("DELETE FROM generalban")
    db.commit()


def get_db_gban():
    dbc.execute("SELECT * FROM generalban")
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_gmute(user_id: int, firstname: str):
    dbc.execute("INSERT INTO generalmute(user_id,firstname) VALUES(?,?)", (user_id, firstname))
    db.commit()


def del_db_gmute(user_id: int):
    dbc.execute("DELETE FROM generalmute WHERE user_id = ?", (user_id,))
    db.commit()


def del_db_gmuteall():
    dbc.execute("DELETE FROM generalmute")
    db.commit()


def get_db_gmute():
    dbc.execute("SELECT * FROM generalmute")
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_privban(user_id: int, firstname: str, chat_id: int):
    dbc.execute("INSERT INTO priban(user_id,firstname,chat_id) VALUES(?,?,?)", (user_id, firstname, chat_id))
    db.commit()


def del_db_priban(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM priban WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_pribanall(chat_id: int):
    dbc.execute("DELETE FROM priban WHERE chat_id = ?", (chat_id,))
    db.commit()


def drop_db_pribanallall():
    dbc.execute("DROP TABLE priban")
    dbc.execute("""CREATE TABLE IF NOT EXISTS priban (user_id,
                                                     firstname, chat_id INTEGER)""")
    db.commit()


def get_db_priban(chat_id: int):
    dbc.execute("SELECT * FROM priban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_greply(text: str, reply: str):
    dbc.execute("INSERT INTO generalreply (text,reply) VALUES(?,?)", (text, reply))
    db.commit()


def del_db_greply(text: str):
    dbc.execute("DELETE FROM generalreply WHERE text = ?", (text,))
    db.commit()


def del_db_grepall():
    dbc.execute("DELETE FROM generalreply")
    db.commit()


def get_db_greply():
    dbc.execute("SELECT * FROM generalreply")
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_wait(key: str, user_id: int, chat_id: int):
    dbc.execute("INSERT INTO wait (key,user_id,chat_id) VALUES(?,?,?)", (key, user_id, chat_id))
    db.commit()


def del_db_wait(key: str):
    dbc.execute("DELETE FROM wait WHERE key = ?", (key,))
    db.commit()


def get_db_wait():
    dbc.execute("SELECT * FROM wait")
    ul = dbc.fetchall()
    return ul if ul else None


def drop_db_wait():
    dbc.execute("DROP TABLE wait")
    dbc.execute("""CREATE TABLE IF NOT EXISTS wait (key,
                                                     user_id INTEGER, chat_id INTEGER)""")
    db.commit()


def set_db_waitg(key: str, gamekey: str, chat_id: int):
    dbc.execute("INSERT INTO waitg (key,gamekey,chat_id) VALUES(?,?,?)", (key, gamekey, chat_id))
    db.commit()


def del_db_waitg(key: str):
    dbc.execute("DELETE FROM waitg WHERE key = ?", (key,))
    db.commit()


def get_db_waitg(chat_id: int):
    dbc.execute("SELECT * FROM waitg WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def drop_db_waitq():
    dbc.execute("DROP TABLE waitg")
    dbc.execute("""CREATE TABLE IF NOT EXISTS waitg (key,
                                                     gamekey, chat_id INTEGER)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_botname(botname: str):
    dbc.execute("INSERT INTO botname(name) VALUES(?)", (botname,))
    db.commit()


def del_db_botname():
    dbc.execute("DELETE FROM botname")
    db.commit()


def get_db_botname():
    dbc.execute("SELECT name FROM botname")
    ul = dbc.fetchone()
    return ul[0] if ul else None


#######################################################################################################
#######################################################################################################

def set_db_general_rtb(databasename, user_id: int, firstname: str):
    dbc.execute("INSERT INTO " + databasename + "(user_id,firstname) VALUES(?,?)", (user_id, firstname))
    db.commit()


def del_db_general_rtb(databasename, user_id: int):
    dbc.execute("DELETE FROM " + databasename + " WHERE user_id = ?", (user_id,))
    db.commit()


def del_db_general_rtball(databasename):
    dbc.execute("DELETE FROM " + databasename)
    db.commit()


def get_db_general_rtb(databasename):
    dbc.execute("SELECT * FROM " + databasename)
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_manager(firstname: str, user_id: int, chat_id: int):
    dbc.execute("INSERT INTO manager(firstname,user_id,chat_id) VALUES(?,?,?)", (firstname, user_id, chat_id))
    db.commit()


def del_db_manager(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM manager WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_managerall(chat_id: int):
    dbc.execute("DELETE FROM manager WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_manager(chat_id: int):
    dbc.execute("SELECT * FROM manager WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_constractors(firstname: str, user_id: int, chat_id: int):
    dbc.execute("INSERT INTO constructor(firstname,user_id,chat_id) VALUES(?,?,?)",
                       (firstname, user_id, chat_id))
    db.commit()


def del_db_constractors(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM constructor WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_constractorsall(chat_id: int):
    dbc.execute("DELETE FROM constructor WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_constractors(chat_id: int):
    dbc.execute("SELECT * FROM constructor WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_admin(firstname: str, user_id: int, chat_id: int):
    dbc.execute("INSERT INTO admin(firstname,user_id,chat_id) VALUES(?,?,?)", (firstname, user_id, chat_id))
    db.commit()


def del_db_admin(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM admin WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_adminall(chat_id: int):
    dbc.execute("DELETE FROM admin WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_admin(chat_id: int):
    dbc.execute("SELECT * FROM admin WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_special(firstname: str, user_id: int, chat_id: int):
    dbc.execute("INSERT INTO special(firstname,user_id,chat_id) VALUES(?,?,?)", (firstname, user_id, chat_id))
    db.commit()


def del_db_special(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM special WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_specialall(chat_id: int):
    dbc.execute("DELETE FROM special WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_special(chat_id: int):
    dbc.execute("SELECT * FROM special WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locktext(key: str, chat_id: int):
    dbc.execute("INSERT INTO locktext(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locktext(chat_id: int):
    dbc.execute("DELETE FROM locktext WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locktext(chat_id: int):
    dbc.execute("SELECT key FROM locktext WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def drop_db_locktext():
    dbc.execute("DROP TABLE locktext")
    dbc.execute("""CREATE TABLE IF NOT EXISTS locktext (key, chat_id)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_lockmnshn(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockmnshn(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockmnshn(chat_id: int):
    dbc.execute("DELETE FROM lockmnshn WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockmnshn(chat_id: int):
    dbc.execute("SELECT key FROM lockmnshn WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locklink(key: str, chat_id: int):
    dbc.execute("INSERT INTO locklink(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locklink(chat_id: int):
    dbc.execute("DELETE FROM locklink WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locklink(chat_id: int):
    dbc.execute("SELECT key FROM locklink WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_locklink_ban(key: str, chat_id: int):
    dbc.execute("INSERT INTO locklinkban(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locklink_ban(chat_id: int):
    dbc.execute("DELETE FROM locklinkban WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locklink_ban(chat_id: int):
    dbc.execute("SELECT key FROM locklinkban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_locklink_mute(key: str, chat_id: int):
    dbc.execute("INSERT INTO locklinkmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locklink_mute(chat_id: int):
    dbc.execute("DELETE FROM locklinkmute WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locklink_mute(chat_id: int):
    dbc.execute("SELECT key FROM locklinkmute WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockphoto(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockphoto(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockphoto(chat_id: int):
    dbc.execute("DELETE FROM lockphoto WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockphoto(chat_id: int):
    dbc.execute("SELECT key FROM lockphoto WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockvideo(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockvideo(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockvideo(chat_id: int):
    dbc.execute("DELETE FROM lockvideo WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockvideo(chat_id: int):
    dbc.execute("SELECT key FROM lockvideo WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locksticker(key: str, chat_id: int):
    dbc.execute("INSERT INTO locksticker(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locksticker(chat_id: int):
    dbc.execute("DELETE FROM locksticker WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locksticker(chat_id: int):
    dbc.execute("SELECT key FROM locksticker WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockanimation(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockanimation(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockanimation(chat_id: int):
    dbc.execute("DELETE FROM lockanimation WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockanimation(chat_id: int):
    dbc.execute("SELECT key FROM lockanimation WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockaudio(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockaudio(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockaudio(chat_id: int):
    dbc.execute("DELETE FROM lockaudio WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockaudio(chat_id: int):
    dbc.execute("SELECT key FROM lockaudio WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockvoice(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockvoice(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockvoice(chat_id: int):
    dbc.execute("DELETE FROM lockvoice WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockvoice(chat_id: int):
    dbc.execute("SELECT key FROM lockvoice WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockforward(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockforward(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockforward(chat_id: int):
    dbc.execute("DELETE FROM lockforward WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockforward(chat_id: int):
    dbc.execute("SELECT key FROM lockforward WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_lockforward_ban(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockforwardban(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockforward_ban(chat_id: int):
    dbc.execute("DELETE FROM lockforwardban WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockforward_ban(chat_id: int):
    dbc.execute("SELECT key FROM lockforwardban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_lockforward_mute(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockforwardmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockforward_mute(chat_id: int):
    dbc.execute("DELETE FROM lockforwardmute WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockforward_mute(chat_id: int):
    dbc.execute("SELECT key FROM lockforwardmute WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockdocument(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockdocument(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockdocument(chat_id: int):
    dbc.execute("DELETE FROM lockdocument WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockdocument(chat_id: int):
    dbc.execute("SELECT key FROM lockdocument WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockcontact(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockcontact(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockcontact(chat_id: int):
    dbc.execute("DELETE FROM lockcontact WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockcontact(chat_id: int):
    dbc.execute("SELECT key FROM lockcontact WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locksendmsg(key: str):
    dbc.execute("INSERT INTO locksendmsg(key) VALUES(?)", (key,))
    db.commit()


def del_db_locksendmsg():
    dbc.execute("DELETE FROM locksendmsg")
    db.commit()


def get_db_locksendmsg():
    dbc.execute("SELECT key FROM locksendmsg")
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockbroadcast(key: str):
    dbc.execute("INSERT INTO lockbroadcast(key) VALUES(?)", (key,))
    db.commit()


def del_db_lockbroadcast():
    dbc.execute("DELETE FROM lockbroadcast")
    db.commit()


def get_db_lockbroadcast():
    dbc.execute("SELECT key FROM lockbroadcast")
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockgenyoutube(key: str):
    dbc.execute("INSERT INTO lockgenyoutube(key) VALUES(?)", (key,))
    db.commit()


def del_db_lockgenyoutube():
    dbc.execute("DELETE FROM lockgenyoutube")
    db.commit()


def get_db_lockgenyoutube():
    dbc.execute("SELECT key FROM lockgenyoutube")
    ul = dbc.fetchall()
    return ul if ul else None

#######################################################################################################
#######################################################################################################

def set_db_lockgenmnshn(key: str):
    dbc.execute("INSERT INTO lockgenmnshn(key) VALUES(?)", (key,))
    db.commit()


def del_db_lockgenmnshn():
    dbc.execute("DELETE FROM lockgenmnshn")
    db.commit()


def get_db_lockgenmnshn() -> str:
    dbc.execute("SELECT key FROM lockgenmnshn")
    ul = dbc.fetchall()
    return ul if ul else None
    
#######################################################################################################
#######################################################################################################

def set_db_addlinkgroup(link: str, chat_id: int):
    dbc.execute("INSERT INTO addlinkgroup(link, chat_id) VALUES(?,?)", (link, chat_id))
    db.commit()


def del_db_addlinkgroup(chat_id: int):
    dbc.execute("DELETE FROM addlinkgroup WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_addlinkgroup(chat_id: int):
    dbc.execute("SELECT * FROM addlinkgroup WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockwelcome(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockwelcome(key, chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockwelcome(chat_id: int):
    dbc.execute("DELETE FROM lockwelcome WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockwelcome(chat_id: int):
    dbc.execute("SELECT * FROM lockwelcome WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_addwelcomegroup(welcome: str, chat_id: int):
    dbc.execute("INSERT INTO addwelcomegroup(welcome, chat_id) VALUES(?,?)", (welcome, chat_id))
    db.commit()


def del_db_addwelcomegroup(chat_id: int):
    dbc.execute("DELETE FROM addwelcomegroup WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_addwelcomegroup(chat_id: int):
    dbc.execute("SELECT * FROM addwelcomegroup WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockbye(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockbye(key, chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockbye(chat_id: int):
    dbc.execute("DELETE FROM lockbye WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockbye(chat_id: int):
    dbc.execute("SELECT * FROM lockbye WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_addbyegroup(bye: str, chat_id: int):
    dbc.execute("INSERT INTO addbyegroup(bye, chat_id) VALUES(?,?)", (bye, chat_id))
    db.commit()


def del_db_addbyegroup(chat_id: int):
    dbc.execute("DELETE FROM addbyegroup WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_addbyegroup(chat_id: int):
    dbc.execute("SELECT * FROM addbyegroup WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockreply(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockreply(key, chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockreply(chat_id: int):
    dbc.execute("DELETE FROM lockreply WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockreply(chat_id: int):
    dbc.execute("SELECT * FROM lockreply WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockfshar(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockfshar(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockfshar(chat_id: int):
    dbc.execute("DELETE FROM lockfshar WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockfshar(chat_id: int):
    dbc.execute("SELECT key FROM lockfshar WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_lockfshar_ban(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockfsharban(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockfshar_ban(chat_id: int):
    dbc.execute("DELETE FROM lockfsharban WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockfshar_ban(chat_id: int):
    dbc.execute("SELECT key FROM lockfsharban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_lockfshar_mute(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockfsharmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockfshar_mute(chat_id: int):
    dbc.execute("DELETE FROM lockfsharmute WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockfshar_mute(chat_id: int):
    dbc.execute("SELECT key FROM lockfsharmute WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locknotification(key: str, chat_id: int):
    dbc.execute("INSERT INTO locknotification(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locknotification(chat_id: int):
    dbc.execute("DELETE FROM locknotification WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locknotification(chat_id: int):
    dbc.execute("SELECT key FROM locknotification WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockzhrafa(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockzhrafa(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockzhrafa(chat_id: int):
    dbc.execute("DELETE FROM lockzhrafa WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockzhrafa(chat_id: int):
    dbc.execute("SELECT key FROM lockzhrafa WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockmusic(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockmusic(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockmusic(chat_id: int):
    dbc.execute("DELETE FROM lockmusic WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockmusic(chat_id: int):
    dbc.execute("SELECT key FROM lockmusic WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockaflam(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockaflam(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockaflam(chat_id: int):
    dbc.execute("DELETE FROM lockaflam WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockaflam(chat_id: int):
    dbc.execute("SELECT key FROM lockaflam WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockyoutube(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockyoutube(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockyoutube(chat_id: int):
    dbc.execute("DELETE FROM lockyoutube WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockyoutube(chat_id: int):
    dbc.execute("SELECT key FROM lockyoutube WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locktranslate(key: str, chat_id: int):
    dbc.execute("INSERT INTO locktranslate(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locktranslate(chat_id: int):
    dbc.execute("DELETE FROM locktranslate WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locktranslate(chat_id: int):
    dbc.execute("SELECT key FROM locktranslate WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_blocktext(key: str, chat_id: int):
    dbc.execute("INSERT INTO blocktext(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_blocktext(key: str, chat_id: int):
    dbc.execute("DELETE FROM blocktext WHERE key = ? and chat_id = ?", (key, chat_id))
    db.commit()


def del_db_blocktextall(chat_id: int):
    dbc.execute("DELETE FROM blocktext WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_blocktext(chat_id: int):
    dbc.execute("SELECT * FROM blocktext WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_blocktext_ban(key: str, chat_id: int):
    dbc.execute("INSERT INTO blocktextban(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_blocktext_ban(chat_id: int):
    dbc.execute("DELETE FROM blocktextban WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_blocktext_ban(chat_id: int):
    dbc.execute("SELECT * FROM blocktextban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def set_db_blocktext_mute(key: str, chat_id: int):
    dbc.execute("INSERT INTO blocktextmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_blocktext_mute(chat_id: int):
    dbc.execute("DELETE FROM blocktextmute WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_blocktext_mute(chat_id: int):
    dbc.execute("SELECT * FROM blocktextmute WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockupper(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockupper(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockupper(chat_id: int):
    dbc.execute("DELETE FROM lockupper WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockupper(chat_id: int):
    dbc.execute("SELECT key FROM lockupper WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lock(databasename, key: str, chat_id: int):
    dbc.execute("INSERT INTO " + databasename + " (key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lock(databasename, chat_id: int):
    dbc.execute("DELETE FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lock(databasename, chat_id: int):
    dbc.execute("SELECT key FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockrwayat(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockrwayat(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockrwayat(chat_id: int):
    dbc.execute("DELETE FROM lockrwayat WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockrwayat(chat_id: int):
    dbc.execute("SELECT key FROM lockrwayat WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_entertainment(databasename, firstname: str, user_id: int, chat_id: int):
    dbc.execute("INSERT INTO " + databasename + "(firstname,user_id,chat_id) VALUES(?,?,?)",
                       (firstname, user_id, chat_id))
    db.commit()


def del_db_entertainment(databasename, user_id: int, chat_id: int):
    dbc.execute("DELETE FROM " + databasename + " WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_entertainmentall(databasename, chat_id: int):
    dbc.execute("DELETE FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_entertainment(databasename, chat_id: int):
    dbc.execute("SELECT * FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockgames(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockgames(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockgames(chat_id: int):
    dbc.execute("DELETE FROM lockgames WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockgames(chat_id: int):
    dbc.execute("SELECT key FROM lockgames WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None

#######################################################################################################
#######################################################################################################

def set_db_locktag(key: str, chat_id: int):
    dbc.execute("INSERT INTO locktag(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_locktag(chat_id: int):
    dbc.execute("DELETE FROM locktag WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_locktag(chat_id: int):
    dbc.execute("SELECT key FROM locktag WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockmeendafny(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockmeendafny(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockmeendafny(chat_id: int):
    dbc.execute("DELETE FROM lockmeendafny WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockmeendafny(chat_id: int):
    dbc.execute("SELECT key FROM lockmeendafny WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_replygroup(text: str, reply: str, chat_id: int):
    dbc.execute("INSERT INTO replygroup (text,reply,chat_id) VALUES(?,?,?)", (text, reply, chat_id))
    db.commit()


def del_db_replygroup(text: str, chat_id: int):
    dbc.execute("DELETE FROM replygroup WHERE text = ? and chat_id = ?", (text, chat_id))
    db.commit()


def del_db_repgroupall(chat_id: int):
    dbc.execute("DELETE FROM replygroup WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_replygroup(chat_id: int):
    dbc.execute("SELECT * FROM replygroup WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


def drop_db_replygroup():
    dbc.execute("DROP TABLE replygroup")
    dbc.execute("""CREATE TABLE IF NOT EXISTS replygroup (text, reply, chat_id)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_deletelink(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockdeletelink(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_deletelink(chat_id: int):
    dbc.execute("DELETE FROM lockdeletelink WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_deletelink(chat_id: int):
    dbc.execute("SELECT key FROM lockdeletelink WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockkickme(key: str, chat_id: int):
    dbc.execute("INSERT INTO lockkickme(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockkickme(chat_id: int):
    dbc.execute("DELETE FROM lockkickme WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockkickme(chat_id: int):
    dbc.execute("SELECT key FROM lockkickme WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_ban(user_id: int, firstname: str, chat_id: int):
    dbc.execute("INSERT INTO ban(user_id,firstname,chat_id) VALUES(?,?,?)", (user_id, firstname, chat_id))
    db.commit()


def del_db_ban(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM ban WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_banall(chat_id: int):
    dbc.execute("DELETE FROM ban WHERE chat_id = ?", (chat_id,))
    db.commit()


def del_db_banallall():
    dbc.execute("DROP TABLE ban")
    dbc.execute("""CREATE TABLE IF NOT EXISTS ban (user_id,
                                                     firstname, chat_id INTEGER)""")
    db.commit()


def get_db_ban(chat_id: int):
    dbc.execute("SELECT * FROM ban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_mute(user_id: int, firstname: str, chat_id: int):
    dbc.execute("INSERT INTO mute(user_id,firstname,chat_id) VALUES(?,?,?)", (user_id, firstname, chat_id))
    db.commit()


def del_db_mute(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM mute WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def del_db_muteall(chat_id: int):
    dbc.execute("DELETE FROM mute WHERE chat_id = ?", (chat_id,))
    db.commit()


def del_db_muteallall():
    dbc.execute("DROP TABLE mute")
    dbc.execute("""CREATE TABLE IF NOT EXISTS mute (user_id,
                                                     firstname, chat_id INTEGER)""")
    db.commit()


def get_db_mute(chat_id: int):
    dbc.execute("SELECT * FROM mute WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_meendafny(user_id_add: int, firstname_add: str, user_id_added: int, chat_id: int):
    dbc.execute("INSERT INTO meendafny(user_id_add,firstname_add,user_id_added,chat_id) VALUES(?,?,?,?)",
                       (user_id_add, firstname_add, user_id_added, chat_id))
    db.commit()


def get_db_meendafny(user_id_added: int, chat_id: int):
    dbc.execute("SELECT * FROM meendafny WHERE user_id_added = ? and chat_id = ?", (user_id_added, chat_id))
    ul = dbc.fetchall()
    return ul if ul else None


def del_db_meendafnyallall():
    dbc.execute("DROP TABLE meendafny")
    dbc.execute("""CREATE TABLE IF NOT EXISTS meendafny (user_id_add INTEGER, firstname_add,
                                                     user_id_added INTEGER, chat_id INTEGER)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_mycontact(counter, user_id, chat_id):
    dbc.execute(
        "SELECT * FROM mycontact WHERE user_id = ? AND chat_id = ?", (user_id, chat_id)
    )
    if dbc.fetchone():
        dbc.execute(
            "UPDATE mycontact SET counter = counter + ? WHERE user_id = ? AND chat_id = ?",
            (counter, user_id, chat_id),
        )
        db.commit()
    else:
        dbc.execute(
            "INSERT INTO mycontact (counter, user_id, chat_id) VALUES (?,?,?)",
            (counter, user_id, chat_id),
        )
        db.commit()


def del_db_mycontact(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM mycontact WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def get_db_mycontact(user_id: int, chat_id: int):
    dbc.execute("SELECT counter FROM mycontact WHERE user_id = ? and chat_id = ?",
                       (user_id, chat_id))
    ul = dbc.fetchone()
    return ul[0] if ul else None


def del_db_mycontactallall():
    dbc.execute("DROP TABLE mycontact")
    dbc.execute("""CREATE TABLE IF NOT EXISTS mycontact (counter INTEGER, user_id, chat_id)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_mypointgame(counter, user_id, chat_id):
    dbc.execute(
        "SELECT * FROM mypointgame WHERE user_id = ? AND chat_id = ?", (user_id, chat_id)
    )
    if dbc.fetchone():
        dbc.execute(
            "UPDATE mypointgame SET counter = counter + ? WHERE user_id = ? AND chat_id = ?",
            (counter, user_id, chat_id),
        )
        db.commit()
    else:
        dbc.execute(
            "INSERT INTO mypointgame (counter, user_id, chat_id) VALUES (?,?,?)",
            (counter, user_id, chat_id),
        )
        db.commit()


def del_db_mypointgame(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM mypointgame WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def get_db_mypointgame(user_id: int, chat_id: int):
    dbc.execute("SELECT counter FROM mypointgame WHERE user_id = ? and chat_id = ?",
                       (user_id, chat_id))
    ul = dbc.fetchone()
    return ul[0] if ul else None


def del_db_mypointgameallall():
    dbc.execute("DROP TABLE mypointgame")
    dbc.execute("""CREATE TABLE IF NOT EXISTS mypointgame (counter INTEGER, user_id, chat_id)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_mymessage(counter, user_id, chat_id):
    dbc.execute(
        "SELECT * FROM mymessage WHERE user_id = ? AND chat_id = ?", (user_id, chat_id)
    )
    if dbc.fetchone():
        dbc.execute(
            "UPDATE mymessage SET counter = counter + ? WHERE user_id = ? AND chat_id = ?",
            (counter, user_id, chat_id),
        )
        db.commit()
    else:
        dbc.execute(
            "INSERT INTO mymessage (counter, user_id, chat_id) VALUES (?,?,?)",
            (counter, user_id, chat_id),
        )
        db.commit()


def del_db_mymessage(user_id: int, chat_id: int):
    dbc.execute("DELETE FROM mymessage WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    db.commit()


def get_db_mymessage(user_id: int, chat_id: int):
    dbc.execute("SELECT counter FROM mymessage WHERE user_id = ? and chat_id = ?",
                       (user_id, chat_id))
    ul = dbc.fetchone()
    return ul[0] if ul else None


def del_db_mymessageallall():
    dbc.execute("DROP TABLE mymessage")
    dbc.execute("""CREATE TABLE IF NOT EXISTS mymessage (counter INTEGER, user_id, chat_id)""")
    db.commit()


#######################################################################################################
#######################################################################################################

def set_db_addcommand(command: str, newcommand: str, chat_id: int):
    dbc.execute("INSERT INTO addcomand (command,newcommand,chat_id) VALUES(?,?,?)",
                       (command, newcommand, chat_id))
    db.commit()


def del_db_addcommand(text: str, chat_id: int):
    dbc.execute("DELETE FROM addcomand WHERE newcommand = ? and chat_id = ?", (text, chat_id))
    db.commit()


def del_db_addcommandall(chat_id: int):
    dbc.execute("DELETE FROM addcomand WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_addcommand(chat_id: int):
    dbc.execute("SELECT * FROM addcomand WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_addcustomid(customid: str, chat_id: int):
    dbc.execute("INSERT INTO addcustomid(customid, chat_id) VALUES(?,?)", (customid, chat_id))
    db.commit()


def del_db_addcustomid(chat_id: int):
    dbc.execute("DELETE FROM addcustomid WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_addcustomid(chat_id: int):
    dbc.execute("SELECT * FROM addcustomid WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockkickbotatban(key: str, chat_id: int):
    dbc.execute("INSERT INTO kickbotatban(key,chat_id) VALUES(?,?)", (key, chat_id))
    db.commit()


def del_db_lockkickbotatban(chat_id: int):
    dbc.execute("DELETE FROM kickbotatban WHERE chat_id = ?", (chat_id,))
    db.commit()


def get_db_lockkickbotatban(chat_id: int):
    dbc.execute("SELECT key FROM kickbotatban WHERE chat_id = ?", (chat_id,))
    ul = dbc.fetchall()
    return ul if ul else None

#######################################################################################################
#######################################################################################################
