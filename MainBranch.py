# Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os.path
import multiprocessing
import uuid
from PIL import Image
from os import path
import wget
import time
import urllib
import instaloader
from Hashtags import hs
from Captions import cap
import instascrape
import random

from Vars import usernames as us, passwords as ps, HostPages as Hp
# from Vars import ProfileXpath as ProfileXp
# from Vars import LogOXpath as LogOXp
from Vars import PagesToFollowFrom as PTFF
from Vars import PageTypes as PT


# pentru orice disperat se uita aici, nu nu am pus parolele direct aici
# si nu le am dat commit ,
# semnat,eugen din trecut

# Other imports here
import os
import wget
import shutil
from pathlib import Path


def AcceptCookies():

    try:
        not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()
    except:
        driver.refresh()
        time.sleep(1)
        try:not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()
        except:
            pass

def InstaLogin(Vusername, Vpassword):
    try:
        username = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        password.clear()

        username.send_keys(Vusername)
        password.send_keys(Vpassword)
    except:
        driver.refresh()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        username = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        password.clear()

        username.send_keys(Vusername)
        password.send_keys(Vpassword)

    time.sleep(3)

    try:
        log_in = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    except:
        time.sleep(3.5)
        log_in = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(1)
    try:
        not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Allow All Cookies")]'))).click()
    except:
        pass
    try:
        not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    except:
        driver.refresh()
        time.sleep(2)
        not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    time.sleep(1)
    try:
        not_now2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    except:
        pass

def SavePost(imgsrc,btc):
    path = os.getcwd()
    path = os.path.join(path, "Posts")
    #imgsrc="https://instagram.fotp3-3.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/240114031_4101049583354243_2549448833453338629_n.jpg?_nc_ht=instagram.fotp3-3.fna.fbcdn.net&_nc_cat=1&_nc_ohc=nRSo2BQV_vsAX-ylchr&edm=AABBvjUBAAAA&ccb=7-4&oh=24656707092404f39d0ed54498a7afe5&oe=61282080&_nc_sid=83d603"
    save_as = os.path.join(path, 'post'+str(btc)+ '.jpg')
    wget.download(imgsrc, save_as)



def GoToFirstPost(h):
    time.sleep(3)

    clickableimages = driver.find_elements_by_class_name('_9AhH0')

    clicknow = clickableimages[h]
    try:
        clicknow.click()
    except:
        searchbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        # search for the hashtag cat
        try:
            searchbox.send_keys(Keys.ENTER)
            time.sleep(1)
        except:
            pass
        try:
            searchbox.send_keys(Keys.ENTER)
            time.sleep(2)
        except:
            pass

        time.sleep(1)
        clickableimages = driver.find_elements_by_class_name('_9AhH0')
        clicknow = clickableimages[h]
        clicknow.click()

def LogOut():
    time.sleep(1)
    choices = driver.find_elements_by_xpath("//span[@class='_2dbep qNELH']")
    cautat = choices[0]
    prof = cautat.find_element_by_xpath('..')
    prof.click()
    time.sleep(0.5)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Log Out")]'))).click()


def GoToProfile():
    time.sleep(1)
    choices = driver.find_elements_by_xpath("//span[@class='_2dbep qNELH']")
    cautat = choices[0]
    prof = cautat.find_element_by_xpath('..')
    prof.click()
    time.sleep(0.5)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Profile")]'))).click()
    time.sleep(2)

def GoToFollowers():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "following")]'))).click()

def GetFollowers():
    elements = driver.find_elements_by_class_name('g47SY ')
    return elements[1].text

def GetFollowing():
    elements = driver.find_elements_by_class_name('g47SY ')
    return elements[2].text

def UpdateStats(f,i,j):
    elements = driver.find_elements_by_class_name('g47SY ')

    f.write(us[i][j]+ " Followers:" + elements[1].text + "  Following:" + elements[2].text)
    f.write("\n")


def GoToLikes():
    time.sleep(1)
    # vcOH2

    T = driver.find_elements_by_class_name('vcOH2')
    if len(T) != 0:
        x = driver.find_element_by_class_name("wpO6b  ")
        actions = ActionChains(driver)
        actions.click(x).perform()
        time.sleep(0.5)
        return 0
    T = driver.find_elements_by_class_name('fXIG0')
    if len(T) != 0:
        x = driver.find_element_by_class_name("wpO6b  ")
        actions = ActionChains(driver)
        actions.click(x).perform()
        time.sleep(0.5)
        return 0

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "zV_Nj"))).click()
    except:
        x = driver.find_element_by_class_name("wpO6b  ")
        actions = ActionChains(driver)
        actions.click(x).perform()
        time.sleep(0.5)
        return 0
    return 1

def FollowFromHost(number,batch,nr):
    Tp = PT[batch][nr]
    k = random.randint(0, len(PTFF[Tp]) - 1)
    SearchForPage(PTFF[Tp][k])
    ind = 0
    GoToFirstPost(ind)
    while GoToLikes() == 0:
        ind += 1
        GoToFirstPost(ind)

    Follow(number)

    x = driver.find_elements_by_class_name("WaOAr")
    actions = ActionChains(driver)
    actions.click(x[1]).perform()
    time.sleep(0.5)

    x = driver.find_element_by_class_name("wpO6b")
    actions = ActionChains(driver)
    actions.click(x).perform()
    time.sleep(0.5)


def ScrollTo(el):
    el.location_once_scrolled_into_view

def Unfollow(number):
    time.sleep(3)
    toFollow = driver.find_elements_by_class_name('L3NKy')
    GoodtoFollow = []

    #SCROLLING PHASE
    lastlength = 0
    for i in range(0, 7):
        toFollow = driver.find_elements_by_class_name('L3NKy')
        length = len(toFollow) - 1
        Fl = toFollow[length]
        ScrollTo(Fl)
        while (length == lastlength):
            time.sleep(1 + random.random())
            toFollow = driver.find_elements_by_class_name('L3NKy')
            length = len(toFollow) - 1
        lastlength = length
    toFollow = driver.find_elements_by_class_name('L3NKy')

    #TAKES ONLY THE USERS YOU ARE FOLLOWING
    for i in range(0, len(toFollow) - 1):
        Fl = toFollow[i]
        if (Fl.text == 'Following'):
            GoodtoFollow.append(Fl)

    #UNFOLLOWS
    for i in range(0, len(GoodtoFollow) - 1):
        Fl = GoodtoFollow[i]
        if number < 0:
            return
        ScrollTo(Fl)
        time.sleep(random.random() + 1.2)
        Fl.click()
        number -= 1
        time.sleep(random.random() + 1.2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Unfollow")]'))).click()
        time.sleep(random.random() + 2.2)
        ScrollTo(Fl)
        time.sleep(1.4 + random.random())


def Follow(number):
    time.sleep(3)
    toFollow = driver.find_elements_by_class_name('L3NKy')
    cnt = 0
    ta = int(len(toFollow) / 2 + 1)
    if ta > len(toFollow) - 1:
        return
    A = toFollow[ta]
    B = A
    while (number > 0):
        ta = int(len(toFollow) / 2 + 1)
        for i in range(ta, len(toFollow) - 1):
            Fl = toFollow[i]
            Fl.location_once_scrolled_into_view
            if number < 0:
                return
            if (Fl.text == 'Follow'):
                number -= 1
                ScrollTo(Fl)
                time.sleep(random.random() + 1.2)
                Fl.click()
                time.sleep(random.random() + 2)


            ScrollTo(Fl)
            time.sleep(1.4 + random.random())

        B = A
        toFollow = driver.find_elements_by_class_name('L3NKy')
        ta = int(len(toFollow) / 2 + 1)
        A = toFollow[ta]
        if A == B:
            return


def GetFirstPic(btc):
    time.sleep(1)

    ind = 0
    GoToFirstPost(ind)

    while GoToLikes() == 0:
        ind += 1
        GoToFirstPost(ind)

    x = '/ html / body / div[7] / div / div / div[1] / div / div[2]'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x))).click()
    x = '/html/body/div[6]/div[3]/button'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x))).click()
    time.sleep(1)

    images = driver.find_elements_by_class_name('FFVAD')
    imagessrc = [image.get_attribute('src') for image in images]
    imagessrc = imagessrc[:-2]
    SavePost(imagessrc[ind],btc)


def RandomizeCapt_Post(batch,nr):
    from Post_Protocol import Post
    global Post
    type = PT[batch][nr]
    k = random.randint(0, len(cap[type]) - 1)
    k1 = random.randint(0, len(hs[type]) - 1)
    Post(caption=cap[type][k], hashtags=hs[type][k1], batch = batch,nr = nr)


def PostFromHost(batch, nr):
    SearchForPage(Hp[batch][nr])
    GetFirstPic(batch)
    RandomizeCapt_Post(batch,nr)


def SearchForPage(page):
    # target the search input field
    try:
        searchbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        searchbox.clear()
    except:
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        searchbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        searchbox.clear()

    # _01UL2
    # search for the hashtag cat
    keyword = page
    searchbox.send_keys(keyword)
    time.sleep(1)
    Trash = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_01UL2")))
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        searchbox.send_keys(Keys.ENTER)
        time.sleep(1)
    except:
        pass

def TurnToNumber(str):
    number=0
    for i in str:
        print(i)
        if i>='0' and i<='9':
            number = number*10 + (int)(i)

    print("RETURNED NUMBER", number)
    return number


def LoginAndInit(i,j):

    AcceptCookies()
    InstaLogin(us[i][j], ps[i][j])


def SwitchOrNot():
    GoToProfile()
    if(TurnToNumber((GetFollowing()))>4000):
        return UnfollowProtocol
    else:
        return FollowFromHost



def FollowManagement(batchnumber,NumberOfUsers):
    for t in range(0, 10):
        at = time.localtime()
        current_time = time.strftime("%H:%M:%S", at)
        print(current_time, "TIME AT START ----------------------------------- ", t)
        driver.refresh()
        time.sleep(2)

        lng=len(us[batchnumber])
        for i in range(0, lng):
            LoginAndInit(batchnumber,i)
            ToCall = SwitchOrNot()
            time.sleep(3)
            ToCall(NumberOfUsers,batchnumber,i)
            LogOut()
            ToWait = random.random() + 3.5
            time.sleep(ToWait * 60)

            time.sleep(3)
        at = time.localtime()
        current_time = time.strftime("%H:%M:%S", at)
        print(current_time, "TIME BEFORE PAUSE ----------------------------------- ")
        ToWait = random.random() + 0.1 + random.randint(35, 40)
        time.sleep(ToWait * 60)

def UnfollowProtocol(number,batchnumber,i):
    print("apelat")
    elements = driver.find_elements_by_class_name('g47SY ')
    elements[2].click()
    print(number)
    Unfollow(number)
    x = driver.find_elements_by_class_name("WaOAr")
    actions = ActionChains(driver)
    actions.click(x[1]).perform()
    time.sleep(0.5)


def GetFirst():
    return first


def PostProtocolFull(batchnumber):

    length= len(us[batchnumber])
    for i in range(0, length):

        LoginAndInit(batchnumber,i)
        time.sleep(2)
        PostFromHost(batchnumber,i)
        LogOut()
        time.sleep(3)


def UpdateData(batchnumber):
    f = open("Stats"+str(batchnumber)+".txt", "w")
    length= len(us[batchnumber])

    for i in range(0, length):

        if i > 0:
            global first
            first = 1
        LoginAndInit(batchnumber,i)
        time.sleep(2)
        GoToProfile()
        UpdateStats(f,batchnumber,i)
        time.sleep(1)
        LogOut()


        time.sleep(3)
    f.close()


# first = 0
# pageNr = 0
#
# Pageln = len(us) - pageNr


def MasterChoice(inpt,batchnumber,NumberOfUsers=15):
    #exit()
    global driver
    driver = webdriver.Chrome('E:/chromedriver/chromedriver.exe')
    driver.get("https://www.instagram.com/")
    if inpt == 1:
        PostProtocolFull(batchnumber)
    elif inpt == 2:
        FollowManagement(batchnumber,NumberOfUsers)
    elif inpt == 3:
        UpdateData(batchnumber)






###########################################################################################################################################

import json
import codecs
import datetime
import os.path
import logging
from instabot import Bot
import argparse

from instagram_private_api import (
    Client, ClientError, ClientLoginError,
    ClientCookieExpiredError, ClientLoginRequiredError,
    __version__ as client_version)

def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings

    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json)
        print('SAVED: {0!s}'.format(new_settings_file))


def BatchAdmin(operation,batch):
    inoperation=operation
    length = len(us[batch])
    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.WARNING)
    device_id = None
    print(operation, batch, " pppppppppppppppaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    for w in range(0,10):
        at = time.localtime()
        current_time = time.strftime("%H:%M:%S", at)
        print(current_time, " start ----------------------------------- ")
        for i in range(0,length):

            username = us[batch][i]
            password = ps[batch][i]
            typ = PT[batch][i]
            print(username)
            time.sleep(2.5+random.random())
            try:
                settings_file = "cookies/settcookie_"+username
                if not os.path.isfile(settings_file):
                    # settings file does not exist
                    print('Unable to find file: {0!s}'.format(settings_file))

                    # login new

                    api = Client(

                        username, password,
                        on_login=lambda x: onlogin_callback(x, settings_file))
                else:
                    with open(settings_file) as file_data:
                        cached_settings = json.load(file_data, object_hook=from_json)
                    print('Reusing settings: {0!s}'.format(settings_file))

                    device_id = cached_settings.get('device_id')
                    # reuse auth settings
                    api = Client(
                        username, password,
                        settings=cached_settings)

            except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
                print('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))
            except ClientLoginError as e:
                print('ClientLoginError {0!s}'.format(e))
                exit(9)
            except ClientError as e:
                print('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response))
                exit(9)
            except Exception as e:
                print('Unexpected Exception: {0!s}'.format(e))
                exit(99)

            # Show when login expires
            cookie_expiry = api.cookie_jar.auth_expires
            print('Cookie Expiry: {0!s}'.format(datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')))

            # Call the api ------------------------------------------

            try:
                UsernameData = api.username_info(username)
            except:
                continue
            userID = UsernameData["user"]["pk"]
            tk = uuid.uuid4()
            Following = api.user_following(userID, rank_token=str(tk))
            lnFollowing = len(Following["users"])

            operation=inoperation

            if lnFollowing > 4000 and operation==2:
                # If you have more than 4k following I will unfollow instead of following
                operation=4

            todeletcookie = 0
            if operation == 1:
                #POSTING ATTEMPT DOES NOT WORK
                p = api.username_feed(Hp[batch][i])
                id = p['items'][0]['id']
                code = p['items'][0]['code']
                k=api.medias_info(id)
                src = "https://www.instagram.com/p/"+ code +"/media/?size=l"
                # #K = instascrape.Profile('theaventadorlover')
                # #K.scrape(session=api.session_id)
                # recent = K.get_recent_posts()
                # for post in recent:
                #     fname = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
                #     post.download(f"{fname}.png")
                # req = urllib.request.Request(
                #     src,
                #     data=None,
                #     headers={
                #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                #     }
                # )
                # f = urllib.request.urlopen(req)
                # data=f.read()

                with open("post1.jpg", "rb") as image:
                    f = image.read()
                    b = bytearray(f)

                api.post_photo(photo_data=b,size=(500,500))

                # urllib.request.urlretrieve(src, "00000001.jpg")

            elif operation == 2:
                #FOLLOWING USERS FROM THE POOL OF ACCOUNTS

                lng = len(PTFF[typ])
                k = random.randint(0,lng-1)
                p = api.username_feed(PTFF[typ][k])
                idsList = []
                for o in range (0, len( p['items'])):
                    id = p['items'][o]['id']
                    media_likers = api.media_likers(id)
                    lens = len(media_likers['users'])
                    for k in range(0,lens):
                        idsList.append(str(media_likers['users'][k]['pk']))

                lenusers = len(idsList)
                isFollowed = api.friendships_show_many(idsList)

                ToFollow = 30
                for i in range(0,lenusers):
                    if i == lenusers:
                        print("NU A MAI GASIT ____________________________!!!!!!!!!!!!!!!!!!")
                    isf = isFollowed["friendship_statuses"][idsList[i]]['following']
                    isp = isFollowed["friendship_statuses"][idsList[i]]['is_private']
                    ot = isFollowed["friendship_statuses"][idsList[i]]['outgoing_request']
                    if isf == False & isp == True & ot == False:
                        try:
                            api.friendships_create(idsList[i])
                        except:
                            todeletcookie = 1


                        ToFollow-=1
                        time.sleep(1.5+random.random())
                    if ToFollow<=0:
                        break

            elif operation == 3:
                pass
                #UPDATE STATS NOT IMPLEMENTED YET WORKS WITH SELENIUM
            elif operation == 4:
                # UNFOLLOWING PROCEDURE

                UsernameData = api.username_info(username)
                userID = UsernameData["user"]["pk"]

                ud=uuid.uuid4()
                ud=str(ud)

                Following = api.user_following(userID, rank_token=ud)
                lnFollowing = len(Following["users"])
                toUnfollow = 30

                for i in range(0, lnFollowing):
                    id = Following["users"][i]["pk"]
                    api.friendships_destroy(user_id=id)
                    toUnfollow -= 1
                    if toUnfollow <= 0:
                        break
                    time.sleep(1.5+random.random())
            else:
                #TESTING AREA !!!!!!!!!!!!!!!!

                UsernameData = api.username_info(username)
                userID = UsernameData["user"]["pk"]

                ud = uuid.uuid4()
                ud = str(ud)
                print(ud, username)
                print(userID, username)
                Following = api.user_following(userID, rank_token=ud)
                lnFollowing = len(Following["users"])
                toUnfollow = 3

                for i in range(0, lnFollowing):
                    id = Following["users"][i]["pk"]
                    api.friendships_destroy(user_id=id)
                    toUnfollow -= 1
                    if toUnfollow <= 0:
                        break
                    time.sleep(1.5 + random.random())
        at = time.localtime()
        current_time = time.strftime("%H:%M:%S", at)
        print(current_time, " end ----------------------------------- ")


        time.sleep(random.randint(35,40)*60)


if __name__ == '__main__':
    print("1 - post protocol \n2 - follow management protocol \n3 - update Stats protocol")
    print("introduce op type")

    operation = input()
    operation=int(operation)
    NumberofUsers=0
    if operation == 2:
        print("Please introduce number of users")
        NumberofUsers = input()
        NumberofUsers = TurnToNumber(NumberofUsers)


    batchnr = len(us)
    #batchnr=1
    #setting batchnr to 1 is used for work with one account at a time


    #MasterChoice -> Selenium implementation , but ban chance is much higher
    #BatchAdmin -> Api implementation , not as effective but it does not get your account banned


    dirp = os.path.abspath('config')
    if os.path.exists(dirp):
        shutil.rmtree(dirp)

    func = BatchAdmin
    if operation == 1:
        func = MasterChoice
    elif operation==2:
        func = MasterChoice
    elif operation==3:
        func = MasterChoice
    else:
        func = BatchAdmin
    p=[]
    for i in range(0,batchnr):
        if operation == 1:
            p.append(multiprocessing.Process(target=func, args=(operation, i, NumberofUsers)))
        else:
            p.append(multiprocessing.Process(target=func, args=(operation, i, NumberofUsers)))
    #exit()
    for i in range(0,batchnr):
        p[i].start()
    for i in range(0,batchnr):
        p[i].join()

