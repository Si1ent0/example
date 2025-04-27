
import allure

from selene import browser, be


class MainPage:
    def __init__(self):
        self.test_robot = browser.element('button.start')
        # top bar
        self.burger_menu = browser.element('//div[@class="PortalNavigation__icon"]')
        self.logo = browser.element('a.VKVideoLogo')
        self.search_input = browser.element('.vkuiSearch__field')
        self.button_clear = browser.element('.vkuiSearch__icon')
        self.video_for_authors = browser.element('//a[contains(text(),"VK Видео для авторов")]')
        self.button_add_action = browser.element('.vkitIconButton__rootCustomSize--Wykl1')
        self.notification = browser.element('#top_notify_btn')
        self.button_profile_menu = browser.element('#top_profile_link')
        self.button_registration = browser.element('#top_reg_link')
        # profile menu
        self.avatar = browser.element('img.vkuiImageBase__img ')
        self.user_name = browser.element('span.UserPlaceholder_header__llc2m')
        self.account_settings = browser.element('div.EcoPlate_lk__wEKCB')
        self.my_channels = browser.element('//*[@id="react_rootEcoPlateEntry"]/div/div/a[1]')
        self.balance = browser.element('//a[@href="/settings?act=payments"]')
        self.settings_profile = browser.element('//a[@href="/settings"]')
        self.theme = browser.element('//span[contains(text(),"Тема")]')
        self.support = browser.element('#top_support_link')
        self.logout = browser.element('#top_logout_link')
        # left bar
        self.left_bar = browser.element('div.VideoLayout__aside')
        self.live = browser.element('//a[@data-testid="main_menu_vk_live"]')
        self.main_button = browser.element('//a[@data-testid="main_menu_trends"]')
        self.trends = browser.element('//a[@data-testid="main_menu_popular_trends"]')
        self.clips = browser.element('//a[@data-testid="main_menu_clips"]')
        self.history = browser.element('//a[@data-testid="main_menu_my_history"]')
        self.watch_later = browser.element('//a[@data-testid="main_menu_my_bookmarks"]')
        self.liked_video = browser.element('//a[@data-testid="main_menu_my_liked"]')
        self.my_video = browser.element('//a[@data-testid="main_menu_my"]')
        self.add_video = browser.element('//a[@data-testid="main_menu_my_added"]')
        self.my_upload_video = browser.element('//a[@data-testid="main_menu_my_uploaded"]')
        self.my_live_video = browser.element('//a[@data-testid="main_menu_my_lives"]')
        self.my_rec_video = browser.element('//a[@data-testid="main_menu_my_recorded_calls"]')
        self.my_playlist = browser.element('//a[@data-testid="main_menu_all_playlists"]')
        self.my_community = browser.element('//a[@data-testid="main_menu_my_communities"]')
        self.victory_day = browser.element('//a[@data-testid="main_menu_victory_day"]')
        self.for_kids = browser.element('//a[@data-testid="main_menu_for_kids"]')
        self.television = browser.element('//a[@data-testid="main_menu_tvchannels_new"]')
        self.movie = browser.element('//a[@data-testid="main_menu_movie"]')
        self.tv_show = browser.element('//a[@data-testid="main_menu_tvshow"]')
        self.toggle = browser.element('//button[@data-testid="main_menu_section_toggle"]')
        self.subscribe = browser.element('//a[@data-testid="main_menu_subscribes"]')
        # tab slider
        self.all = browser.element('//div[@data-testid="tab-/"]')
        self.interview = browser.element('//div[@data-testid="tab-/interview"]')
        self.politic = browser.element('//div[@data-testid="tab-/politic"]')
        self.music = browser.element('//div[@data-testid="tab-/music"]')
        self.tourism = browser.element('//div[@data-testid="tab-/tourisme"]')
        self.auto = browser.element('//div[@data-testid="tab-/automotive"]')
        self.technology = browser.element('//div[@data-testid="tab-/technology"]')
        self.food = browser.element('//div[@data-testid="tab-/cooking"]')
        # Карточка видео / card video
        self.card_video = browser.element('//a[@data-testid="video_card_thumb"]')
        self.duration_video = browser.element('//a[@data-testid="video_card_duration"]')
        self.logo_author_video = browser.element('//a[@data-testid="video_card_author"]')
        self.title_video = browser.element('//a[@data-testid="video_card_title"]')
        self.action_menu_video = browser.element('//a[@data-testid="video_card_more"]')
        self.author_video = browser.element('//a[@data-testid="video_card_owner"]')
        self.author_video = browser.element('//a[@data-testid="video_card_additional_info"]')
        # Блок быстрой регистрации
        self.title_quick_log = browser.element('div.VideoQuickLogin__title')
        self.text_quick_log = browser.element('div.VideoQuickLogin__text')
        self.quick_log_button = browser.element('//div[@class="VideoQuickLogin__actions"]/div[@data-task-click="VideoShowcase/login"]')
        self.quick_reg_button = browser.element('//div[@class="VideoQuickLogin__actions"]/a[@data-task-click="VideoShowcase/registration"]')



    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        browser.open('/')
        self.test_robot.click()

    # top bar
    @allure.step("Отображается бургер меню")
    def burger_menu_should_be_display(self):
        self.burger_menu.should(be.visible)

    @allure.step("Отображается лого")
    def logo_should_should_be_display(self):
        self.logo.should(be.visible)

    @allure.step("Отображается строка поиска")
    def search_input_should_be_display(self):
        self.search_input.should(be.visible)

    @allure.step("Отображается кнопка регистрации")
    def reg_button_should_be_display(self):
        self.button_registration.should(be.visible)

    # left bar
    @allure.step("Отображается левый bar")
    def left_bar_should_be_display(self):
        self.left_bar.should(be.visible)

    @allure.step("Отображается live button")
    def live_button_should_be_display(self):
        self.live.should(be.visible)

    @allure.step("Отображается main button")
    def main_button_should_be_display(self):
        self.main_button.should(be.visible)

    @allure.step("Отображается trends button")
    def trends_button_should_be_display(self):
        self.trends.should(be.visible)

    @allure.step("Отображается clips button")
    def clips_button_should_be_display(self):
        self.clips.should(be.visible)

    @allure.step("Отображается history button")
    def history_button_should_be_display(self):
        self.history.should(be.visible)

    @allure.step("Отображается watch latter button")
    def watch_latter_button_should_be_display(self):
        self.watch_later.should(be.visible)

    @allure.step("Отображается liked video button")
    def liked_video_button_should_be_display(self):
        self.liked_video.should(be.visible)

    @allure.step("Отображается victory day button")
    def victory_day_button_should_be_display(self):
        self.victory_day.should(be.visible)

    @allure.step("Отображается for kids button")
    def for_kids_button_should_be_display(self):
        self.for_kids.should(be.visible)

    @allure.step("Отображается television button")
    def television_button_should_be_display(self):
        self.television.should(be.visible)

    @allure.step("Отображается movie button")
    def movie_button_should_be_display(self):
        self.movie.should(be.visible)

    @allure.step("Отображается tv show button")
    def tvshow_button_should_be_display(self):
        self.tv_show.should(be.visible)

    @allure.step("Отображается toggle button")
    def toggle_button_should_be_display(self):
        self.toggle.should(be.visible)

    # быстрый вход в систему
    @allure.step("Отображается title быстрого входа")
    def quick_log_title_should_be_display(self):
        self.title_quick_log.should(be.visible)

    @allure.step("Отображается описание быстрого входа")
    def quick_log_text_should_be_display(self):
        self.text_quick_log.should(be.visible)

    @allure.step("Отображается кнопка логина быстрого входа")
    def quick_log_button_should_be_display(self):
        self.quick_log_button.should(be.visible)

    @allure.step("Отображается кнопка регистрации быстрого входа")
    def quick_reg_button_should_be_display(self):
        self.quick_reg_button.should(be.visible)


    # tab slider
    @allure.step("Отображается кнопка all tab slider")
    def tab_all_should_be_display(self):
        self.all.should(be.visible)

    @allure.step("Отображается кнопка интервью tab slider")
    def tab_interview_should_be_display(self):
        self.interview.should(be.visible)

    @allure.step("Отображается кнопка politic tab slider")
    def tab_politic_should_be_display(self):
        self.politic.should(be.visible)

    @allure.step("Отображается кнопка music tab slider")
    def tab_music_should_be_display(self):
        self.music.should(be.visible)

    @allure.step("Отображается кнопка tourism tab slider")
    def tab_tourism_should_be_display(self):
        self.tourism.should(be.visible)


    @allure.step("Проверка элементов верхнего бара")
    def top_bar_element_should_be_display(self):
        self.burger_menu_should_be_display()
        self.logo_should_should_be_display()
        self.search_input_should_be_display()
        self.reg_button_should_be_display()

    @allure.step("Проверка элементов левого бара")
    def left_bar_element_should_be_display(self):
        self.left_bar_should_be_display()
        self.live_button_should_be_display()
        self.main_button_should_be_display()
        self.trends_button_should_be_display()
        self.clips_button_should_be_display()
        self.victory_day_button_should_be_display()
        self.toggle_button_should_be_display()

    @allure.step("Проверка элементов быстрого входа")
    def quick_log_element_should_be_display(self):
        self.quick_log_title_should_be_display()
        self.quick_log_text_should_be_display()
        self.quick_log_button_should_be_display()
        self.quick_reg_button_should_be_display()

    @allure.step("Проверка элементов tab slider ")
    def tab_slider_element_should_be_display(self):
        self.tab_all_should_be_display()
        self.tab_tourism_should_be_display()
        self.tab_interview_should_be_display()
        self.tab_music_should_be_display()









