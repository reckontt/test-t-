from selenium import webdriver
dr=webdriver.Chrome()
dr.get('http://www.baidu.com')
#添加百度登录的cookie
dr.add_cookie({'name':'BDUSS','value':'Fva1NhbVc1dUF0TDRmQmdXOUkxNzdBQktuZE5scVVBS1IzT3VMfm9YS0FsbTVjQVFBQUFBJCQAAAAAAAAAAAEAAAB-jVkjyOe46MqrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAJR1yACUdcaj'})
#刷新网页
test
r.refresh()
