from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
import sys
ur1=[]
ur2=[]
c=0
fi = open("log.txt","w")
fi.close()
fi=open("log.txt","a")
def func(siteurl):
	global ur1
	global ur2
	global c
	t="Page"+str(c)+".json"
	f2 = open(t,"a")
	c=c+1
	chrome_options = Options()
	WINDOW_SIZE = "1400,800"
	chrome_options.add_argument("start-maximised")
	chrome_options.add_argument("disable-infobars")
	chrome_options.add_argument("disable-extensions")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
	d = DesiredCapabilities.CHROME
	d['loggingPrefs'] = { 'browser':'ALL' }
	driver=webdriver.Chrome(desired_capabilities=d,chrome_options=chrome_options)
	driver.get(siteurl)
	
	for entry in driver.get_log('browser'):
		fi.write(str(entry))
		fi.write('\n')
	ele=driver.find_elements_by_css_selector("a")
	el=[]
	ur=[]
	for i in ele:
		for j in i.text:
			if j[0]>='A' and j[0]<='Z':
				el.append(i.text)
	el=list(set(el))
	
	f2.write("{\"Pages\":[")
	for i in el:
		try:
			t=driver.find_element_by_link_text(i)
			t.click()
			time.sleep(10)
			ur.append(driver.current_url)
			f2.write("{\"page\":\"")
			f2.write(driver.current_url)
			f2.write("\",\"Content\":\"")
			#print(driver.current_url)
			cont = driver.find_elements_by_css_selector('p')
			for i in cont:
				f2.write(i.text)
			driver.back()
			time.sleep(5)
			f2.write("\"},")
		except:
			continue
	f2.write("]}")
	ur1=ur1+ur
	ur2.append(siteurl)
	#print(ur1)
	ur1=list(set(ur1)-set(ur2))
	print(ur1)
	f2.close()
	for i in ur1:
		func(i)
	#print(ur1)
func(sys.argv[1])
#print(sys.argv[1])
fi.close()














