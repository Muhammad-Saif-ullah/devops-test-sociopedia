from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

HOST = "http://localhost"
PORT = 3000
URL = f"{HOST}:{PORT}"
NEW_ACCOUNT_DATA = {
    "first_name": "M",
    "last_name": "Tallal",
    "location": "Islamabad",
    "occupation": "Software Engineer",
    "email": "tallal@gmail.com",
    "password": "123456"
}
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Test 1: Register
def test_register():
    driver.get(URL)
    sign_up_link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/form/div[2]/p')
    sign_up_link.click()
    sleep(5)
    first_name = driver.find_element(By.NAME, "firstName")
    first_name.send_keys(NEW_ACCOUNT_DATA["first_name"])
    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys(NEW_ACCOUNT_DATA["last_name"])
    location = driver.find_element(By.NAME, "location")
    location.send_keys(NEW_ACCOUNT_DATA["location"])
    occupation = driver.find_element(By.NAME, "occupation")
    occupation.send_keys(NEW_ACCOUNT_DATA["occupation"])
    email = driver.find_element(By.NAME, "email")
    email.send_keys(NEW_ACCOUNT_DATA["email"])
    password = driver.find_element(By.NAME, "password")
    password.send_keys(NEW_ACCOUNT_DATA["password"])

    register_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/form/div[2]/button')
    register_button.click()
    sleep(5)

    try:
        input_el = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/input')

        if input_el.get_attribute("placeholder") == "What's on your mind...":
            print("✅ Test (Register Account) Passed")
        else:
            Exception()
    except:
        print("❌ Test (Register Account) Failed")


# Test 2: Login
def test_login(actual_login_test: bool):
    driver.get(URL)
    email = driver.find_element(By.NAME, "email")
    email.send_keys(NEW_ACCOUNT_DATA["email"])
    password = driver.find_element(By.NAME, "password")
    password.send_keys(NEW_ACCOUNT_DATA["password"])
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/form/div[2]/button')
    login_button.click()
    sleep(5)

    try:
        input_el = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/input')

        if input_el.get_attribute("placeholder") == "What's on your mind..." and actual_login_test:
            print("✅ Test (Login) Passed")
        else:
            Exception()
    except:
        if not actual_login_test:
            print("⭕ Login failed. Invalid credentials")
        else:
            print("❌ Test (Login) Failed")


# Test 3: Logout
def test_logout():
    test_login(actual_login_test=False)
    sleep(3)
    options_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div')
    options_button.click()
    sleep(3)
    log_out = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
    log_out.click()

    try:
        input_el = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/h5')

        if input_el.text == "Welcome to Socipedia, the Social Media for Sociopaths!":
            print("✅ Test (Logout) Passed")
        else:
            Exception()
    except:
        print("❌ Test (Logout) Failed")


# Test 4: Create Post
def test_create_post(actual_create_post_test: bool):
    test_login(actual_login_test=False)
    sleep(3)
    post_text_el = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="What\'s on your mind..."]')
    random_number_str = str(random.randint(100000, 999999))
    post_text_el.send_keys("This is an automated test post " + random_number_str)
    post_button = driver.find_element(By.CLASS_NAME, 'new-post-button')
    post_button.click()
    sleep(5)
    
    try:
        all_posts = driver.find_elements(By.CLASS_NAME, 'single-post')
        for post in all_posts:
            post_text = post.find_element(By.CLASS_NAME, 'post-description').text
            if post_text == "This is an automated test post " + random_number_str and actual_create_post_test:
                print("✅ Test (Create Post) Passed")
                return random_number_str
            elif post_text == "This is an automated test post " + random_number_str:
                return random_number_str
    except:
        if not actual_create_post_test:
            print("⭕ Create Post failed.")
        else:
            print("❌ Test (Create Post) Failed")


# Test 5: Like Post
def test_like_post():
    test_login(actual_login_test=False)
    sleep(3)
    like_button = driver.find_elements(By.CLASS_NAME, 'like-button')[0]
    current_likes = like_button.find_element(By.XPATH, './following-sibling::p').text
    like_button.click()
    sleep(2)
    new_likes = like_button.find_element(By.XPATH, './following-sibling::p').text

    if int(new_likes) == int(current_likes) + 1:
        print("✅ Test (Like Post) Passed")
    else:
        print("❌ Test (Like Post) Failed")


# Test 6: Unlike Post
def test_unlike_post():
    test_login(actual_login_test=False)
    sleep(3)
    like_button = driver.find_elements(By.CLASS_NAME, 'like-button')[0]
    current_likes = like_button.find_element(By.XPATH, './following-sibling::p').text
    like_button.click()
    sleep(2)
    new_likes = like_button.find_element(By.XPATH, './following-sibling::p').text

    if int(new_likes) == int(current_likes) - 1:
        print("✅ Test (Unlike Post) Passed")
    else:
        print("❌ Test (Unlike Post) Failed")


# Test 7: Comment on Post
def test_comment_on_post():
    test_login(actual_login_test=False)
    sleep(3)
    single_post = driver.find_elements(By.CLASS_NAME, 'single-post')[0]
    comment_svg = single_post.find_element(By.CSS_SELECTOR, 'svg[data-testid="ChatBubbleOutlineOutlinedIcon"]')
    comment_svg.click()
    new_comment = single_post.find_element(By.CSS_SELECTOR, 'input[placeholder="Add a comment..."]')
    random_number = str(random.randint(100000, 999999))
    new_comment.send_keys("This is an automated test comment " + random_number)
    sleep(1)
    add_comment_button = single_post.find_element(By.CLASS_NAME, 'add-comment-button')
    add_comment_button.click()

    sleep(2)
    div_all_comments = single_post.find_element(By.CLASS_NAME, 'all-post-comments')
    all_comments = div_all_comments.find_elements(By.TAG_NAME, 'p')
    for comment in all_comments:
        # print("🔵", comment.text)
        comment_text = comment.text.split('-')[0].strip()
        if comment_text == "This is an automated test comment " + random_number:
            print("✅ Test (Comment on Post) Passed")
            return
        
    print("❌ Test (Comment on Post) Failed")
    

# Test 8: Delete Own Post
def test_delete_post():
    post_number = test_create_post(actual_create_post_test=False)
    # print("🔵", post_number)
    sleep(3)
    all_posts = driver.find_elements(By.CLASS_NAME, 'single-post')
    for post in all_posts:
        post_text = post.find_element(By.CLASS_NAME, 'post-description').text
        # print("🔵", post_text)
        if post_text == "This is an automated test post " + post_number:
            delete_button = post.find_element(By.CSS_SELECTOR, 'svg[data-testid="ClearOutlinedIcon"]')
            delete_button.click()
            alert = driver.switch_to.alert
            alert.accept()
            sleep(2)
            driver.switch_to.default_content()
            new_all_posts = driver.find_elements(By.CLASS_NAME, 'single-post')
            for post in new_all_posts:
                post_text = post.find_element(By.CLASS_NAME, 'post-description').text
                if post_text == "This is an automated test post " + post_number:
                    print("❌ Test (Delete Post) Failed")
                    return
            print("✅ Test (Delete Post) Passed")
            return

    print("❌ Test (Delete Post) Failed")
    

# Test 9: Add Friend
def test_add_friend():
    driver.get(URL)
    test_login(actual_login_test=False)
    sleep(3)

    all_posts = driver.find_elements(By.CLASS_NAME, 'single-post')
    selected_post = None
    for post in all_posts:
        try:
            post.find_element(By.CSS_SELECTOR, 'svg[data-testid="PersonAddOutlinedIcon"]')
            selected_post = post
            break
        except:
            continue

    if not selected_post:
        print("⭕ All users are already friends. Skipping test...")
        return

    # data-testid="PersonAddOutlinedIcon"
    add_friend_button = selected_post.find_element(By.CSS_SELECTOR, 'svg[data-testid="PersonAddOutlinedIcon"]')
    if add_friend_button:
        new_friend_name = selected_post.find_element(By.CLASS_NAME, 'single-name-friend').text
        # print("🔵", new_friend_name)
        add_friend_button.click()
        sleep(2)
        friends_list = driver.find_element(By.CLASS_NAME, 'friends-list')
        current_friends = friends_list.find_elements(By.CLASS_NAME, 'single-name-friend')
        for friend in current_friends:
            if friend.text == new_friend_name:
                print("✅ Test (Add Friend) Passed")
                return

    print("❌ Test (Add Friend) Failed")


# Test 10: Remove Friend
def test_remove_friend():
    driver.get(URL)
    test_login(actual_login_test=False)
    sleep(3)

    friends_list = driver.find_element(By.CLASS_NAME, 'friends-list')
    current_friend_names = friends_list.find_elements(By.CLASS_NAME, 'single-name-friend')
    if len(current_friend_names) == 0:
        print("⭕ No friends to remove. Skipping test...")
        return

    all_friends = friends_list.find_elements(By.CLASS_NAME, 'each-friend')
    check_friend = all_friends[0]
    current_friend_name = check_friend.find_element(By.CLASS_NAME, 'single-name-friend').text
    # print("🔵", check_friend.get_attribute("outerHTML"))

    remove_friend_button = check_friend.find_element(By.CSS_SELECTOR, 'svg[data-testid="PersonRemoveOutlinedIcon"]')
    remove_friend_button.click()
    sleep(2)

    new_friends_list = driver.find_element(By.CLASS_NAME, 'friends-list')
    new_friend_names = new_friends_list.find_elements(By.CLASS_NAME, 'single-name-friend')
    
    for name in new_friend_names:
        if name.text == current_friend_name:
            print("❌ Test (Remove Friend) Failed")
            return

    print("✅ Test (Remove Friend) Passed")



BTW_DELAY = 3
test_register()
sleep(BTW_DELAY)
test_login(True)
sleep(BTW_DELAY)
test_logout()
sleep(BTW_DELAY)
test_create_post(True)
sleep(BTW_DELAY)
test_like_post()
sleep(BTW_DELAY)
test_unlike_post()
sleep(BTW_DELAY)
test_comment_on_post()
sleep(BTW_DELAY)
test_delete_post()
sleep(BTW_DELAY)
test_add_friend()
sleep(BTW_DELAY)
test_remove_friend()
sleep(BTW_DELAY)

driver.close()
