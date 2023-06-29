from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.chip import MDChip
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from libs.utils.app_utils import get_app_screen, get_app_version_info, get_app_version_info_string
from libs.utils.screen_utils import init_screen, is_mobile
from libs.theme.theme_utils import PRIMARY_COLORS, ThemeMode
from libs.utils.preferences_service import PreferencesService, Preferences

# https://youtube.com/watch?v=sa4AVMjjzNo
# making app crashing on Android
#window.keyboard_anim_args = {'d': 0.2, 't': 'in_out_expo'}
#window.softinput_mode = "below_target"

class AppScreen(MDScreen):
    pass

class MainApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        init_screen()

    def is_mobile_device(self):
        return is_mobile()

    def get_metadata(self):
        return get_app_version_info()

    def build(self):
        self.service = PreferencesService()
        self.title = self.get_metadata()["name"]
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.theme_style = self.service.get(Preferences.THEME_STYLE.name, default_value=ThemeMode.Dark.name)
        self.theme_cls.primary_palette = self.service.get(Preferences.THEME_PRIMARY_COLOR.name, default_value=PRIMARY_COLORS[0])

        # this is equivalent to just returning Builder.load_file(...)
        # but being explicit here for clarity about whats going on with root widget
        Builder.load_file("main_layout.kv")
        appScreen = AppScreen()
        return appScreen

    def on_start(self):
        Clock.schedule_once(self.on_app_started, 0)
    
    def on_app_started(self, *args):
        info = get_app_version_info_string()
        print(f"App <{info}> started.")

    def on_stop(self):
        print("App stopped.")

    def show_info(self, *args):
        self.root.ids['screen_manager'].current = "about"

    def exit(self):
        Clock.schedule_once(self.stop, 0)

if __name__ == '__main__':
    MainApp().run()
