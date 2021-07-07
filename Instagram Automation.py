from instabot import Bot
import os
import glob
import shutil
import warnings
warnings.filterwarnings("ignore")

def Delete_unwanted_files():

    # DELETE UNWANTED FILES
    try:
        path = os.getcwd()

        newPath = path.replace(os.sep, '/')
        newpath = newPath + "/" + "config"

        shutil.rmtree(newpath)

        # This is alternative method to delete unwanted directory files
        '''
        path = os. getcwd()

        newPath = path.replace(os.sep, '/')
        newpath = newPath + "/" + "config" + "/" + "*"

        print(newpath)

        files = glob.glob(newpath)

        for f in files:

            print(f)
            os.remove(f)

        print("done")

        '''
    except:
        print("nope")



    '''
    myfile="C:/Users/SADARUWAN/PycharmProjects/python_Practice/config/2n_picgraphy_uuid_and_cookie.json"

    ## If file exists, delete it ##
    if os.path.isfile(myfile):

        os.remove(myfile)
        #print('Unwanted Files Handaled')

    else:
        pass
'''
class config:

    def config_set(self,us_n,pw):

        global bot

        bot = Bot()
        bot.login(username=us_n, password=pw)

        print(f'{us_n} Logged In Successfuly')


# '2n_picgraphy'
# 'Thowageballek'


set_config = config()


class instabot:

    def followers(self):

        followers = bot.get_user_followers('2n_picgraphy')

        global len_followers, names_folowers
        len_followers = len(followers)

        names_folowers = []
        for i in range(0,len(followers)):
            x = bot.get_user_info(followers[i])
            names_folowers.append(x['username'])

        #print(names_folowers)

    def following(self):

        following = bot.get_user_following('2n_picgraphy')

        global len_following, names_folowing
        len_following = len(following)

        names_folowing = []
        for i in range(0, len(following)):
            x2 = bot.get_user_info(following[i])
            names_folowing.append(x2['username'])

        #print(names_folowing)

main = instabot()


class automate_insta:

    def details_summary(self):

        print(bot.get_user_info('2n_picgraphy'))

        print('-----------------------------------------------')

        print("Your Followers : ", len_followers)

        print('-----------------------------------------------')

        print("Your Followings :", len_following)

    def adavance_summary(self):

        print(" ")
        print('-----------Followers That Are Not Following you-----------')
        print(" ")

        suspecious_followers = []

        for i in names_folowing :
            if i in names_folowers:
                continue
            else:
                suspecious_followers.append(i)

        print('Suspecious Followrs Count : ', len(suspecious_followers))

        for i in suspecious_followers:
            print(i)

        print(" ")
        print('-----------Followings That You Are Not Follows-----------')
        print(" ")

        Poor_followings = []

        for i in names_folowers:
            if i in names_folowing:
                continue
            else:
                Poor_followings.append(i)

        print('Followings That You Are Not Follows : ', len(Poor_followings))

        for i in Poor_followings:
            print(i)

insta_auto = automate_insta()


'''
ista_auto.details_summary()
ista_auto.adavance_summary()
'''
def app():

    print("WELCOME TO INSTRAGRAM BOT\n----------------------")

    while True:

        Delete_unwanted_files()
        try:

            username = input("Enter User Name : ")
            password = input("Enter Password  : ")

            set_config.config_set(username,password)

            main.following()
            main.followers()

            break

        except:
            print("Ops ! Eror Ocured Try Again")
            continue

    while True:

        print("-------------------\nMAIN MENU\n-------------------\n"
              "1 ----- Summary Of Account\n"
              "2 ----- Deep Infomations\n"
              "3 ----- Exit")


        print("-------------------------------------------")
        option = input("Select Option : ")
        print("-------------------------------------------")

        if option == "1":
            insta_auto.details_summary()

        elif option == "2":
            insta_auto.adavance_summary()

        elif option == "3":
            bot.logout(username=username,password=password)
            print("Account Logout Succussfuly | Thank Your !")
            break

        else:
            continue





app()



