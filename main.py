from chapter4 import *
from chapter5 import *
from chapter6 import *
from chapter7 import *
from chapter8 import *
from chapter9 import *
from chapter10 import *
# from chapter11 import *
from chapter12 import *
from chapter13 import *
from chapter14 import *
from chapter15 import *
from chapter16 import *
from chapter17 import *
from chapter18 import *
from chapter19 import *
from chapter20 import *
import json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

list_methods = ListMethods()
# list_methods.append_to_list()

################################
# Dictionary
# person = create_person_dict()
# contact = create_contact_dict()
# pretty_print_dict(contact)

################################
string_methods = StringMethods('Hello, world')
# string_methods.start_end_check('hi','world')
# string_methods.strip_text()


################################
text = "My phone number is 0999-323-333 and 334-533-3432. Contact me at example@example.com."
# find_phone_number_groups(text)
# match_hero("Batman and Superman are in the movie.")
# match_batman_zero_or_more('The Adventures of Batwowowoman')
# check_start_end('Hello, world!')
# match_wildcard('The cat in the hat sat on the flat mat.')
# case_insensitive_search('RoboCop is a robot')
# extract_contact_info(text)


##################################
# choose_drink()



##################################
# get_path_info('noone.txt')
# copy_file('test.txt','noone.txt')
# move_file('noone.txt','./test_modules/noone.txt')

##################################
# copy_file('noone.txt','noone2.txt')
# move_file_or_folder('noone.txt','test_module/noone3.txt')
# copy_folder('test_folder','test1_folder')
# delete_directory_and_contents('test1_folder')
# create_zip('test_zip1.zip',['test.txt','sample.xlsx'])
# add_to_zip('test_zip.zip',['token-drive.pickle'])
# extract_zip('a.zip','')
# list_zip_contents('a.zip')

################################
url = 'https://automatetheboringstuff.com'
img_url = 'https://automatetheboringstuff.com/images/cover_automate2_thumb.jpg'
# content = download_web_page(url)
# soup = parse_html(content)
# display_page_preview(content)
# parse_html(content)
# element = find_elements_by_class(soup,'a')
# get_element_text(element,2)
# get_link_attributes(soup)
# download_image(img_url, 'test_image.jpg')
# print(get_all_links(url))
# download_all_images(url)

################################
# driver_path = 'D:\\RPA_Pratice\\msedgedriver.exe'
# driver = set_up_driver(driver_path)
# open_web_page(driver,url)


################################
# wb = open_excel_file('sample.xlsx')
# sheet = get_sheet(wb,'Sheet')
# get_cell_value(sheet,'C2')
# get_cell_by_position(sheet, 1, 2)
# create_and_save_excel('test.xlsx')
# set_cell_font(sheet,'A1', bold=True, italic=True)
# add_and_remove_sheet(wb, 'Test', 'Sheet3')
# read_sheet_to_list(sheet)

##################################
# pdf = open_pdf('Test.pdf')
# extract_all_text(pdf)

################################
# sheet = connect_to_google_sheet('1pkRVPwJtsTzS5MLXrJtIR6G2tzT-KTM-uEgOztqXD5k')
# list_all_sheets()
# read_gsheet_data(sheet)

################################
# create_word_doc('test.docx')
# add_text_to_word('test.docx','no one can create a word')
# read_word_doc('test.docx')

################################
headers = ['Name', 'Age', 'City']
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
# read_csv('test.csv')
# write_csv('test.csv', [['Name', 'Age', 'City'], ['Alice', 30, 'New York'], ['Bob', 25, 'Los Angeles']])
# write_csv_as_dict('test.csv', headers, data)
# read_json('test.json')
# write_json('test.json', {'Name': 'Eve', 'Age': 29, 'City': 'San Francisco'})
# update_json('test.json', 'Age', 222)

##################################
# get_current_time()
# datetime_operations()
# countdown_timer(13)
# current_time = datetime.datetime.now()
# one_minute_later = (current_time + datetime.timedelta(minutes=1)).strftime("%H:%M")
# print(f"Setting alarm for 1 minute later: {one_minute_later}")
# alarm_clock(one_minute_later)

################################################################
sender_email = config["email"]["sender_email"]
sender_password = config["email"]["sender_password"]
recipient_email = config["email"]["recipient_email"]
recipient_name = ""
subject_email = 'Test Subject'
message_text = """ Hello from

This is a test email using Python's smtplib library.

Best regards,
"""
# send_email(sender_email, sender_password, recipient_email,subject_email,message_text)
# check_inbox(sender_email,sender_password)

################################################################
# open_and_view_image('test.jpg')
# create_new_image()
img_path = 'test.jpg'
# image_processor = ImageProcessor(img_path)
# image_processor.rotate_image()

# draw_image = ImageDrawer(img_path)
# draw_image.draw_rectangle()

# add_watermark(img_path, 'Test Watermark')

################################
# show_prompt()