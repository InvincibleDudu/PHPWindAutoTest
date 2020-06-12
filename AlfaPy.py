# def sum(a,b,c):
#     return a+b+c
#
#
# print(sum('a','asd',"23"))
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from get_csv import get_csv
from log import save_log


def post_once(bs, post):
    sleep(2)
    bs.find_element_by_link_text("登录").click()
    name = bs.find_element_by_name("pwuser")
    pswd = bs.find_element_by_name("pwpwd")
    submit = bs.find_element_by_name("submit")

    name.clear()
    name.send_keys("杜佳晨")
    pswd.clear()
    pswd.send_keys("djc123")
    submit.click()
    sleep(2)

    section = bs.find_element_by_xpath('//*[@id="fn_2"]')
    section.click()
    create = bs.find_element_by_xpath('//*[@id="td_post"]')
    ActionChains(bs).move_to_element(create).perform()
    post_btn = bs.find_element_by_xpath("//*[@id='pw_box']/div/a")
    post_btn.click()
    title = bs.find_element_by_xpath('//*[@id="atc_title"]')
    body = bs.find_element_by_xpath('//*[@id="textarea"]')

    title.clear()
    title.send_keys(post["title"])
    body.clear()
    body.send_keys(post["body"])
    submit_post = bs.find_element_by_xpath('//*[@id="main"]/form[1]/div/table[2]/tbody/tr[4]/td[1]/div/input[1]')
    submit_post.click()

    try:
        error = bs.find_element_by_xpath('//*[@id="box_container"]/div/div[2]/p')
        print(error.text)
        msg = "%s/%s: Error： %s" % (post['title'], post['body'], error.text)
    except:
        print("Post Success")
        msg = "%s/%s: Success： %s" % (post['title'], post['body'], "Post Success")

    sleep(2)
    bs.find_element_by_xpath('//*[@id="nav-user"]/table/tbody/tr/td[4]/a[3]').click()
    sleep(2)
    bs.find_element_by_xpath('//*[@id="nav-global"]/li[1]/a').click()
    sleep(2)

    return msg


def login():
    bs = webdriver.Chrome()
    bs.maximize_window()
    bs.get("http://localhost/phpwind/")
    results = []
    posts = get_csv('posts.csv')
    for post in posts:
        msg = post_once(bs, post)
        results.append(msg)

    save_log(results)
    sleep(22)


if __name__ == "__main__":
    login()
