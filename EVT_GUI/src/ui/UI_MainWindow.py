from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QRect, QSize)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import *

from components import WidgetBase, ButtonBase, NavigationButton, HollowButton, MenuButton, CheckBoxBase, LabelBase, LineEditBase, TextEditBase, TextBrowserBase, ComboBoxBase, Frame_RangeSetting, SpinBoxBase, DoubleSpinBoxBase, ProgressBarBase, ToolBoxBase, GroupBoxBase, ScrollAreaBase, TreeWidgetBase, TabWidgetBase, Table_ViewModels, Table_EditAudioSpeaker
from views import ToolPage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.verticalLayout = QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QFrame(self.CentralWidget)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setMinimumSize(QSize(0, 30))
        self.TitleBar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_30 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Frame_Top_Toggle_Menu = QFrame(self.TitleBar)
        self.Frame_Top_Toggle_Menu.setObjectName(u"Frame_Top_Toggle_Menu")
        self.Frame_Top_Toggle_Menu.setMinimumSize(QSize(48, 0))
        self.Frame_Top_Toggle_Menu.setMaximumSize(QSize(48, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.Frame_Top_Toggle_Menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Button_Toggle_Menu = QPushButton(self.Frame_Top_Toggle_Menu)
        self.Button_Toggle_Menu.setObjectName(u"Button_Toggle_Menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Toggle_Menu.sizePolicy().hasHeightForWidth())
        self.Button_Toggle_Menu.setSizePolicy(sizePolicy)
        self.Button_Toggle_Menu.setStyleSheet(u"QPushButton {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	image: url(:/Button_Icon/images/icons/Menu.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 1.5px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"QPushButton:checked {\n"
"	/*background-color: rgb(45, 45, 45);*/\n"
"}")

        self.verticalLayout_2.addWidget(self.Button_Toggle_Menu)


        self.horizontalLayout_30.addWidget(self.Frame_Top_Toggle_Menu)

        self.Frame_Top = QFrame(self.TitleBar)
        self.Frame_Top.setObjectName(u"Frame_Top")
        self.horizontalLayout_11 = QHBoxLayout(self.Frame_Top)
        self.horizontalLayout_11.setSpacing(21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_Right_Top = QSpacerItem(587, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.HorizontalSpacer_Right_Top)

        self.CheckBox_SwitchTheme = CheckBoxBase(self.Frame_Top)
        self.CheckBox_SwitchTheme.setObjectName(u"CheckBox_SwitchTheme")

        self.horizontalLayout_11.addWidget(self.CheckBox_SwitchTheme)

        self.Frame_Top_Control_Window = QFrame(self.Frame_Top)
        self.Frame_Top_Control_Window.setObjectName(u"Frame_Top_Control_Window")
        self.Frame_Top_Control_Window.setMinimumSize(QSize(144, 0))
        self.Frame_Top_Control_Window.setMaximumSize(QSize(144, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.Frame_Top_Control_Window)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Button_Minimize_Window = ButtonBase(self.Frame_Top_Control_Window)
        self.Button_Minimize_Window.setObjectName(u"Button_Minimize_Window")
        sizePolicy.setHeightForWidth(self.Button_Minimize_Window.sizePolicy().hasHeightForWidth())
        self.Button_Minimize_Window.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.Button_Minimize_Window)

        self.Button_Maximize_Window = ButtonBase(self.Frame_Top_Control_Window)
        self.Button_Maximize_Window.setObjectName(u"Button_Maximize_Window")
        sizePolicy.setHeightForWidth(self.Button_Maximize_Window.sizePolicy().hasHeightForWidth())
        self.Button_Maximize_Window.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.Button_Maximize_Window)

        self.Button_Close_Window = ButtonBase(self.Frame_Top_Control_Window)
        self.Button_Close_Window.setObjectName(u"Button_Close_Window")
        sizePolicy.setHeightForWidth(self.Button_Close_Window.sizePolicy().hasHeightForWidth())
        self.Button_Close_Window.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.Button_Close_Window)


        self.horizontalLayout_11.addWidget(self.Frame_Top_Control_Window)


        self.horizontalLayout_30.addWidget(self.Frame_Top)


        self.verticalLayout.addWidget(self.TitleBar)

        self.Content = QFrame(self.CentralWidget)
        self.Content.setObjectName(u"Content")
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Frame_Menu = QFrame(self.Content)
        self.Frame_Menu.setObjectName(u"Frame_Menu")
        self.Frame_Menu.setMinimumSize(QSize(210, 0))
        self.Frame_Menu.setMaximumSize(QSize(210, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.Frame_Menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 3)
        self.Button_Menu_Home = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Home.setObjectName(u"Button_Menu_Home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_Menu_Home.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Home.setSizePolicy(sizePolicy1)
        self.Button_Menu_Home.setMinimumSize(QSize(0, 48))
        icon = QIcon()
        icon.addFile(u":/Button_Icon/images/icons/Home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Home.setIcon(icon)
        self.Button_Menu_Home.setIconSize(QSize(24, 24))
        self.horizontalLayout_8 = QHBoxLayout(self.Button_Menu_Home)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Home)

        self.Button_Menu_Env = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Env.setObjectName(u"Button_Menu_Env")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Env.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Env.setSizePolicy(sizePolicy1)
        self.Button_Menu_Env.setMinimumSize(QSize(0, 48))
        icon1 = QIcon()
        icon1.addFile(u":/Button_Icon/images/icons/Box.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Env.setIcon(icon1)
        self.Button_Menu_Env.setIconSize(QSize(24, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.Button_Menu_Env)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Env)

        self.Button_Menu_Models = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Models.setObjectName(u"Button_Menu_Models")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Models.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Models.setSizePolicy(sizePolicy1)
        self.Button_Menu_Models.setMinimumSize(QSize(0, 48))
        icon2 = QIcon()
        icon2.addFile(u":/Button_Icon/images/icons/Boxes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Models.setIcon(icon2)
        self.Button_Menu_Models.setIconSize(QSize(24, 24))
        self.horizontalLayout_34 = QHBoxLayout(self.Button_Menu_Models)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Models)

        self.Button_Menu_Process = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Process.setObjectName(u"Button_Menu_Process")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Process.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Process.setSizePolicy(sizePolicy1)
        self.Button_Menu_Process.setMinimumSize(QSize(0, 48))
        icon3 = QIcon()
        icon3.addFile(u":/Button_Icon/images/icons/Audio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Process.setIcon(icon3)
        self.Button_Menu_Process.setIconSize(QSize(24, 24))
        self.horizontalLayout_33 = QHBoxLayout(self.Button_Menu_Process)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Process)

        self.Button_Menu_VPR = NavigationButton(self.Frame_Menu)
        self.Button_Menu_VPR.setObjectName(u"Button_Menu_VPR")
        sizePolicy1.setHeightForWidth(self.Button_Menu_VPR.sizePolicy().hasHeightForWidth())
        self.Button_Menu_VPR.setSizePolicy(sizePolicy1)
        self.Button_Menu_VPR.setMinimumSize(QSize(0, 48))
        icon4 = QIcon()
        icon4.addFile(u":/Button_Icon/images/icons/VPR.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_VPR.setIcon(icon4)
        self.Button_Menu_VPR.setIconSize(QSize(24, 24))
        self.horizontalLayout_10 = QHBoxLayout(self.Button_Menu_VPR)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_VPR)

        self.Button_Menu_ASR = NavigationButton(self.Frame_Menu)
        self.Button_Menu_ASR.setObjectName(u"Button_Menu_ASR")
        sizePolicy1.setHeightForWidth(self.Button_Menu_ASR.sizePolicy().hasHeightForWidth())
        self.Button_Menu_ASR.setSizePolicy(sizePolicy1)
        self.Button_Menu_ASR.setMinimumSize(QSize(0, 48))
        icon5 = QIcon()
        icon5.addFile(u":/Button_Icon/images/icons/ASR.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_ASR.setIcon(icon5)
        self.Button_Menu_ASR.setIconSize(QSize(24, 24))
        self.horizontalLayout_36 = QHBoxLayout(self.Button_Menu_ASR)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_ASR)

        self.Button_Menu_Dataset = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Dataset.setObjectName(u"Button_Menu_Dataset")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Dataset.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Dataset.setSizePolicy(sizePolicy1)
        self.Button_Menu_Dataset.setMinimumSize(QSize(0, 48))
        icon6 = QIcon()
        icon6.addFile(u":/Button_Icon/images/icons/Dataset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Dataset.setIcon(icon6)
        self.Button_Menu_Dataset.setIconSize(QSize(24, 24))
        self.horizontalLayout_38 = QHBoxLayout(self.Button_Menu_Dataset)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Dataset)

        self.Button_Menu_Train = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Train.setObjectName(u"Button_Menu_Train")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Train.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Train.setSizePolicy(sizePolicy1)
        self.Button_Menu_Train.setMinimumSize(QSize(0, 48))
        icon7 = QIcon()
        icon7.addFile(u":/Button_Icon/images/icons/HDD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Train.setIcon(icon7)
        self.Button_Menu_Train.setIconSize(QSize(24, 24))
        self.horizontalLayout_40 = QHBoxLayout(self.Button_Menu_Train)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Train)

        self.Button_Menu_TTS = NavigationButton(self.Frame_Menu)
        self.Button_Menu_TTS.setObjectName(u"Button_Menu_TTS")
        sizePolicy1.setHeightForWidth(self.Button_Menu_TTS.sizePolicy().hasHeightForWidth())
        self.Button_Menu_TTS.setSizePolicy(sizePolicy1)
        self.Button_Menu_TTS.setMinimumSize(QSize(0, 48))
        icon8 = QIcon()
        icon8.addFile(u":/Button_Icon/images/icons/TTS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_TTS.setIcon(icon8)
        self.Button_Menu_TTS.setIconSize(QSize(24, 24))
        self.horizontalLayout_47 = QHBoxLayout(self.Button_Menu_TTS)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_TTS)

        self.VerticalSpacer_Menu = QSpacerItem(20, 522, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.VerticalSpacer_Menu)

        self.Button_Menu_Settings = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Settings.setObjectName(u"Button_Menu_Settings")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Settings.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Settings.setSizePolicy(sizePolicy1)
        self.Button_Menu_Settings.setMinimumSize(QSize(0, 48))
        icon9 = QIcon()
        icon9.addFile(u":/Button_Icon/images/icons/Settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Settings.setIcon(icon9)
        self.Button_Menu_Settings.setIconSize(QSize(24, 24))
        self.horizontalLayout_9 = QHBoxLayout(self.Button_Menu_Settings)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Settings)

        self.Button_Menu_Info = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Info.setObjectName(u"Button_Menu_Info")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Info.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Info.setSizePolicy(sizePolicy1)
        self.Button_Menu_Info.setMinimumSize(QSize(0, 48))
        icon10 = QIcon()
        icon10.addFile(u":/Button_Icon/images/icons/Info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Info.setIcon(icon10)
        self.Button_Menu_Info.setIconSize(QSize(24, 24))
        self.horizontalLayout_13 = QHBoxLayout(self.Button_Menu_Info)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Info)


        self.horizontalLayout_2.addWidget(self.Frame_Menu)

        self.Frame_Pages = QFrame(self.Content)
        self.Frame_Pages.setObjectName(u"Frame_Pages")
        self.verticalLayout_5 = QVBoxLayout(self.Frame_Pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Splitter_Pages = QSplitter(self.Frame_Pages)
        self.Splitter_Pages.setObjectName(u"Splitter_Pages")
        self.Splitter_Pages.setOrientation(Qt.Orientation.Vertical)
        self.Splitter_Pages.setHandleWidth(0)
        self.Splitter_Pages.setChildrenCollapsible(False)
        self.StackedWidget_Pages = QStackedWidget(self.Splitter_Pages)
        self.StackedWidget_Pages.setObjectName(u"StackedWidget_Pages")
        self.Page_Home = QWidget()
        self.Page_Home.setObjectName(u"Page_Home")
        self.verticalLayout_99 = QVBoxLayout(self.Page_Home)
        self.verticalLayout_99.setSpacing(21)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(21, 12, 21, 12)
        self.Frame_High_Home = QFrame(self.Page_Home)
        self.Frame_High_Home.setObjectName(u"Frame_High_Home")
        self.Frame_High_Home.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_100 = QVBoxLayout(self.Frame_High_Home)
        self.verticalLayout_100.setSpacing(21)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(12, 0, 12, 0)
        self.Label_Cover_Home = LabelBase(self.Frame_High_Home)
        self.Label_Cover_Home.setObjectName(u"Label_Cover_Home")
        sizePolicy.setHeightForWidth(self.Label_Cover_Home.sizePolicy().hasHeightForWidth())
        self.Label_Cover_Home.setSizePolicy(sizePolicy)
        self.Label_Cover_Home.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: grey;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QLabel:hover {\n"
"}")

        self.verticalLayout_100.addWidget(self.Label_Cover_Home)

        self.TextBrowser_Text_Home = TextBrowserBase(self.Frame_High_Home)
        self.TextBrowser_Text_Home.setObjectName(u"TextBrowser_Text_Home")

        self.verticalLayout_100.addWidget(self.TextBrowser_Text_Home)


        self.verticalLayout_99.addWidget(self.Frame_High_Home)

        self.Frame_Low_Home = QFrame(self.Page_Home)
        self.Frame_Low_Home.setObjectName(u"Frame_Low_Home")
        self.Frame_Low_Home.setMinimumSize(QSize(0, 90))
        self.Frame_Low_Home.setStyleSheet(u"QFrame {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.Frame_Low_Home)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 0, 12, 0)
        self.Button_Demo = HollowButton(self.Frame_Low_Home)
        self.Button_Demo.setObjectName(u"Button_Demo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_Demo.sizePolicy().hasHeightForWidth())
        self.Button_Demo.setSizePolicy(sizePolicy2)
        self.Button_Demo.setMinimumSize(QSize(210, 75))
        self.horizontalLayout_70 = QHBoxLayout(self.Button_Demo)
        self.horizontalLayout_70.setSpacing(12)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(21, 12, 21, 12)
        self.Label_Demo_Icon = QLabel(self.Button_Demo)
        self.Label_Demo_Icon.setObjectName(u"Label_Demo_Icon")
        self.Label_Demo_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/images/icons/Play.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_70.addWidget(self.Label_Demo_Icon)

        self.Label_Demo_Text = LabelBase(self.Button_Demo)
        self.Label_Demo_Text.setObjectName(u"Label_Demo_Text")

        self.horizontalLayout_70.addWidget(self.Label_Demo_Text)

        self.horizontalLayout_70.setStretch(0, 2)
        self.horizontalLayout_70.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Demo)

        self.HorizontalSpacer_Low_Home_1 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_1)

        self.Button_Server = HollowButton(self.Frame_Low_Home)
        self.Button_Server.setObjectName(u"Button_Server")
        sizePolicy2.setHeightForWidth(self.Button_Server.sizePolicy().hasHeightForWidth())
        self.Button_Server.setSizePolicy(sizePolicy2)
        self.Button_Server.setMinimumSize(QSize(210, 75))
        self.horizontalLayout_71 = QHBoxLayout(self.Button_Server)
        self.horizontalLayout_71.setSpacing(12)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(21, 12, 21, 12)
        self.Label_Server_Icon = QLabel(self.Button_Server)
        self.Label_Server_Icon.setObjectName(u"Label_Server_Icon")
        self.Label_Server_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/images/icons/Server.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_71.addWidget(self.Label_Server_Icon)

        self.Label_Server_Text = LabelBase(self.Button_Server)
        self.Label_Server_Text.setObjectName(u"Label_Server_Text")

        self.horizontalLayout_71.addWidget(self.Label_Server_Text)

        self.horizontalLayout_71.setStretch(0, 2)
        self.horizontalLayout_71.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Server)

        self.HorizontalSpacer_Low_Home_2 = QSpacerItem(106, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_2)

        self.Button_Repo = HollowButton(self.Frame_Low_Home)
        self.Button_Repo.setObjectName(u"Button_Repo")
        sizePolicy2.setHeightForWidth(self.Button_Repo.sizePolicy().hasHeightForWidth())
        self.Button_Repo.setSizePolicy(sizePolicy2)
        self.Button_Repo.setMinimumSize(QSize(210, 75))
        self.horizontalLayout_76 = QHBoxLayout(self.Button_Repo)
        self.horizontalLayout_76.setSpacing(12)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(21, 12, 21, 12)
        self.Label_Repo_Icon = QLabel(self.Button_Repo)
        self.Label_Repo_Icon.setObjectName(u"Label_Repo_Icon")
        self.Label_Repo_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/images/icons/GitHub.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_76.addWidget(self.Label_Repo_Icon)

        self.Label_Repo_Text = LabelBase(self.Button_Repo)
        self.Label_Repo_Text.setObjectName(u"Label_Repo_Text")

        self.horizontalLayout_76.addWidget(self.Label_Repo_Text)

        self.horizontalLayout_76.setStretch(0, 2)
        self.horizontalLayout_76.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Repo)

        self.HorizontalSpacer_Low_Home_3 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_3)

        self.Button_Donate = HollowButton(self.Frame_Low_Home)
        self.Button_Donate.setObjectName(u"Button_Donate")
        sizePolicy2.setHeightForWidth(self.Button_Donate.sizePolicy().hasHeightForWidth())
        self.Button_Donate.setSizePolicy(sizePolicy2)
        self.Button_Donate.setMinimumSize(QSize(210, 75))
        self.horizontalLayout_79 = QHBoxLayout(self.Button_Donate)
        self.horizontalLayout_79.setSpacing(12)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(21, 12, 21, 12)
        self.Label_Donate_Icon = QLabel(self.Button_Donate)
        self.Label_Donate_Icon.setObjectName(u"Label_Donate_Icon")
        self.Label_Donate_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/images/icons/Heart.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_79.addWidget(self.Label_Donate_Icon)

        self.Label_Donate_Text = LabelBase(self.Button_Donate)
        self.Label_Donate_Text.setObjectName(u"Label_Donate_Text")

        self.horizontalLayout_79.addWidget(self.Label_Donate_Text)

        self.horizontalLayout_79.setStretch(0, 2)
        self.horizontalLayout_79.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Donate)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(2, 3)
        self.horizontalLayout_5.setStretch(4, 3)
        self.horizontalLayout_5.setStretch(6, 3)

        self.verticalLayout_99.addWidget(self.Frame_Low_Home)

        self.StackedWidget_Pages.addWidget(self.Page_Home)
        self.Page_Env = QWidget()
        self.Page_Env.setObjectName(u"Page_Env")
        self.verticalLayout_128 = QVBoxLayout(self.Page_Env)
        self.verticalLayout_128.setSpacing(21)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(21, 12, 21, 12)
        self.Frame_Env_Install_Top = QFrame(self.Page_Env)
        self.Frame_Env_Install_Top.setObjectName(u"Frame_Env_Install_Top")
        self.Frame_Env_Install_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Env_Install_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.Frame_Env_Install_Top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Button_Env_Install_Title = NavigationButton(self.Frame_Env_Install_Top)
        self.Button_Env_Install_Title.setObjectName(u"Button_Env_Install_Title")
        sizePolicy1.setHeightForWidth(self.Button_Env_Install_Title.sizePolicy().hasHeightForWidth())
        self.Button_Env_Install_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.Button_Env_Install_Title)

        self.Button_Env_Manage_Title = NavigationButton(self.Frame_Env_Install_Top)
        self.Button_Env_Manage_Title.setObjectName(u"Button_Env_Manage_Title")
        sizePolicy1.setHeightForWidth(self.Button_Env_Manage_Title.sizePolicy().hasHeightForWidth())
        self.Button_Env_Manage_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.Button_Env_Manage_Title)

        self.HorizontalSpacer_Env_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.HorizontalSpacer_Env_Title)


        self.verticalLayout_128.addWidget(self.Frame_Env_Install_Top)

        self.StackedWidget_Pages_Env = QStackedWidget(self.Page_Env)
        self.StackedWidget_Pages_Env.setObjectName(u"StackedWidget_Pages_Env")
        self.StackedWidget_Pages_Env.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.SubPage_Env_Install = QWidget()
        self.SubPage_Env_Install.setObjectName(u"SubPage_Env_Install")
        self.gridLayout_103 = QGridLayout(self.SubPage_Env_Install)
        self.gridLayout_103.setSpacing(12)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.gridLayout_103.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Env_Install = ScrollAreaBase(self.SubPage_Env_Install)
        self.ScrollArea_Env_Install.setObjectName(u"ScrollArea_Env_Install")
        self.ScrollArea_Env_Install.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Env_Install = QWidget()
        self.ScrollAreaWidgetContents_Env_Install.setObjectName(u"ScrollAreaWidgetContents_Env_Install")
        self.ScrollAreaWidgetContents_Env_Install.setGeometry(QRect(0, 0, 242, 495))
        self.verticalLayout_130 = QVBoxLayout(self.ScrollAreaWidgetContents_Env_Install)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.Frame_Env_Install_Middle = QFrame(self.ScrollAreaWidgetContents_Env_Install)
        self.Frame_Env_Install_Middle.setObjectName(u"Frame_Env_Install_Middle")
        self.Frame_Env_Install_Middle.setStyleSheet(u"QFrame {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_127 = QVBoxLayout(self.Frame_Env_Install_Middle)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.Frame_Env_Install_Aria2 = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Aria2.setObjectName(u"Frame_Env_Install_Aria2")
        self.Frame_Env_Install_Aria2.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Aria2.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Aria2.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_118 = QGridLayout(self.Frame_Env_Install_Aria2)
        self.gridLayout_118.setSpacing(12)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.gridLayout_118.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_Aria2 = QPushButton(self.Frame_Env_Install_Aria2)
        self.Button_Install_Aria2.setObjectName(u"Button_Install_Aria2")
        self.Button_Install_Aria2.setMaximumSize(QSize(33, 33))
        self.Button_Install_Aria2.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/images/icons/Refresh.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_118.addWidget(self.Button_Install_Aria2, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Aria2 = ProgressBarBase(self.Frame_Env_Install_Aria2)
        self.ProgressBar_Env_Install_Aria2.setObjectName(u"ProgressBar_Env_Install_Aria2")
        self.ProgressBar_Env_Install_Aria2.setMaximumSize(QSize(16777215, 3))

        self.gridLayout_118.addWidget(self.ProgressBar_Env_Install_Aria2, 1, 0, 1, 2)

        self.Label_Env_Install_Aria2_Status = LabelBase(self.Frame_Env_Install_Aria2)
        self.Label_Env_Install_Aria2_Status.setObjectName(u"Label_Env_Install_Aria2_Status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Label_Env_Install_Aria2_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_Aria2_Status.setSizePolicy(sizePolicy3)
        self.Label_Env_Install_Aria2_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_118.addWidget(self.Label_Env_Install_Aria2_Status, 2, 0, 1, 2)

        self.Label_Env_Install_Aria2 = LabelBase(self.Frame_Env_Install_Aria2)
        self.Label_Env_Install_Aria2.setObjectName(u"Label_Env_Install_Aria2")
        self.Label_Env_Install_Aria2.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_118.addWidget(self.Label_Env_Install_Aria2, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_Aria2)

        self.Frame_Env_Install_FFmpeg = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_FFmpeg.setObjectName(u"Frame_Env_Install_FFmpeg")
        self.Frame_Env_Install_FFmpeg.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_FFmpeg.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_FFmpeg.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_119 = QGridLayout(self.Frame_Env_Install_FFmpeg)
        self.gridLayout_119.setSpacing(12)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.gridLayout_119.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_FFmpeg = QPushButton(self.Frame_Env_Install_FFmpeg)
        self.Button_Install_FFmpeg.setObjectName(u"Button_Install_FFmpeg")
        self.Button_Install_FFmpeg.setMaximumSize(QSize(33, 33))
        self.Button_Install_FFmpeg.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/images/icons/Refresh.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_119.addWidget(self.Button_Install_FFmpeg, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_FFmpeg = ProgressBarBase(self.Frame_Env_Install_FFmpeg)
        self.ProgressBar_Env_Install_FFmpeg.setObjectName(u"ProgressBar_Env_Install_FFmpeg")
        self.ProgressBar_Env_Install_FFmpeg.setMaximumSize(QSize(16777215, 3))

        self.gridLayout_119.addWidget(self.ProgressBar_Env_Install_FFmpeg, 1, 0, 1, 2)

        self.Label_Env_Install_FFmpeg_Status = LabelBase(self.Frame_Env_Install_FFmpeg)
        self.Label_Env_Install_FFmpeg_Status.setObjectName(u"Label_Env_Install_FFmpeg_Status")
        sizePolicy3.setHeightForWidth(self.Label_Env_Install_FFmpeg_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_FFmpeg_Status.setSizePolicy(sizePolicy3)
        self.Label_Env_Install_FFmpeg_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_119.addWidget(self.Label_Env_Install_FFmpeg_Status, 2, 0, 1, 2)

        self.Label_Env_Install_FFmpeg = LabelBase(self.Frame_Env_Install_FFmpeg)
        self.Label_Env_Install_FFmpeg.setObjectName(u"Label_Env_Install_FFmpeg")
        self.Label_Env_Install_FFmpeg.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_119.addWidget(self.Label_Env_Install_FFmpeg, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_FFmpeg)

        self.Frame_Env_Install_Python = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Python.setObjectName(u"Frame_Env_Install_Python")
        self.Frame_Env_Install_Python.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Python.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Python.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_120 = QGridLayout(self.Frame_Env_Install_Python)
        self.gridLayout_120.setSpacing(12)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.gridLayout_120.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_Python = QPushButton(self.Frame_Env_Install_Python)
        self.Button_Install_Python.setObjectName(u"Button_Install_Python")
        self.Button_Install_Python.setMaximumSize(QSize(33, 33))
        self.Button_Install_Python.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/images/icons/Refresh.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_120.addWidget(self.Button_Install_Python, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Python = ProgressBarBase(self.Frame_Env_Install_Python)
        self.ProgressBar_Env_Install_Python.setObjectName(u"ProgressBar_Env_Install_Python")
        self.ProgressBar_Env_Install_Python.setMaximumSize(QSize(16777215, 3))

        self.gridLayout_120.addWidget(self.ProgressBar_Env_Install_Python, 1, 0, 1, 2)

        self.Label_Env_Install_Python_Status = LabelBase(self.Frame_Env_Install_Python)
        self.Label_Env_Install_Python_Status.setObjectName(u"Label_Env_Install_Python_Status")
        sizePolicy3.setHeightForWidth(self.Label_Env_Install_Python_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_Python_Status.setSizePolicy(sizePolicy3)
        self.Label_Env_Install_Python_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_120.addWidget(self.Label_Env_Install_Python_Status, 2, 0, 1, 2)

        self.Label_Env_Install_Python = LabelBase(self.Frame_Env_Install_Python)
        self.Label_Env_Install_Python.setObjectName(u"Label_Env_Install_Python")
        self.Label_Env_Install_Python.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_120.addWidget(self.Label_Env_Install_Python, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_Python)

        self.Frame_Env_Install_PyReqs = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_PyReqs.setObjectName(u"Frame_Env_Install_PyReqs")
        self.Frame_Env_Install_PyReqs.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_PyReqs.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_PyReqs.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_121 = QGridLayout(self.Frame_Env_Install_PyReqs)
        self.gridLayout_121.setSpacing(12)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.gridLayout_121.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_PyReqs = QPushButton(self.Frame_Env_Install_PyReqs)
        self.Button_Install_PyReqs.setObjectName(u"Button_Install_PyReqs")
        self.Button_Install_PyReqs.setMaximumSize(QSize(33, 33))
        self.Button_Install_PyReqs.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/images/icons/Refresh.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_121.addWidget(self.Button_Install_PyReqs, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_PyReqs = ProgressBarBase(self.Frame_Env_Install_PyReqs)
        self.ProgressBar_Env_Install_PyReqs.setObjectName(u"ProgressBar_Env_Install_PyReqs")
        self.ProgressBar_Env_Install_PyReqs.setMaximumSize(QSize(16777215, 3))

        self.gridLayout_121.addWidget(self.ProgressBar_Env_Install_PyReqs, 1, 0, 1, 2)

        self.Label_Env_Install_PyReqs_Status = LabelBase(self.Frame_Env_Install_PyReqs)
        self.Label_Env_Install_PyReqs_Status.setObjectName(u"Label_Env_Install_PyReqs_Status")
        sizePolicy3.setHeightForWidth(self.Label_Env_Install_PyReqs_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_PyReqs_Status.setSizePolicy(sizePolicy3)
        self.Label_Env_Install_PyReqs_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_121.addWidget(self.Label_Env_Install_PyReqs_Status, 2, 0, 1, 2)

        self.Label_Env_Install_PyReqs = LabelBase(self.Frame_Env_Install_PyReqs)
        self.Label_Env_Install_PyReqs.setObjectName(u"Label_Env_Install_PyReqs")
        self.Label_Env_Install_PyReqs.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_121.addWidget(self.Label_Env_Install_PyReqs, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_PyReqs)

        self.Frame_Env_Install_Pytorch = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Pytorch.setObjectName(u"Frame_Env_Install_Pytorch")
        self.Frame_Env_Install_Pytorch.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Pytorch.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Pytorch.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_122 = QGridLayout(self.Frame_Env_Install_Pytorch)
        self.gridLayout_122.setSpacing(12)
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.gridLayout_122.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_Pytorch = QPushButton(self.Frame_Env_Install_Pytorch)
        self.Button_Install_Pytorch.setObjectName(u"Button_Install_Pytorch")
        self.Button_Install_Pytorch.setMaximumSize(QSize(33, 33))
        self.Button_Install_Pytorch.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/images/icons/Refresh.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_122.addWidget(self.Button_Install_Pytorch, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Pytorch = ProgressBarBase(self.Frame_Env_Install_Pytorch)
        self.ProgressBar_Env_Install_Pytorch.setObjectName(u"ProgressBar_Env_Install_Pytorch")
        self.ProgressBar_Env_Install_Pytorch.setMaximumSize(QSize(16777215, 3))

        self.gridLayout_122.addWidget(self.ProgressBar_Env_Install_Pytorch, 1, 0, 1, 2)

        self.Label_Env_Install_Pytorch_Status = LabelBase(self.Frame_Env_Install_Pytorch)
        self.Label_Env_Install_Pytorch_Status.setObjectName(u"Label_Env_Install_Pytorch_Status")
        sizePolicy3.setHeightForWidth(self.Label_Env_Install_Pytorch_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_Pytorch_Status.setSizePolicy(sizePolicy3)
        self.Label_Env_Install_Pytorch_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_122.addWidget(self.Label_Env_Install_Pytorch_Status, 2, 0, 1, 2)

        self.Label_Env_Install_Pytorch = LabelBase(self.Frame_Env_Install_Pytorch)
        self.Label_Env_Install_Pytorch.setObjectName(u"Label_Env_Install_Pytorch")
        self.Label_Env_Install_Pytorch.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_122.addWidget(self.Label_Env_Install_Pytorch, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_Pytorch)


        self.verticalLayout_130.addWidget(self.Frame_Env_Install_Middle)

        self.VerticalSpacer_Env_Install = QSpacerItem(17, 84, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_130.addItem(self.VerticalSpacer_Env_Install)

        self.ScrollArea_Env_Install.setWidget(self.ScrollAreaWidgetContents_Env_Install)

        self.gridLayout_103.addWidget(self.ScrollArea_Env_Install, 0, 0, 1, 1)

        self.StackedWidget_Pages_Env.addWidget(self.SubPage_Env_Install)
        self.SubPage_Env_Manage = QWidget()
        self.SubPage_Env_Manage.setObjectName(u"SubPage_Env_Manage")
        self.gridLayout_113 = QGridLayout(self.SubPage_Env_Manage)
        self.gridLayout_113.setSpacing(12)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.gridLayout_113.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Env_Manage = ScrollAreaBase(self.SubPage_Env_Manage)
        self.ScrollArea_Env_Manage.setObjectName(u"ScrollArea_Env_Manage")
        self.ScrollArea_Env_Manage.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Env_Manage = QWidget()
        self.ScrollAreaWidgetContents_Env_Manage.setObjectName(u"ScrollAreaWidgetContents_Env_Manage")
        self.ScrollAreaWidgetContents_Env_Manage.setGeometry(QRect(0, 0, 86, 84))
        self.verticalLayout_81 = QVBoxLayout(self.ScrollAreaWidgetContents_Env_Manage)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.ToolBox_Env_Manage_Pytorch = ToolBoxBase(self.ScrollAreaWidgetContents_Env_Manage)
        self.ToolBox_Env_Manage_Pytorch.setObjectName(u"ToolBox_Env_Manage_Pytorch")
        self.ToolBox_Env_Manage_Pytorch_Page1Content = WidgetBase()
        self.ToolBox_Env_Manage_Pytorch_Page1Content.setObjectName(u"ToolBox_Env_Manage_Pytorch_Page1Content")
        self.ToolBox_Env_Manage_Pytorch_Page1Content.setGeometry(QRect(0, 0, 292, 204))
        self.verticalLayout_105 = QVBoxLayout(self.ToolBox_Env_Manage_Pytorch_Page1Content)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 12, 0, 12)
        self.Frame_Env_Manage_Pytorch_Version = QFrame(self.ToolBox_Env_Manage_Pytorch_Page1Content)
        self.Frame_Env_Manage_Pytorch_Version.setObjectName(u"Frame_Env_Manage_Pytorch_Version")
        self.Frame_Env_Manage_Pytorch_Version.setMinimumSize(QSize(0, 90))
        self.Frame_Env_Manage_Pytorch_Version.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_67 = QHBoxLayout(self.Frame_Env_Manage_Pytorch_Version)
        self.horizontalLayout_67.setSpacing(12)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Manage_Pytorch_Version = LabelBase(self.Frame_Env_Manage_Pytorch_Version)
        self.Label_Env_Manage_Pytorch_Version.setObjectName(u"Label_Env_Manage_Pytorch_Version")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Label_Env_Manage_Pytorch_Version.sizePolicy().hasHeightForWidth())
        self.Label_Env_Manage_Pytorch_Version.setSizePolicy(sizePolicy4)
        self.Label_Env_Manage_Pytorch_Version.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_67.addWidget(self.Label_Env_Manage_Pytorch_Version)

        self.ComboBox_Env_Manage_Pytorch_Version = ComboBoxBase(self.Frame_Env_Manage_Pytorch_Version)
        self.ComboBox_Env_Manage_Pytorch_Version.setObjectName(u"ComboBox_Env_Manage_Pytorch_Version")
        self.ComboBox_Env_Manage_Pytorch_Version.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_67.addWidget(self.ComboBox_Env_Manage_Pytorch_Version)


        self.verticalLayout_105.addWidget(self.Frame_Env_Manage_Pytorch_Version)

        self.Frame_Env_Manage_Pytorch_Install = QFrame(self.ToolBox_Env_Manage_Pytorch_Page1Content)
        self.Frame_Env_Manage_Pytorch_Install.setObjectName(u"Frame_Env_Manage_Pytorch_Install")
        self.Frame_Env_Manage_Pytorch_Install.setMinimumSize(QSize(0, 90))
        self.Frame_Env_Manage_Pytorch_Install.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.Frame_Env_Manage_Pytorch_Install)
        self.horizontalLayout_26.setSpacing(12)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(21, 12, 21, 12)
        self.HorizontalSpacer_Env_Manage_Pytorch_Install = QSpacerItem(844, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.HorizontalSpacer_Env_Manage_Pytorch_Install)

        self.Button_Env_Manage_Pytorch_Install = HollowButton(self.Frame_Env_Manage_Pytorch_Install)
        self.Button_Env_Manage_Pytorch_Install.setObjectName(u"Button_Env_Manage_Pytorch_Install")
        self.Button_Env_Manage_Pytorch_Install.setMinimumSize(QSize(123, 0))

        self.horizontalLayout_26.addWidget(self.Button_Env_Manage_Pytorch_Install)


        self.verticalLayout_105.addWidget(self.Frame_Env_Manage_Pytorch_Install)

        self.ToolBox_Env_Manage_Pytorch.addItem(self.ToolBox_Env_Manage_Pytorch_Page1Content, u"")

        self.verticalLayout_81.addWidget(self.ToolBox_Env_Manage_Pytorch)

        self.VerticalSpacer_Env_Manage = QSpacerItem(17, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_81.addItem(self.VerticalSpacer_Env_Manage)

        self.ScrollArea_Env_Manage.setWidget(self.ScrollAreaWidgetContents_Env_Manage)

        self.gridLayout_113.addWidget(self.ScrollArea_Env_Manage, 0, 0, 1, 1)

        self.StackedWidget_Pages_Env.addWidget(self.SubPage_Env_Manage)

        self.verticalLayout_128.addWidget(self.StackedWidget_Pages_Env)

        self.StackedWidget_Pages.addWidget(self.Page_Env)
        self.Page_Models = QWidget()
        self.Page_Models.setObjectName(u"Page_Models")
        self.verticalLayout_244 = QVBoxLayout(self.Page_Models)
        self.verticalLayout_244.setSpacing(21)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.verticalLayout_244.setContentsMargins(21, 12, 21, 12)
        self.Frame_Models_Top = QFrame(self.Page_Models)
        self.Frame_Models_Top.setObjectName(u"Frame_Models_Top")
        self.Frame_Models_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Models_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.Frame_Models_Top)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Button_Models_Process_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_Process_Title.setObjectName(u"Button_Models_Process_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_Process_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_Process_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_Process_Title)

        self.Button_Models_VPR_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_VPR_Title.setObjectName(u"Button_Models_VPR_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_VPR_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_VPR_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_VPR_Title)

        self.Button_Models_ASR_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_ASR_Title.setObjectName(u"Button_Models_ASR_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_ASR_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_ASR_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_ASR_Title)

        self.Button_Models_TTS_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_TTS_Title.setObjectName(u"Button_Models_TTS_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_TTS_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_TTS_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_TTS_Title)

        self.HorizontalSpacer_Models_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.HorizontalSpacer_Models_Title)

        self.Button_Models_Refresh = ButtonBase(self.Frame_Models_Top)
        self.Button_Models_Refresh.setObjectName(u"Button_Models_Refresh")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Button_Models_Refresh.sizePolicy().hasHeightForWidth())
        self.Button_Models_Refresh.setSizePolicy(sizePolicy5)
        self.Button_Models_Refresh.setMinimumSize(QSize(84, 0))
        icon11 = QIcon()
        icon11.addFile(u":/Button_Icon/images/icons/Refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Models_Refresh.setIcon(icon11)
        self.Button_Models_Refresh.setIconSize(QSize(21, 21))

        self.horizontalLayout_18.addWidget(self.Button_Models_Refresh)

        self.Button_Models_Append = ButtonBase(self.Frame_Models_Top)
        self.Button_Models_Append.setObjectName(u"Button_Models_Append")
        sizePolicy5.setHeightForWidth(self.Button_Models_Append.sizePolicy().hasHeightForWidth())
        self.Button_Models_Append.setSizePolicy(sizePolicy5)
        self.Button_Models_Append.setMinimumSize(QSize(84, 0))
        icon12 = QIcon()
        icon12.addFile(u":/Button_Icon/images/icons/Plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Models_Append.setIcon(icon12)
        self.Button_Models_Append.setIconSize(QSize(21, 21))

        self.horizontalLayout_18.addWidget(self.Button_Models_Append)


        self.verticalLayout_244.addWidget(self.Frame_Models_Top)

        self.StackedWidget_Pages_Models = QStackedWidget(self.Page_Models)
        self.StackedWidget_Pages_Models.setObjectName(u"StackedWidget_Pages_Models")
        self.StackedWidget_Pages_Models.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.SubPage_Models_Process = QWidget()
        self.SubPage_Models_Process.setObjectName(u"SubPage_Models_Process")
        self.gridLayout_102 = QGridLayout(self.SubPage_Models_Process)
        self.gridLayout_102.setSpacing(12)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.gridLayout_102.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_Process = TabWidgetBase(self.SubPage_Models_Process)
        self.TabWidget_Models_Process.setObjectName(u"TabWidget_Models_Process")
        self.Tab_Models_Process_UVR = QWidget()
        self.Tab_Models_Process_UVR.setObjectName(u"Tab_Models_Process_UVR")
        self.verticalLayout_75 = QVBoxLayout(self.Tab_Models_Process_UVR)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_Process_UVR = Table_ViewModels(self.Tab_Models_Process_UVR)
        self.Table_Models_Process_UVR.setObjectName(u"Table_Models_Process_UVR")

        self.verticalLayout_75.addWidget(self.Table_Models_Process_UVR)

        self.TabWidget_Models_Process.addTab(self.Tab_Models_Process_UVR, "")

        self.gridLayout_102.addWidget(self.TabWidget_Models_Process, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_Process)
        self.SubPage_Models_VPR = QWidget()
        self.SubPage_Models_VPR.setObjectName(u"SubPage_Models_VPR")
        self.gridLayout_7 = QGridLayout(self.SubPage_Models_VPR)
        self.gridLayout_7.setSpacing(12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_VPR = TabWidgetBase(self.SubPage_Models_VPR)
        self.TabWidget_Models_VPR.setObjectName(u"TabWidget_Models_VPR")
        self.Tab_Models_VPR_TDNN = QWidget()
        self.Tab_Models_VPR_TDNN.setObjectName(u"Tab_Models_VPR_TDNN")
        self.verticalLayout_27 = QVBoxLayout(self.Tab_Models_VPR_TDNN)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_VPR_TDNN = Table_ViewModels(self.Tab_Models_VPR_TDNN)
        self.Table_Models_VPR_TDNN.setObjectName(u"Table_Models_VPR_TDNN")

        self.verticalLayout_27.addWidget(self.Table_Models_VPR_TDNN)

        self.TabWidget_Models_VPR.addTab(self.Tab_Models_VPR_TDNN, "")

        self.gridLayout_7.addWidget(self.TabWidget_Models_VPR, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_VPR)
        self.SubPage_Models_ASR = QWidget()
        self.SubPage_Models_ASR.setObjectName(u"SubPage_Models_ASR")
        self.gridLayout_11 = QGridLayout(self.SubPage_Models_ASR)
        self.gridLayout_11.setSpacing(12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_ASR = TabWidgetBase(self.SubPage_Models_ASR)
        self.TabWidget_Models_ASR.setObjectName(u"TabWidget_Models_ASR")
        self.Tab_Models_ASR_Whisper = QWidget()
        self.Tab_Models_ASR_Whisper.setObjectName(u"Tab_Models_ASR_Whisper")
        self.verticalLayout_46 = QVBoxLayout(self.Tab_Models_ASR_Whisper)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_ASR_Whisper = Table_ViewModels(self.Tab_Models_ASR_Whisper)
        self.Table_Models_ASR_Whisper.setObjectName(u"Table_Models_ASR_Whisper")

        self.verticalLayout_46.addWidget(self.Table_Models_ASR_Whisper)

        self.TabWidget_Models_ASR.addTab(self.Tab_Models_ASR_Whisper, "")

        self.gridLayout_11.addWidget(self.TabWidget_Models_ASR, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_ASR)
        self.SubPage_Models_TTS = QWidget()
        self.SubPage_Models_TTS.setObjectName(u"SubPage_Models_TTS")
        self.gridLayout_10 = QGridLayout(self.SubPage_Models_TTS)
        self.gridLayout_10.setSpacing(12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_TTS = TabWidgetBase(self.SubPage_Models_TTS)
        self.TabWidget_Models_TTS.setObjectName(u"TabWidget_Models_TTS")
        self.Tab_Models_TTS_GPTSoVITS = QWidget()
        self.Tab_Models_TTS_GPTSoVITS.setObjectName(u"Tab_Models_TTS_GPTSoVITS")
        self.verticalLayout_72 = QVBoxLayout(self.Tab_Models_TTS_GPTSoVITS)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_TTS_GPTSoVITS = Table_ViewModels(self.Tab_Models_TTS_GPTSoVITS)
        self.Table_Models_TTS_GPTSoVITS.setObjectName(u"Table_Models_TTS_GPTSoVITS")

        self.verticalLayout_72.addWidget(self.Table_Models_TTS_GPTSoVITS)

        self.TabWidget_Models_TTS.addTab(self.Tab_Models_TTS_GPTSoVITS, "")
        self.Tab_Models_TTS_VITS = QWidget()
        self.Tab_Models_TTS_VITS.setObjectName(u"Tab_Models_TTS_VITS")
        self.verticalLayout_38 = QVBoxLayout(self.Tab_Models_TTS_VITS)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_TTS_VITS = Table_ViewModels(self.Tab_Models_TTS_VITS)
        self.Table_Models_TTS_VITS.setObjectName(u"Table_Models_TTS_VITS")

        self.verticalLayout_38.addWidget(self.Table_Models_TTS_VITS)

        self.TabWidget_Models_TTS.addTab(self.Tab_Models_TTS_VITS, "")

        self.gridLayout_10.addWidget(self.TabWidget_Models_TTS, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_TTS)

        self.verticalLayout_244.addWidget(self.StackedWidget_Pages_Models)

        self.StackedWidget_Pages.addWidget(self.Page_Models)
        self.Page_Process = ToolPage()
        self.Page_Process.setObjectName(u"Page_Process")
        self.StackedWidget_Pages.addWidget(self.Page_Process)
        self.Page_VPR = QWidget()
        self.Page_VPR.setObjectName(u"Page_VPR")
        self.verticalLayout_44 = QVBoxLayout(self.Page_VPR)
        self.verticalLayout_44.setSpacing(21)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(21, 12, 21, 12)
        self.Frame_VPR_Top = QFrame(self.Page_VPR)
        self.Frame_VPR_Top.setObjectName(u"Frame_VPR_Top")
        self.Frame_VPR_Top.setMinimumSize(QSize(0, 60))
        self.Frame_VPR_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_53 = QHBoxLayout(self.Frame_VPR_Top)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Button_VoiceIdentifier_Title = NavigationButton(self.Frame_VPR_Top)
        self.Button_VoiceIdentifier_Title.setObjectName(u"Button_VoiceIdentifier_Title")
        sizePolicy1.setHeightForWidth(self.Button_VoiceIdentifier_Title.sizePolicy().hasHeightForWidth())
        self.Button_VoiceIdentifier_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_53.addWidget(self.Button_VoiceIdentifier_Title)

        self.HorizontalSpacer_VoiceIdentifier_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.HorizontalSpacer_VoiceIdentifier_Title)

        self.Button_VoiceIdentifier_Help = QPushButton(self.Frame_VPR_Top)
        self.Button_VoiceIdentifier_Help.setObjectName(u"Button_VoiceIdentifier_Help")
        self.Button_VoiceIdentifier_Help.setMinimumSize(QSize(45, 45))
        self.Button_VoiceIdentifier_Help.setStyleSheet(u"QPushButton {\n"
"	image-position: center;\n"
"	image: url(:/Button_Icon/images/icons/Question.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_53.addWidget(self.Button_VoiceIdentifier_Help)


        self.verticalLayout_44.addWidget(self.Frame_VPR_Top)

        self.StackedWidget_Pages_VPR = QStackedWidget(self.Page_VPR)
        self.StackedWidget_Pages_VPR.setObjectName(u"StackedWidget_Pages_VPR")
        self.StackedWidget_Pages_VPR.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_VPR_TDNN = QWidget()
        self.Subpage_VPR_TDNN.setObjectName(u"Subpage_VPR_TDNN")
        self.gridLayout_21 = QGridLayout(self.Subpage_VPR_TDNN)
        self.gridLayout_21.setSpacing(12)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_VPR_TDNN = QWidget(self.Subpage_VPR_TDNN)
        self.Widget_Left_VPR_TDNN.setObjectName(u"Widget_Left_VPR_TDNN")
        self.Widget_Left_VPR_TDNN.setMinimumSize(QSize(150, 0))
        self.Widget_Left_VPR_TDNN.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.Widget_Left_VPR_TDNN)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_VPR_TDNN = TreeWidgetBase(self.Widget_Left_VPR_TDNN)
        __qtreewidgetitem = QTreeWidgetItem(self.TreeWidget_Catalogue_VPR_TDNN)
        QTreeWidgetItem(__qtreewidgetitem)
        self.TreeWidget_Catalogue_VPR_TDNN.setObjectName(u"TreeWidget_Catalogue_VPR_TDNN")

        self.verticalLayout_4.addWidget(self.TreeWidget_Catalogue_VPR_TDNN)


        self.gridLayout_21.addWidget(self.Widget_Left_VPR_TDNN, 0, 0, 1, 1)

        self.ScrollArea_Middle_VPR_TDNN = ScrollAreaBase(self.Subpage_VPR_TDNN)
        self.ScrollArea_Middle_VPR_TDNN.setObjectName(u"ScrollArea_Middle_VPR_TDNN")
        self.ScrollArea_Middle_VPR_TDNN.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_VPR_TDNN.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_VPR_TDNN.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_VPR_TDNN = QWidget()
        self.ScrollArea_Middle_WidgetContents_VPR_TDNN.setObjectName(u"ScrollArea_Middle_WidgetContents_VPR_TDNN")
        self.ScrollArea_Middle_WidgetContents_VPR_TDNN.setGeometry(QRect(0, 0, 586, 983))
        self.verticalLayout_7 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_VPR_TDNN)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_VPR_TDNN_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_VPR_TDNN)
        self.GroupBox_VPR_TDNN_InputParams.setObjectName(u"GroupBox_VPR_TDNN_InputParams")
        self.verticalLayout_33 = QVBoxLayout(self.GroupBox_VPR_TDNN_InputParams)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 12, 0, 12)
        self.Frame_VPR_TDNN_InputParams_BasicSettings = QFrame(self.GroupBox_VPR_TDNN_InputParams)
        self.Frame_VPR_TDNN_InputParams_BasicSettings.setObjectName(u"Frame_VPR_TDNN_InputParams_BasicSettings")
        self.verticalLayout_137 = QVBoxLayout(self.Frame_VPR_TDNN_InputParams_BasicSettings)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.Frame_VPR_TDNN_AudioDirInput = QFrame(self.Frame_VPR_TDNN_InputParams_BasicSettings)
        self.Frame_VPR_TDNN_AudioDirInput.setObjectName(u"Frame_VPR_TDNN_AudioDirInput")
        self.Frame_VPR_TDNN_AudioDirInput.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_AudioDirInput.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_32 = QGridLayout(self.Frame_VPR_TDNN_AudioDirInput)
        self.gridLayout_32.setSpacing(12)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_AudioDirInput = LabelBase(self.Frame_VPR_TDNN_AudioDirInput)
        self.Label_VPR_TDNN_AudioDirInput.setObjectName(u"Label_VPR_TDNN_AudioDirInput")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_AudioDirInput.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_AudioDirInput.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_AudioDirInput.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_32.addWidget(self.Label_VPR_TDNN_AudioDirInput, 0, 0, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_AudioDirInput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.HorizontalSpacer_VPR_TDNN_AudioDirInput, 0, 1, 1, 1)

        self.Button_VPR_TDNN_AudioDirInput_MoreActions = MenuButton(self.Frame_VPR_TDNN_AudioDirInput)
        self.Button_VPR_TDNN_AudioDirInput_MoreActions.setObjectName(u"Button_VPR_TDNN_AudioDirInput_MoreActions")
        self.Button_VPR_TDNN_AudioDirInput_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_AudioDirInput_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_AudioDirInput_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_32.addWidget(self.Button_VPR_TDNN_AudioDirInput_MoreActions, 0, 2, 1, 1)

        self.LineEdit_VPR_TDNN_AudioDirInput = LineEditBase(self.Frame_VPR_TDNN_AudioDirInput)
        self.LineEdit_VPR_TDNN_AudioDirInput.setObjectName(u"LineEdit_VPR_TDNN_AudioDirInput")
        self.LineEdit_VPR_TDNN_AudioDirInput.setMinimumSize(QSize(0, 27))

        self.gridLayout_32.addWidget(self.LineEdit_VPR_TDNN_AudioDirInput, 1, 0, 1, 3)


        self.verticalLayout_137.addWidget(self.Frame_VPR_TDNN_AudioDirInput)

        self.Frame_VPR_TDNN_StdAudioSpeaker = QFrame(self.Frame_VPR_TDNN_InputParams_BasicSettings)
        self.Frame_VPR_TDNN_StdAudioSpeaker.setObjectName(u"Frame_VPR_TDNN_StdAudioSpeaker")
        self.Frame_VPR_TDNN_StdAudioSpeaker.setMinimumSize(QSize(0, 222))
        self.Frame_VPR_TDNN_StdAudioSpeaker.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.Frame_VPR_TDNN_StdAudioSpeaker)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_StdAudioSpeaker = LabelBase(self.Frame_VPR_TDNN_StdAudioSpeaker)
        self.Label_VPR_TDNN_StdAudioSpeaker.setObjectName(u"Label_VPR_TDNN_StdAudioSpeaker")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_StdAudioSpeaker.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_StdAudioSpeaker.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_StdAudioSpeaker.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_12.addWidget(self.Label_VPR_TDNN_StdAudioSpeaker)

        self.Table_VPR_TDNN_StdAudioSpeaker = Table_EditAudioSpeaker(self.Frame_VPR_TDNN_StdAudioSpeaker)
        self.Table_VPR_TDNN_StdAudioSpeaker.setObjectName(u"Table_VPR_TDNN_StdAudioSpeaker")

        self.verticalLayout_12.addWidget(self.Table_VPR_TDNN_StdAudioSpeaker)


        self.verticalLayout_137.addWidget(self.Frame_VPR_TDNN_StdAudioSpeaker)


        self.verticalLayout_33.addWidget(self.Frame_VPR_TDNN_InputParams_BasicSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_VPR_TDNN_InputParams)

        self.GroupBox_VPR_TDNN_VPRParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_VPR_TDNN)
        self.GroupBox_VPR_TDNN_VPRParams.setObjectName(u"GroupBox_VPR_TDNN_VPRParams")
        self.verticalLayout_47 = QVBoxLayout(self.GroupBox_VPR_TDNN_VPRParams)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 12, 0, 12)
        self.Frame_VPR_TDNN_VPRParams_BasicSettings = QFrame(self.GroupBox_VPR_TDNN_VPRParams)
        self.Frame_VPR_TDNN_VPRParams_BasicSettings.setObjectName(u"Frame_VPR_TDNN_VPRParams_BasicSettings")
        self.verticalLayout_45 = QVBoxLayout(self.Frame_VPR_TDNN_VPRParams_BasicSettings)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Frame_VPR_TDNN_DecisionThreshold = QFrame(self.Frame_VPR_TDNN_VPRParams_BasicSettings)
        self.Frame_VPR_TDNN_DecisionThreshold.setObjectName(u"Frame_VPR_TDNN_DecisionThreshold")
        self.Frame_VPR_TDNN_DecisionThreshold.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_DecisionThreshold.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_33 = QGridLayout(self.Frame_VPR_TDNN_DecisionThreshold)
        self.gridLayout_33.setSpacing(12)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_DecisionThreshold = LabelBase(self.Frame_VPR_TDNN_DecisionThreshold)
        self.Label_VPR_TDNN_DecisionThreshold.setObjectName(u"Label_VPR_TDNN_DecisionThreshold")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_DecisionThreshold.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_DecisionThreshold.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_DecisionThreshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_33.addWidget(self.Label_VPR_TDNN_DecisionThreshold, 0, 0, 1, 1)

        self.DoubleSpinBox_VPR_TDNN_DecisionThreshold = DoubleSpinBoxBase(self.Frame_VPR_TDNN_DecisionThreshold)
        self.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setObjectName(u"DoubleSpinBox_VPR_TDNN_DecisionThreshold")
        self.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setEnabled(True)
        self.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setMaximum(999999.000000000000000)

        self.gridLayout_33.addWidget(self.DoubleSpinBox_VPR_TDNN_DecisionThreshold, 1, 0, 1, 3)

        self.Button_VPR_TDNN_DecisionThreshold_MoreActions = MenuButton(self.Frame_VPR_TDNN_DecisionThreshold)
        self.Button_VPR_TDNN_DecisionThreshold_MoreActions.setObjectName(u"Button_VPR_TDNN_DecisionThreshold_MoreActions")
        self.Button_VPR_TDNN_DecisionThreshold_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_DecisionThreshold_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_DecisionThreshold_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_33.addWidget(self.Button_VPR_TDNN_DecisionThreshold_MoreActions, 0, 2, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_DecisionThreshold = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_33.addItem(self.HorizontalSpacer_VPR_TDNN_DecisionThreshold, 0, 1, 1, 1)


        self.verticalLayout_45.addWidget(self.Frame_VPR_TDNN_DecisionThreshold)

        self.Frame_VPR_TDNN_ModelPath = QFrame(self.Frame_VPR_TDNN_VPRParams_BasicSettings)
        self.Frame_VPR_TDNN_ModelPath.setObjectName(u"Frame_VPR_TDNN_ModelPath")
        self.Frame_VPR_TDNN_ModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_ModelPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_34 = QGridLayout(self.Frame_VPR_TDNN_ModelPath)
        self.gridLayout_34.setSpacing(12)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_ModelPath = LabelBase(self.Frame_VPR_TDNN_ModelPath)
        self.Label_VPR_TDNN_ModelPath.setObjectName(u"Label_VPR_TDNN_ModelPath")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_ModelPath.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_ModelPath.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_ModelPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_34.addWidget(self.Label_VPR_TDNN_ModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_ModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.HorizontalSpacer_VPR_TDNN_ModelPath, 0, 1, 1, 1)

        self.Button_VPR_TDNN_ModelPath_MoreActions = MenuButton(self.Frame_VPR_TDNN_ModelPath)
        self.Button_VPR_TDNN_ModelPath_MoreActions.setObjectName(u"Button_VPR_TDNN_ModelPath_MoreActions")
        self.Button_VPR_TDNN_ModelPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_ModelPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_ModelPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_34.addWidget(self.Button_VPR_TDNN_ModelPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_VPR_TDNN_ModelPath = LineEditBase(self.Frame_VPR_TDNN_ModelPath)
        self.LineEdit_VPR_TDNN_ModelPath.setObjectName(u"LineEdit_VPR_TDNN_ModelPath")
        self.LineEdit_VPR_TDNN_ModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_34.addWidget(self.LineEdit_VPR_TDNN_ModelPath, 1, 0, 1, 3)


        self.verticalLayout_45.addWidget(self.Frame_VPR_TDNN_ModelPath)


        self.verticalLayout_47.addWidget(self.Frame_VPR_TDNN_VPRParams_BasicSettings)

        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings = ToolBoxBase(self.GroupBox_VPR_TDNN_VPRParams)
        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings.setObjectName(u"ToolBox_VPR_TDNN_VPRParams_AdvanceSettings")
        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content")
        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 162, 315))
        self.verticalLayout_21 = QVBoxLayout(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Frame_VPR_TDNN_ModelType = QFrame(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content)
        self.Frame_VPR_TDNN_ModelType.setObjectName(u"Frame_VPR_TDNN_ModelType")
        self.Frame_VPR_TDNN_ModelType.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_ModelType.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_35 = QGridLayout(self.Frame_VPR_TDNN_ModelType)
        self.gridLayout_35.setSpacing(12)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_ModelType = LabelBase(self.Frame_VPR_TDNN_ModelType)
        self.Label_VPR_TDNN_ModelType.setObjectName(u"Label_VPR_TDNN_ModelType")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_ModelType.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_ModelType.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_ModelType.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_35.addWidget(self.Label_VPR_TDNN_ModelType, 0, 0, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_ModelType = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.HorizontalSpacer_VPR_TDNN_ModelType, 0, 1, 1, 1)

        self.Button_VPR_TDNN_ModelType_MoreActions = MenuButton(self.Frame_VPR_TDNN_ModelType)
        self.Button_VPR_TDNN_ModelType_MoreActions.setObjectName(u"Button_VPR_TDNN_ModelType_MoreActions")
        self.Button_VPR_TDNN_ModelType_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_ModelType_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_ModelType_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_35.addWidget(self.Button_VPR_TDNN_ModelType_MoreActions, 0, 2, 1, 1)

        self.ComboBox_VPR_TDNN_ModelType = ComboBoxBase(self.Frame_VPR_TDNN_ModelType)
        self.ComboBox_VPR_TDNN_ModelType.setObjectName(u"ComboBox_VPR_TDNN_ModelType")
        self.ComboBox_VPR_TDNN_ModelType.setMinimumSize(QSize(0, 27))

        self.gridLayout_35.addWidget(self.ComboBox_VPR_TDNN_ModelType, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_VPR_TDNN_ModelType)

        self.Frame_VPR_TDNN_FeatureMethod = QFrame(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content)
        self.Frame_VPR_TDNN_FeatureMethod.setObjectName(u"Frame_VPR_TDNN_FeatureMethod")
        self.Frame_VPR_TDNN_FeatureMethod.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_FeatureMethod.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_36 = QGridLayout(self.Frame_VPR_TDNN_FeatureMethod)
        self.gridLayout_36.setSpacing(12)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_FeatureMethod = LabelBase(self.Frame_VPR_TDNN_FeatureMethod)
        self.Label_VPR_TDNN_FeatureMethod.setObjectName(u"Label_VPR_TDNN_FeatureMethod")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_FeatureMethod.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_FeatureMethod.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_FeatureMethod.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_36.addWidget(self.Label_VPR_TDNN_FeatureMethod, 0, 0, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_FeatureMethod = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.HorizontalSpacer_VPR_TDNN_FeatureMethod, 0, 1, 1, 1)

        self.Button_VPR_TDNN_FeatureMethod_MoreActions = MenuButton(self.Frame_VPR_TDNN_FeatureMethod)
        self.Button_VPR_TDNN_FeatureMethod_MoreActions.setObjectName(u"Button_VPR_TDNN_FeatureMethod_MoreActions")
        self.Button_VPR_TDNN_FeatureMethod_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_FeatureMethod_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_FeatureMethod_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_36.addWidget(self.Button_VPR_TDNN_FeatureMethod_MoreActions, 0, 2, 1, 1)

        self.ComboBox_VPR_TDNN_FeatureMethod = ComboBoxBase(self.Frame_VPR_TDNN_FeatureMethod)
        self.ComboBox_VPR_TDNN_FeatureMethod.setObjectName(u"ComboBox_VPR_TDNN_FeatureMethod")
        self.ComboBox_VPR_TDNN_FeatureMethod.setMinimumSize(QSize(0, 27))

        self.gridLayout_36.addWidget(self.ComboBox_VPR_TDNN_FeatureMethod, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_VPR_TDNN_FeatureMethod)

        self.Frame_VPR_TDNN_DurationOfAudio = QFrame(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content)
        self.Frame_VPR_TDNN_DurationOfAudio.setObjectName(u"Frame_VPR_TDNN_DurationOfAudio")
        self.Frame_VPR_TDNN_DurationOfAudio.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_DurationOfAudio.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_37 = QGridLayout(self.Frame_VPR_TDNN_DurationOfAudio)
        self.gridLayout_37.setSpacing(12)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_DurationOfAudio = LabelBase(self.Frame_VPR_TDNN_DurationOfAudio)
        self.Label_VPR_TDNN_DurationOfAudio.setObjectName(u"Label_VPR_TDNN_DurationOfAudio")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_DurationOfAudio.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_DurationOfAudio.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_DurationOfAudio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_37.addWidget(self.Label_VPR_TDNN_DurationOfAudio, 0, 0, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_DurationOfAudio = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.HorizontalSpacer_VPR_TDNN_DurationOfAudio, 0, 1, 1, 1)

        self.Button_VPR_TDNN_DurationOfAudio_MoreActions = MenuButton(self.Frame_VPR_TDNN_DurationOfAudio)
        self.Button_VPR_TDNN_DurationOfAudio_MoreActions.setObjectName(u"Button_VPR_TDNN_DurationOfAudio_MoreActions")
        self.Button_VPR_TDNN_DurationOfAudio_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_DurationOfAudio_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_DurationOfAudio_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_37.addWidget(self.Button_VPR_TDNN_DurationOfAudio_MoreActions, 0, 2, 1, 1)

        self.DoubleSpinBox_VPR_TDNN_DurationOfAudio = DoubleSpinBoxBase(self.Frame_VPR_TDNN_DurationOfAudio)
        self.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setObjectName(u"DoubleSpinBox_VPR_TDNN_DurationOfAudio")
        self.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setEnabled(True)
        self.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setMaximum(999999.000000000000000)

        self.gridLayout_37.addWidget(self.DoubleSpinBox_VPR_TDNN_DurationOfAudio, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_VPR_TDNN_DurationOfAudio)

        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings.addItem(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_47.addWidget(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_VPR_TDNN_VPRParams)

        self.GroupBox_VPR_TDNN_OutputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_VPR_TDNN)
        self.GroupBox_VPR_TDNN_OutputParams.setObjectName(u"GroupBox_VPR_TDNN_OutputParams")
        self.verticalLayout_48 = QVBoxLayout(self.GroupBox_VPR_TDNN_OutputParams)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 12, 0, 12)
        self.Frame_VPR_TDNN_OutputParams_BasicSettings = QFrame(self.GroupBox_VPR_TDNN_OutputParams)
        self.Frame_VPR_TDNN_OutputParams_BasicSettings.setObjectName(u"Frame_VPR_TDNN_OutputParams_BasicSettings")
        self.verticalLayout_139 = QVBoxLayout(self.Frame_VPR_TDNN_OutputParams_BasicSettings)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.Frame_VPR_TDNN_OutputDirName = QFrame(self.Frame_VPR_TDNN_OutputParams_BasicSettings)
        self.Frame_VPR_TDNN_OutputDirName.setObjectName(u"Frame_VPR_TDNN_OutputDirName")
        self.Frame_VPR_TDNN_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_38 = QGridLayout(self.Frame_VPR_TDNN_OutputDirName)
        self.gridLayout_38.setSpacing(12)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_OutputDirName = LabelBase(self.Frame_VPR_TDNN_OutputDirName)
        self.Label_VPR_TDNN_OutputDirName.setObjectName(u"Label_VPR_TDNN_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_38.addWidget(self.Label_VPR_TDNN_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_VPR_TDNN_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.HorizontalSpacer_VPR_TDNN_OutputDirName, 0, 1, 1, 1)

        self.Button_VPR_TDNN_OutputDirName_MoreActions = MenuButton(self.Frame_VPR_TDNN_OutputDirName)
        self.Button_VPR_TDNN_OutputDirName_MoreActions.setObjectName(u"Button_VPR_TDNN_OutputDirName_MoreActions")
        self.Button_VPR_TDNN_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_38.addWidget(self.Button_VPR_TDNN_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_VPR_TDNN_OutputDirName = LineEditBase(self.Frame_VPR_TDNN_OutputDirName)
        self.LineEdit_VPR_TDNN_OutputDirName.setObjectName(u"LineEdit_VPR_TDNN_OutputDirName")
        self.LineEdit_VPR_TDNN_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_38.addWidget(self.LineEdit_VPR_TDNN_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_139.addWidget(self.Frame_VPR_TDNN_OutputDirName)


        self.verticalLayout_48.addWidget(self.Frame_VPR_TDNN_OutputParams_BasicSettings)

        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_VPR_TDNN_OutputParams)
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_VPR_TDNN_OutputParams_AdvanceSettings")
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 105))
        self.verticalLayout_110 = QVBoxLayout(self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.Frame_VPR_TDNN_AudioSpeakersDataName = QFrame(self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_VPR_TDNN_AudioSpeakersDataName.setObjectName(u"Frame_VPR_TDNN_AudioSpeakersDataName")
        self.Frame_VPR_TDNN_AudioSpeakersDataName.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_AudioSpeakersDataName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_112 = QGridLayout(self.Frame_VPR_TDNN_AudioSpeakersDataName)
        self.gridLayout_112.setSpacing(12)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.gridLayout_112.setContentsMargins(21, 12, 21, 12)
        self.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions = MenuButton(self.Frame_VPR_TDNN_AudioSpeakersDataName)
        self.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions.setObjectName(u"Button_VPR_TDNN_AudioSpeakersDataName_MoreActions")
        self.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_112.addWidget(self.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions, 0, 2, 1, 1)

        self.Label_VPR_TDNN_AudioSpeakersDataName = LabelBase(self.Frame_VPR_TDNN_AudioSpeakersDataName)
        self.Label_VPR_TDNN_AudioSpeakersDataName.setObjectName(u"Label_VPR_TDNN_AudioSpeakersDataName")
        sizePolicy5.setHeightForWidth(self.Label_VPR_TDNN_AudioSpeakersDataName.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_AudioSpeakersDataName.setSizePolicy(sizePolicy5)
        self.Label_VPR_TDNN_AudioSpeakersDataName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_112.addWidget(self.Label_VPR_TDNN_AudioSpeakersDataName, 0, 0, 1, 1)

        self.LineEdit_VPR_TDNN_AudioSpeakersDataName = LineEditBase(self.Frame_VPR_TDNN_AudioSpeakersDataName)
        self.LineEdit_VPR_TDNN_AudioSpeakersDataName.setObjectName(u"LineEdit_VPR_TDNN_AudioSpeakersDataName")
        self.LineEdit_VPR_TDNN_AudioSpeakersDataName.setMinimumSize(QSize(0, 27))

        self.gridLayout_112.addWidget(self.LineEdit_VPR_TDNN_AudioSpeakersDataName, 1, 0, 1, 3)

        self.HorizontalSpacer_VPR_TDNN_AudioSpeakersDataName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_112.addItem(self.HorizontalSpacer_VPR_TDNN_AudioSpeakersDataName, 0, 1, 1, 1)


        self.verticalLayout_110.addWidget(self.Frame_VPR_TDNN_AudioSpeakersDataName)

        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.addItem(self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_48.addWidget(self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_VPR_TDNN_OutputParams)

        self.ScrollArea_Middle_VPR_TDNN.setWidget(self.ScrollArea_Middle_WidgetContents_VPR_TDNN)

        self.gridLayout_21.addWidget(self.ScrollArea_Middle_VPR_TDNN, 0, 1, 1, 1)

        self.Widget_Right_VPR_TDNN = QWidget(self.Subpage_VPR_TDNN)
        self.Widget_Right_VPR_TDNN.setObjectName(u"Widget_Right_VPR_TDNN")
        self.Widget_Right_VPR_TDNN.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Widget_Right_VPR_TDNN)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_VPR_TDNN = TextBrowserBase(self.Widget_Right_VPR_TDNN)
        self.TextBrowser_Params_VPR_TDNN.setObjectName(u"TextBrowser_Params_VPR_TDNN")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_VPR_TDNN.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_VPR_TDNN.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_VPR_TDNN.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_2.addWidget(self.TextBrowser_Params_VPR_TDNN, 0, 0, 1, 3)

        self.Button_ResetSettings_VPR_TDNN = HollowButton(self.Widget_Right_VPR_TDNN)
        self.Button_ResetSettings_VPR_TDNN.setObjectName(u"Button_ResetSettings_VPR_TDNN")

        self.gridLayout_2.addWidget(self.Button_ResetSettings_VPR_TDNN, 1, 0, 1, 1)

        self.Button_ImportSettings_VPR_TDNN = HollowButton(self.Widget_Right_VPR_TDNN)
        self.Button_ImportSettings_VPR_TDNN.setObjectName(u"Button_ImportSettings_VPR_TDNN")

        self.gridLayout_2.addWidget(self.Button_ImportSettings_VPR_TDNN, 1, 1, 1, 1)

        self.Button_ExportSettings_VPR_TDNN = HollowButton(self.Widget_Right_VPR_TDNN)
        self.Button_ExportSettings_VPR_TDNN.setObjectName(u"Button_ExportSettings_VPR_TDNN")

        self.gridLayout_2.addWidget(self.Button_ExportSettings_VPR_TDNN, 1, 2, 1, 1)

        self.Button_EditResult_VPR_TDNN = HollowButton(self.Widget_Right_VPR_TDNN)
        self.Button_EditResult_VPR_TDNN.setObjectName(u"Button_EditResult_VPR_TDNN")

        self.gridLayout_2.addWidget(self.Button_EditResult_VPR_TDNN, 2, 0, 1, 3)

        self.Button_CheckOutput_VPR_TDNN = HollowButton(self.Widget_Right_VPR_TDNN)
        self.Button_CheckOutput_VPR_TDNN.setObjectName(u"Button_CheckOutput_VPR_TDNN")

        self.gridLayout_2.addWidget(self.Button_CheckOutput_VPR_TDNN, 3, 0, 1, 3)


        self.gridLayout_21.addWidget(self.Widget_Right_VPR_TDNN, 0, 2, 1, 1)

        self.ProgressBar_VPR_TDNN = ProgressBarBase(self.Subpage_VPR_TDNN)
        self.ProgressBar_VPR_TDNN.setObjectName(u"ProgressBar_VPR_TDNN")
        self.ProgressBar_VPR_TDNN.setMinimumSize(QSize(0, 30))
        self.ProgressBar_VPR_TDNN.setValue(0)
        self.ProgressBar_VPR_TDNN.setTextVisible(False)
        self.horizontalLayout_73 = QHBoxLayout(self.ProgressBar_VPR_TDNN)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_VPR_TDNN = QStackedWidget(self.ProgressBar_VPR_TDNN)
        self.StackedWidget_VPR_TDNN.setObjectName(u"StackedWidget_VPR_TDNN")
        self.StackedWidget_VPR_TDNN.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_VPR_TDNN.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_VPR_TDNN_Execute = QWidget()
        self.Page_VPR_TDNN_Execute.setObjectName(u"Page_VPR_TDNN_Execute")
        self.verticalLayout_102 = QVBoxLayout(self.Page_VPR_TDNN_Execute)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.Button_VPR_TDNN_Execute = HollowButton(self.Page_VPR_TDNN_Execute)
        self.Button_VPR_TDNN_Execute.setObjectName(u"Button_VPR_TDNN_Execute")
        sizePolicy2.setHeightForWidth(self.Button_VPR_TDNN_Execute.sizePolicy().hasHeightForWidth())
        self.Button_VPR_TDNN_Execute.setSizePolicy(sizePolicy2)
        self.Button_VPR_TDNN_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_102.addWidget(self.Button_VPR_TDNN_Execute)

        self.StackedWidget_VPR_TDNN.addWidget(self.Page_VPR_TDNN_Execute)
        self.Page_VPR_TDNN_Terminate = QWidget()
        self.Page_VPR_TDNN_Terminate.setObjectName(u"Page_VPR_TDNN_Terminate")
        self.verticalLayout_119 = QVBoxLayout(self.Page_VPR_TDNN_Terminate)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.Button_VPR_TDNN_Terminate = HollowButton(self.Page_VPR_TDNN_Terminate)
        self.Button_VPR_TDNN_Terminate.setObjectName(u"Button_VPR_TDNN_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_VPR_TDNN_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_VPR_TDNN_Terminate.setSizePolicy(sizePolicy2)
        self.Button_VPR_TDNN_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_119.addWidget(self.Button_VPR_TDNN_Terminate)

        self.StackedWidget_VPR_TDNN.addWidget(self.Page_VPR_TDNN_Terminate)

        self.horizontalLayout_73.addWidget(self.StackedWidget_VPR_TDNN)


        self.gridLayout_21.addWidget(self.ProgressBar_VPR_TDNN, 1, 0, 1, 3)

        self.gridLayout_21.setColumnStretch(0, 3)
        self.gridLayout_21.setColumnStretch(1, 10)
        self.gridLayout_21.setColumnStretch(2, 7)
        self.StackedWidget_Pages_VPR.addWidget(self.Subpage_VPR_TDNN)

        self.verticalLayout_44.addWidget(self.StackedWidget_Pages_VPR)

        self.StackedWidget_Pages.addWidget(self.Page_VPR)
        self.Page_ASR = QWidget()
        self.Page_ASR.setObjectName(u"Page_ASR")
        self.verticalLayout_41 = QVBoxLayout(self.Page_ASR)
        self.verticalLayout_41.setSpacing(21)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(21, 12, 21, 12)
        self.Frame_ASR_Top = QFrame(self.Page_ASR)
        self.Frame_ASR_Top.setObjectName(u"Frame_ASR_Top")
        self.Frame_ASR_Top.setMinimumSize(QSize(0, 60))
        self.Frame_ASR_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_55 = QHBoxLayout(self.Frame_ASR_Top)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Button_VoiceTranscriber_Title = NavigationButton(self.Frame_ASR_Top)
        self.Button_VoiceTranscriber_Title.setObjectName(u"Button_VoiceTranscriber_Title")
        sizePolicy1.setHeightForWidth(self.Button_VoiceTranscriber_Title.sizePolicy().hasHeightForWidth())
        self.Button_VoiceTranscriber_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_55.addWidget(self.Button_VoiceTranscriber_Title)

        self.HorizontalSpacer_VoiceTranscriber_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.HorizontalSpacer_VoiceTranscriber_Title)

        self.Button_VoiceTranscriber_Help = QPushButton(self.Frame_ASR_Top)
        self.Button_VoiceTranscriber_Help.setObjectName(u"Button_VoiceTranscriber_Help")
        self.Button_VoiceTranscriber_Help.setMinimumSize(QSize(45, 45))
        self.Button_VoiceTranscriber_Help.setStyleSheet(u"QPushButton {\n"
"	image-position: center;\n"
"	image: url(:/Button_Icon/images/icons/Question.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_55.addWidget(self.Button_VoiceTranscriber_Help)


        self.verticalLayout_41.addWidget(self.Frame_ASR_Top)

        self.StackedWidget_Pages_ASR = QStackedWidget(self.Page_ASR)
        self.StackedWidget_Pages_ASR.setObjectName(u"StackedWidget_Pages_ASR")
        self.StackedWidget_Pages_ASR.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_ASR_Whisper = QWidget()
        self.Subpage_ASR_Whisper.setObjectName(u"Subpage_ASR_Whisper")
        self.gridLayout_19 = QGridLayout(self.Subpage_ASR_Whisper)
        self.gridLayout_19.setSpacing(12)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_ASR_Whisper = QWidget(self.Subpage_ASR_Whisper)
        self.Widget_Left_ASR_Whisper.setObjectName(u"Widget_Left_ASR_Whisper")
        self.Widget_Left_ASR_Whisper.setMinimumSize(QSize(150, 0))
        self.Widget_Left_ASR_Whisper.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.Widget_Left_ASR_Whisper)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_ASR_Whisper = TreeWidgetBase(self.Widget_Left_ASR_Whisper)
        __qtreewidgetitem1 = QTreeWidgetItem(self.TreeWidget_Catalogue_ASR_Whisper)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.TreeWidget_Catalogue_ASR_Whisper.setObjectName(u"TreeWidget_Catalogue_ASR_Whisper")

        self.verticalLayout_8.addWidget(self.TreeWidget_Catalogue_ASR_Whisper)


        self.gridLayout_19.addWidget(self.Widget_Left_ASR_Whisper, 0, 0, 1, 1)

        self.ScrollArea_Middle_ASR_Whisper = ScrollAreaBase(self.Subpage_ASR_Whisper)
        self.ScrollArea_Middle_ASR_Whisper.setObjectName(u"ScrollArea_Middle_ASR_Whisper")
        self.ScrollArea_Middle_ASR_Whisper.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_ASR_Whisper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_ASR_Whisper.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_ASR_Whisper = QWidget()
        self.ScrollArea_Middle_WidgetContents_ASR_Whisper.setObjectName(u"ScrollArea_Middle_WidgetContents_ASR_Whisper")
        self.ScrollArea_Middle_WidgetContents_ASR_Whisper.setGeometry(QRect(0, 0, 586, 687))
        self.verticalLayout_16 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_ASR_Whisper)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_ASR_Whisper_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_ASR_Whisper)
        self.GroupBox_ASR_Whisper_InputParams.setObjectName(u"GroupBox_ASR_Whisper_InputParams")
        self.verticalLayout_32 = QVBoxLayout(self.GroupBox_ASR_Whisper_InputParams)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 12, 0, 12)
        self.Frame_ASR_Whisper_InputParams_BasicSettings = QFrame(self.GroupBox_ASR_Whisper_InputParams)
        self.Frame_ASR_Whisper_InputParams_BasicSettings.setObjectName(u"Frame_ASR_Whisper_InputParams_BasicSettings")
        self.verticalLayout_129 = QVBoxLayout(self.Frame_ASR_Whisper_InputParams_BasicSettings)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_Whisper_AudioDir = QFrame(self.Frame_ASR_Whisper_InputParams_BasicSettings)
        self.Frame_ASR_Whisper_AudioDir.setObjectName(u"Frame_ASR_Whisper_AudioDir")
        self.Frame_ASR_Whisper_AudioDir.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_AudioDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_39 = QGridLayout(self.Frame_ASR_Whisper_AudioDir)
        self.gridLayout_39.setSpacing(12)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_AudioDir = LabelBase(self.Frame_ASR_Whisper_AudioDir)
        self.Label_ASR_Whisper_AudioDir.setObjectName(u"Label_ASR_Whisper_AudioDir")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_AudioDir.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_AudioDir.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_AudioDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_39.addWidget(self.Label_ASR_Whisper_AudioDir, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_Whisper_AudioDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.HorizontalSpacer_ASR_Whisper_AudioDir, 0, 1, 1, 1)

        self.Button_ASR_Whisper_AudioDir_MoreActions = MenuButton(self.Frame_ASR_Whisper_AudioDir)
        self.Button_ASR_Whisper_AudioDir_MoreActions.setObjectName(u"Button_ASR_Whisper_AudioDir_MoreActions")
        self.Button_ASR_Whisper_AudioDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_AudioDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_AudioDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_39.addWidget(self.Button_ASR_Whisper_AudioDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_ASR_Whisper_AudioDir = LineEditBase(self.Frame_ASR_Whisper_AudioDir)
        self.LineEdit_ASR_Whisper_AudioDir.setObjectName(u"LineEdit_ASR_Whisper_AudioDir")
        self.LineEdit_ASR_Whisper_AudioDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_39.addWidget(self.LineEdit_ASR_Whisper_AudioDir, 1, 0, 1, 3)


        self.verticalLayout_129.addWidget(self.Frame_ASR_Whisper_AudioDir)


        self.verticalLayout_32.addWidget(self.Frame_ASR_Whisper_InputParams_BasicSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_ASR_Whisper_InputParams)

        self.GroupBox_ASR_Whisper_WhisperParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_ASR_Whisper)
        self.GroupBox_ASR_Whisper_WhisperParams.setObjectName(u"GroupBox_ASR_Whisper_WhisperParams")
        self.verticalLayout_49 = QVBoxLayout(self.GroupBox_ASR_Whisper_WhisperParams)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 12, 0, 12)
        self.Frame_ASR_Whisper_WhisperParams_BasicSettings = QFrame(self.GroupBox_ASR_Whisper_WhisperParams)
        self.Frame_ASR_Whisper_WhisperParams_BasicSettings.setObjectName(u"Frame_ASR_Whisper_WhisperParams_BasicSettings")
        self.verticalLayout_37 = QVBoxLayout(self.Frame_ASR_Whisper_WhisperParams_BasicSettings)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_Whisper_AddLanguageInfo = QFrame(self.Frame_ASR_Whisper_WhisperParams_BasicSettings)
        self.Frame_ASR_Whisper_AddLanguageInfo.setObjectName(u"Frame_ASR_Whisper_AddLanguageInfo")
        self.Frame_ASR_Whisper_AddLanguageInfo.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_AddLanguageInfo.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_40 = QGridLayout(self.Frame_ASR_Whisper_AddLanguageInfo)
        self.gridLayout_40.setSpacing(12)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_AddLanguageInfo = LabelBase(self.Frame_ASR_Whisper_AddLanguageInfo)
        self.Label_ASR_Whisper_AddLanguageInfo.setObjectName(u"Label_ASR_Whisper_AddLanguageInfo")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_AddLanguageInfo.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_AddLanguageInfo.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_AddLanguageInfo.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_40.addWidget(self.Label_ASR_Whisper_AddLanguageInfo, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_Whisper_AddLanguageInfo = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.HorizontalSpacer_ASR_Whisper_AddLanguageInfo, 0, 1, 1, 1)

        self.Button_ASR_Whisper_AddLanguageInfo_MoreActions = MenuButton(self.Frame_ASR_Whisper_AddLanguageInfo)
        self.Button_ASR_Whisper_AddLanguageInfo_MoreActions.setObjectName(u"Button_ASR_Whisper_AddLanguageInfo_MoreActions")
        self.Button_ASR_Whisper_AddLanguageInfo_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_AddLanguageInfo_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_AddLanguageInfo_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_40.addWidget(self.Button_ASR_Whisper_AddLanguageInfo_MoreActions, 0, 2, 1, 1)

        self.CheckBox_ASR_Whisper_AddLanguageInfo = CheckBoxBase(self.Frame_ASR_Whisper_AddLanguageInfo)
        self.CheckBox_ASR_Whisper_AddLanguageInfo.setObjectName(u"CheckBox_ASR_Whisper_AddLanguageInfo")
        self.CheckBox_ASR_Whisper_AddLanguageInfo.setMinimumSize(QSize(0, 27))

        self.gridLayout_40.addWidget(self.CheckBox_ASR_Whisper_AddLanguageInfo, 1, 0, 1, 3)


        self.verticalLayout_37.addWidget(self.Frame_ASR_Whisper_AddLanguageInfo)

        self.Frame_ASR_Whisper_ModelPath = QFrame(self.Frame_ASR_Whisper_WhisperParams_BasicSettings)
        self.Frame_ASR_Whisper_ModelPath.setObjectName(u"Frame_ASR_Whisper_ModelPath")
        self.Frame_ASR_Whisper_ModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_ModelPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_41 = QGridLayout(self.Frame_ASR_Whisper_ModelPath)
        self.gridLayout_41.setSpacing(12)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_ModelPath = LabelBase(self.Frame_ASR_Whisper_ModelPath)
        self.Label_ASR_Whisper_ModelPath.setObjectName(u"Label_ASR_Whisper_ModelPath")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_ModelPath.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_ModelPath.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_ModelPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_41.addWidget(self.Label_ASR_Whisper_ModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_Whisper_ModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_41.addItem(self.HorizontalSpacer_ASR_Whisper_ModelPath, 0, 1, 1, 1)

        self.Button_ASR_Whisper_ModelPath_MoreActions = MenuButton(self.Frame_ASR_Whisper_ModelPath)
        self.Button_ASR_Whisper_ModelPath_MoreActions.setObjectName(u"Button_ASR_Whisper_ModelPath_MoreActions")
        self.Button_ASR_Whisper_ModelPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_ModelPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_ModelPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_41.addWidget(self.Button_ASR_Whisper_ModelPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_ASR_Whisper_ModelPath = LineEditBase(self.Frame_ASR_Whisper_ModelPath)
        self.LineEdit_ASR_Whisper_ModelPath.setObjectName(u"LineEdit_ASR_Whisper_ModelPath")
        self.LineEdit_ASR_Whisper_ModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_41.addWidget(self.LineEdit_ASR_Whisper_ModelPath, 1, 0, 1, 3)


        self.verticalLayout_37.addWidget(self.Frame_ASR_Whisper_ModelPath)


        self.verticalLayout_49.addWidget(self.Frame_ASR_Whisper_WhisperParams_BasicSettings)

        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings = ToolBoxBase(self.GroupBox_ASR_Whisper_WhisperParams)
        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings.setObjectName(u"ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings")
        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content")
        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 315))
        self.verticalLayout_15 = QVBoxLayout(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_Whisper_fp16 = QFrame(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_Whisper_fp16.setObjectName(u"Frame_ASR_Whisper_fp16")
        self.Frame_ASR_Whisper_fp16.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_fp16.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_44 = QGridLayout(self.Frame_ASR_Whisper_fp16)
        self.gridLayout_44.setSpacing(12)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_fp16 = LabelBase(self.Frame_ASR_Whisper_fp16)
        self.Label_ASR_Whisper_fp16.setObjectName(u"Label_ASR_Whisper_fp16")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_fp16.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_fp16.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_fp16.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_44.addWidget(self.Label_ASR_Whisper_fp16, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_Whisper_fp16 = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.HorizontalSpacer_ASR_Whisper_fp16, 0, 1, 1, 1)

        self.CheckBox_ASR_Whisper_fp16 = CheckBoxBase(self.Frame_ASR_Whisper_fp16)
        self.CheckBox_ASR_Whisper_fp16.setObjectName(u"CheckBox_ASR_Whisper_fp16")
        self.CheckBox_ASR_Whisper_fp16.setMinimumSize(QSize(0, 27))

        self.gridLayout_44.addWidget(self.CheckBox_ASR_Whisper_fp16, 1, 0, 1, 3)

        self.Button_ASR_Whisper_fp16_MoreActions = MenuButton(self.Frame_ASR_Whisper_fp16)
        self.Button_ASR_Whisper_fp16_MoreActions.setObjectName(u"Button_ASR_Whisper_fp16_MoreActions")
        self.Button_ASR_Whisper_fp16_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_fp16_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_fp16_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_44.addWidget(self.Button_ASR_Whisper_fp16_MoreActions, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_ASR_Whisper_fp16)

        self.Frame_ASR_Whisper_ConditionOnPreviousText = QFrame(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_Whisper_ConditionOnPreviousText.setObjectName(u"Frame_ASR_Whisper_ConditionOnPreviousText")
        self.Frame_ASR_Whisper_ConditionOnPreviousText.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_ConditionOnPreviousText.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_43 = QGridLayout(self.Frame_ASR_Whisper_ConditionOnPreviousText)
        self.gridLayout_43.setSpacing(12)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(21, 12, 21, 12)
        self.CheckBox_ASR_Whisper_ConditionOnPreviousText = CheckBoxBase(self.Frame_ASR_Whisper_ConditionOnPreviousText)
        self.CheckBox_ASR_Whisper_ConditionOnPreviousText.setObjectName(u"CheckBox_ASR_Whisper_ConditionOnPreviousText")
        self.CheckBox_ASR_Whisper_ConditionOnPreviousText.setMinimumSize(QSize(0, 27))

        self.gridLayout_43.addWidget(self.CheckBox_ASR_Whisper_ConditionOnPreviousText, 1, 0, 1, 3)

        self.HorizontalSpacer_ASR_Whisper_ConditionOnPreviousText = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_43.addItem(self.HorizontalSpacer_ASR_Whisper_ConditionOnPreviousText, 0, 1, 1, 1)

        self.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions = MenuButton(self.Frame_ASR_Whisper_ConditionOnPreviousText)
        self.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions.setObjectName(u"Button_ASR_Whisper_ConditionOnPreviousText_MoreActions")
        self.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_43.addWidget(self.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions, 0, 2, 1, 1)

        self.Label_ASR_Whisper_ConditionOnPreviousText = LabelBase(self.Frame_ASR_Whisper_ConditionOnPreviousText)
        self.Label_ASR_Whisper_ConditionOnPreviousText.setObjectName(u"Label_ASR_Whisper_ConditionOnPreviousText")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_ConditionOnPreviousText.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_ConditionOnPreviousText.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_ConditionOnPreviousText.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_43.addWidget(self.Label_ASR_Whisper_ConditionOnPreviousText, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_ASR_Whisper_ConditionOnPreviousText)

        self.Frame_ASR_Whisper_Verbose = QFrame(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_Whisper_Verbose.setObjectName(u"Frame_ASR_Whisper_Verbose")
        self.Frame_ASR_Whisper_Verbose.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_Verbose.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_42 = QGridLayout(self.Frame_ASR_Whisper_Verbose)
        self.gridLayout_42.setSpacing(12)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_Verbose = LabelBase(self.Frame_ASR_Whisper_Verbose)
        self.Label_ASR_Whisper_Verbose.setObjectName(u"Label_ASR_Whisper_Verbose")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_Verbose.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_Verbose.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_Verbose.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_42.addWidget(self.Label_ASR_Whisper_Verbose, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_Whisper_Verbose = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_42.addItem(self.HorizontalSpacer_ASR_Whisper_Verbose, 0, 1, 1, 1)

        self.CheckBox_ASR_Whisper_Verbose = CheckBoxBase(self.Frame_ASR_Whisper_Verbose)
        self.CheckBox_ASR_Whisper_Verbose.setObjectName(u"CheckBox_ASR_Whisper_Verbose")
        self.CheckBox_ASR_Whisper_Verbose.setMinimumSize(QSize(0, 27))

        self.gridLayout_42.addWidget(self.CheckBox_ASR_Whisper_Verbose, 1, 0, 1, 3)

        self.Button_ASR_Whisper_Verbose_MoreActions = MenuButton(self.Frame_ASR_Whisper_Verbose)
        self.Button_ASR_Whisper_Verbose_MoreActions.setObjectName(u"Button_ASR_Whisper_Verbose_MoreActions")
        self.Button_ASR_Whisper_Verbose_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_Verbose_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_Verbose_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_42.addWidget(self.Button_ASR_Whisper_Verbose_MoreActions, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_ASR_Whisper_Verbose)

        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings.addItem(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_49.addWidget(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_ASR_Whisper_WhisperParams)

        self.GroupBox_ASR_Whisper_OutputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_ASR_Whisper)
        self.GroupBox_ASR_Whisper_OutputParams.setObjectName(u"GroupBox_ASR_Whisper_OutputParams")
        self.verticalLayout_89 = QVBoxLayout(self.GroupBox_ASR_Whisper_OutputParams)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 12, 0, 12)
        self.Frame_ASR_Whisper_OutputParams_BasicSettings = QFrame(self.GroupBox_ASR_Whisper_OutputParams)
        self.Frame_ASR_Whisper_OutputParams_BasicSettings.setObjectName(u"Frame_ASR_Whisper_OutputParams_BasicSettings")
        self.verticalLayout_135 = QVBoxLayout(self.Frame_ASR_Whisper_OutputParams_BasicSettings)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_Whisper_OutputDirName = QFrame(self.Frame_ASR_Whisper_OutputParams_BasicSettings)
        self.Frame_ASR_Whisper_OutputDirName.setObjectName(u"Frame_ASR_Whisper_OutputDirName")
        self.Frame_ASR_Whisper_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_Whisper_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_45 = QGridLayout(self.Frame_ASR_Whisper_OutputDirName)
        self.gridLayout_45.setSpacing(12)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_OutputDirName = LabelBase(self.Frame_ASR_Whisper_OutputDirName)
        self.Label_ASR_Whisper_OutputDirName.setObjectName(u"Label_ASR_Whisper_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_ASR_Whisper_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_ASR_Whisper_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_45.addWidget(self.Label_ASR_Whisper_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_Whisper_OutputDirName = QSpacerItem(481, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_45.addItem(self.HorizontalSpacer_ASR_Whisper_OutputDirName, 0, 1, 1, 1)

        self.Button_ASR_Whisper_OutputDirName_MoreActions = MenuButton(self.Frame_ASR_Whisper_OutputDirName)
        self.Button_ASR_Whisper_OutputDirName_MoreActions.setObjectName(u"Button_ASR_Whisper_OutputDirName_MoreActions")
        self.Button_ASR_Whisper_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_Whisper_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_Whisper_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_45.addWidget(self.Button_ASR_Whisper_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_ASR_Whisper_OutputDirName = LineEditBase(self.Frame_ASR_Whisper_OutputDirName)
        self.LineEdit_ASR_Whisper_OutputDirName.setObjectName(u"LineEdit_ASR_Whisper_OutputDirName")
        self.LineEdit_ASR_Whisper_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_45.addWidget(self.LineEdit_ASR_Whisper_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_135.addWidget(self.Frame_ASR_Whisper_OutputDirName)


        self.verticalLayout_89.addWidget(self.Frame_ASR_Whisper_OutputParams_BasicSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_ASR_Whisper_OutputParams)

        self.VerticalSpacer_ASR_Whisper = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.VerticalSpacer_ASR_Whisper)

        self.ScrollArea_Middle_ASR_Whisper.setWidget(self.ScrollArea_Middle_WidgetContents_ASR_Whisper)

        self.gridLayout_19.addWidget(self.ScrollArea_Middle_ASR_Whisper, 0, 1, 1, 1)

        self.Widget_Right_ASR_Whisper = QWidget(self.Subpage_ASR_Whisper)
        self.Widget_Right_ASR_Whisper.setObjectName(u"Widget_Right_ASR_Whisper")
        self.Widget_Right_ASR_Whisper.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.Widget_Right_ASR_Whisper)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_ASR_Whisper = TextBrowserBase(self.Widget_Right_ASR_Whisper)
        self.TextBrowser_Params_ASR_Whisper.setObjectName(u"TextBrowser_Params_ASR_Whisper")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_ASR_Whisper.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_ASR_Whisper.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_ASR_Whisper.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_4.addWidget(self.TextBrowser_Params_ASR_Whisper, 0, 0, 1, 3)

        self.Button_ResetSettings_ASR_Whisper = HollowButton(self.Widget_Right_ASR_Whisper)
        self.Button_ResetSettings_ASR_Whisper.setObjectName(u"Button_ResetSettings_ASR_Whisper")

        self.gridLayout_4.addWidget(self.Button_ResetSettings_ASR_Whisper, 1, 0, 1, 1)

        self.Button_ImportSettings_ASR_Whisper = HollowButton(self.Widget_Right_ASR_Whisper)
        self.Button_ImportSettings_ASR_Whisper.setObjectName(u"Button_ImportSettings_ASR_Whisper")

        self.gridLayout_4.addWidget(self.Button_ImportSettings_ASR_Whisper, 1, 1, 1, 1)

        self.Button_ExportSettings_ASR_Whisper = HollowButton(self.Widget_Right_ASR_Whisper)
        self.Button_ExportSettings_ASR_Whisper.setObjectName(u"Button_ExportSettings_ASR_Whisper")

        self.gridLayout_4.addWidget(self.Button_ExportSettings_ASR_Whisper, 1, 2, 1, 1)

        self.Button_CheckOutput_ASR_Whisper = HollowButton(self.Widget_Right_ASR_Whisper)
        self.Button_CheckOutput_ASR_Whisper.setObjectName(u"Button_CheckOutput_ASR_Whisper")

        self.gridLayout_4.addWidget(self.Button_CheckOutput_ASR_Whisper, 2, 0, 1, 3)


        self.gridLayout_19.addWidget(self.Widget_Right_ASR_Whisper, 0, 2, 1, 1)

        self.ProgressBar_ASR_Whisper = ProgressBarBase(self.Subpage_ASR_Whisper)
        self.ProgressBar_ASR_Whisper.setObjectName(u"ProgressBar_ASR_Whisper")
        self.ProgressBar_ASR_Whisper.setMinimumSize(QSize(0, 30))
        self.ProgressBar_ASR_Whisper.setValue(0)
        self.ProgressBar_ASR_Whisper.setTextVisible(False)
        self.horizontalLayout_35 = QHBoxLayout(self.ProgressBar_ASR_Whisper)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_ASR_Whisper = QStackedWidget(self.ProgressBar_ASR_Whisper)
        self.StackedWidget_ASR_Whisper.setObjectName(u"StackedWidget_ASR_Whisper")
        self.StackedWidget_ASR_Whisper.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_ASR_Whisper.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_ASR_Whisper_Execute = QWidget()
        self.Page_ASR_Whisper_Execute.setObjectName(u"Page_ASR_Whisper_Execute")
        self.verticalLayout_90 = QVBoxLayout(self.Page_ASR_Whisper_Execute)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Button_ASR_Whisper_Execute = HollowButton(self.Page_ASR_Whisper_Execute)
        self.Button_ASR_Whisper_Execute.setObjectName(u"Button_ASR_Whisper_Execute")
        sizePolicy2.setHeightForWidth(self.Button_ASR_Whisper_Execute.sizePolicy().hasHeightForWidth())
        self.Button_ASR_Whisper_Execute.setSizePolicy(sizePolicy2)
        self.Button_ASR_Whisper_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_90.addWidget(self.Button_ASR_Whisper_Execute)

        self.StackedWidget_ASR_Whisper.addWidget(self.Page_ASR_Whisper_Execute)
        self.Page_ASR_Whisper_Terminate = QWidget()
        self.Page_ASR_Whisper_Terminate.setObjectName(u"Page_ASR_Whisper_Terminate")
        self.verticalLayout_91 = QVBoxLayout(self.Page_ASR_Whisper_Terminate)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.Button_ASR_Whisper_Terminate = HollowButton(self.Page_ASR_Whisper_Terminate)
        self.Button_ASR_Whisper_Terminate.setObjectName(u"Button_ASR_Whisper_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_ASR_Whisper_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_ASR_Whisper_Terminate.setSizePolicy(sizePolicy2)
        self.Button_ASR_Whisper_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_91.addWidget(self.Button_ASR_Whisper_Terminate)

        self.StackedWidget_ASR_Whisper.addWidget(self.Page_ASR_Whisper_Terminate)

        self.horizontalLayout_35.addWidget(self.StackedWidget_ASR_Whisper)


        self.gridLayout_19.addWidget(self.ProgressBar_ASR_Whisper, 1, 0, 1, 3)

        self.gridLayout_19.setColumnStretch(0, 3)
        self.gridLayout_19.setColumnStretch(1, 10)
        self.gridLayout_19.setColumnStretch(2, 7)
        self.StackedWidget_Pages_ASR.addWidget(self.Subpage_ASR_Whisper)

        self.verticalLayout_41.addWidget(self.StackedWidget_Pages_ASR)

        self.StackedWidget_Pages.addWidget(self.Page_ASR)
        self.Page_Dataset = QWidget()
        self.Page_Dataset.setObjectName(u"Page_Dataset")
        self.verticalLayout_39 = QVBoxLayout(self.Page_Dataset)
        self.verticalLayout_39.setSpacing(21)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(21, 12, 21, 12)
        self.Frame_Dataset_Top = QFrame(self.Page_Dataset)
        self.Frame_Dataset_Top.setObjectName(u"Frame_Dataset_Top")
        self.Frame_Dataset_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Dataset_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.Frame_Dataset_Top)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Button_DatasetCreator_Title_GPTSoVITS = NavigationButton(self.Frame_Dataset_Top)
        self.Button_DatasetCreator_Title_GPTSoVITS.setObjectName(u"Button_DatasetCreator_Title_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.Button_DatasetCreator_Title_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.Button_DatasetCreator_Title_GPTSoVITS.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.Button_DatasetCreator_Title_GPTSoVITS)

        self.Button_DatasetCreator_Title_VITS = NavigationButton(self.Frame_Dataset_Top)
        self.Button_DatasetCreator_Title_VITS.setObjectName(u"Button_DatasetCreator_Title_VITS")
        sizePolicy1.setHeightForWidth(self.Button_DatasetCreator_Title_VITS.sizePolicy().hasHeightForWidth())
        self.Button_DatasetCreator_Title_VITS.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.Button_DatasetCreator_Title_VITS)

        self.HorizontalSpacer_DatasetCreator_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.HorizontalSpacer_DatasetCreator_Title)

        self.Button_DatasetCreator_Help = QPushButton(self.Frame_Dataset_Top)
        self.Button_DatasetCreator_Help.setObjectName(u"Button_DatasetCreator_Help")
        self.Button_DatasetCreator_Help.setMinimumSize(QSize(45, 45))
        self.Button_DatasetCreator_Help.setStyleSheet(u"QPushButton {\n"
"	image-position: center;\n"
"	image: url(:/Button_Icon/images/icons/Question.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_17.addWidget(self.Button_DatasetCreator_Help)


        self.verticalLayout_39.addWidget(self.Frame_Dataset_Top)

        self.StackedWidget_Pages_Dataset = QStackedWidget(self.Page_Dataset)
        self.StackedWidget_Pages_Dataset.setObjectName(u"StackedWidget_Pages_Dataset")
        self.StackedWidget_Pages_Dataset.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_DAT_GPTSoVITS = QWidget()
        self.Subpage_DAT_GPTSoVITS.setObjectName(u"Subpage_DAT_GPTSoVITS")
        self.gridLayout_108 = QGridLayout(self.Subpage_DAT_GPTSoVITS)
        self.gridLayout_108.setSpacing(12)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.gridLayout_108.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_DAT_GPTSoVITS = QWidget(self.Subpage_DAT_GPTSoVITS)
        self.Widget_Left_DAT_GPTSoVITS.setObjectName(u"Widget_Left_DAT_GPTSoVITS")
        self.Widget_Left_DAT_GPTSoVITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_DAT_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_62 = QVBoxLayout(self.Widget_Left_DAT_GPTSoVITS)
        self.verticalLayout_62.setSpacing(12)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_DAT_GPTSoVITS = TreeWidgetBase(self.Widget_Left_DAT_GPTSoVITS)
        __qtreewidgetitem2 = QTreeWidgetItem(self.TreeWidget_Catalogue_DAT_GPTSoVITS)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setObjectName(u"TreeWidget_Catalogue_DAT_GPTSoVITS")

        self.verticalLayout_62.addWidget(self.TreeWidget_Catalogue_DAT_GPTSoVITS)


        self.gridLayout_108.addWidget(self.Widget_Left_DAT_GPTSoVITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_DAT_GPTSoVITS = ScrollAreaBase(self.Subpage_DAT_GPTSoVITS)
        self.ScrollArea_Middle_DAT_GPTSoVITS.setObjectName(u"ScrollArea_Middle_DAT_GPTSoVITS")
        self.ScrollArea_Middle_DAT_GPTSoVITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_DAT_GPTSoVITS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_DAT_GPTSoVITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS.setObjectName(u"ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS")
        self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS.setGeometry(QRect(0, 0, 586, 689))
        self.verticalLayout_63 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.verticalLayout_63.setSpacing(12)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_DAT_GPTSoVITS_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.GroupBox_DAT_GPTSoVITS_InputParams.setObjectName(u"GroupBox_DAT_GPTSoVITS_InputParams")
        self.verticalLayout_123 = QVBoxLayout(self.GroupBox_DAT_GPTSoVITS_InputParams)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings = QFrame(self.GroupBox_DAT_GPTSoVITS_InputParams)
        self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings.setObjectName(u"Frame_DAT_GPTSoVITS_InputParams_BasicSettings")
        self.verticalLayout_64 = QVBoxLayout(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath = QFrame(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath.setObjectName(u"Frame_DAT_GPTSoVITS_AudioSpeakersDataPath")
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_82 = QGridLayout(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.gridLayout_82.setSpacing(12)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gridLayout_82.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath = LabelBase(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setObjectName(u"Label_DAT_GPTSoVITS_AudioSpeakersDataPath")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_82.addWidget(self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_InputParams = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_82.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_InputParams, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions")
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_82.addWidget(self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath = LineEditBase(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setObjectName(u"LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath")
        self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_82.addWidget(self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath, 1, 0, 1, 3)


        self.verticalLayout_64.addWidget(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)

        self.Frame_DAT_GPTSoVITS_SRTDir = QFrame(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_SRTDir.setObjectName(u"Frame_DAT_GPTSoVITS_SRTDir")
        self.Frame_DAT_GPTSoVITS_SRTDir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_SRTDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_83 = QGridLayout(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.gridLayout_83.setSpacing(12)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.gridLayout_83.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_SRTDir = LabelBase(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.Label_DAT_GPTSoVITS_SRTDir.setObjectName(u"Label_DAT_GPTSoVITS_SRTDir")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_SRTDir.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_SRTDir.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_SRTDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_83.addWidget(self.Label_DAT_GPTSoVITS_SRTDir, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_SRTDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_83.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_SRTDir, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_SRTDir_MoreActions")
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_83.addWidget(self.Button_DAT_GPTSoVITS_SRTDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_SRTDir = LineEditBase(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.LineEdit_DAT_GPTSoVITS_SRTDir.setObjectName(u"LineEdit_DAT_GPTSoVITS_SRTDir")
        self.LineEdit_DAT_GPTSoVITS_SRTDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_83.addWidget(self.LineEdit_DAT_GPTSoVITS_SRTDir, 1, 0, 1, 3)


        self.verticalLayout_64.addWidget(self.Frame_DAT_GPTSoVITS_SRTDir)


        self.verticalLayout_123.addWidget(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)


        self.verticalLayout_63.addWidget(self.GroupBox_DAT_GPTSoVITS_InputParams)

        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setObjectName(u"GroupBox_DAT_GPTSoVITS_GPTSoVITSParams")
        self.verticalLayout_124 = QVBoxLayout(self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings = QFrame(self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams)
        self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings.setObjectName(u"Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings")
        self.verticalLayout_65 = QVBoxLayout(self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_DataFormat = QFrame(self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_DataFormat.setObjectName(u"Frame_DAT_GPTSoVITS_DataFormat")
        self.Frame_DAT_GPTSoVITS_DataFormat.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_DataFormat.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_84 = QGridLayout(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.gridLayout_84.setSpacing(12)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_84.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_DataFormat = LabelBase(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.Label_DAT_GPTSoVITS_DataFormat.setObjectName(u"Label_DAT_GPTSoVITS_DataFormat")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_DataFormat.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_DataFormat.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_DataFormat.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_84.addWidget(self.Label_DAT_GPTSoVITS_DataFormat, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_DataFormat = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_84.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_DataFormat, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_DataFormat_MoreActions")
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_84.addWidget(self.Button_DAT_GPTSoVITS_DataFormat_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_DataFormat = LineEditBase(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.LineEdit_DAT_GPTSoVITS_DataFormat.setObjectName(u"LineEdit_DAT_GPTSoVITS_DataFormat")
        self.LineEdit_DAT_GPTSoVITS_DataFormat.setMinimumSize(QSize(0, 27))

        self.gridLayout_84.addWidget(self.LineEdit_DAT_GPTSoVITS_DataFormat, 1, 0, 1, 3)


        self.verticalLayout_65.addWidget(self.Frame_DAT_GPTSoVITS_DataFormat)


        self.verticalLayout_124.addWidget(self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings)


        self.verticalLayout_63.addWidget(self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams)

        self.GroupBox_DAT_GPTSoVITS_OutputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.GroupBox_DAT_GPTSoVITS_OutputParams.setObjectName(u"GroupBox_DAT_GPTSoVITS_OutputParams")
        self.verticalLayout_109 = QVBoxLayout(self.GroupBox_DAT_GPTSoVITS_OutputParams)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings = QFrame(self.GroupBox_DAT_GPTSoVITS_OutputParams)
        self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings.setObjectName(u"Frame_DAT_GPTSoVITS_OutputParams_BasicSettings")
        self.verticalLayout_68 = QVBoxLayout(self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_OutputDirName = QFrame(self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_OutputDirName.setObjectName(u"Frame_DAT_GPTSoVITS_OutputDirName")
        self.Frame_DAT_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_104 = QGridLayout(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.gridLayout_104.setSpacing(12)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.gridLayout_104.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_OutputDirName = LabelBase(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.Label_DAT_GPTSoVITS_OutputDirName.setObjectName(u"Label_DAT_GPTSoVITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_104.addWidget(self.Label_DAT_GPTSoVITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_104.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_OutputDirName, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_OutputDirName_MoreActions")
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_104.addWidget(self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_OutputDirName = LineEditBase(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.LineEdit_DAT_GPTSoVITS_OutputDirName.setObjectName(u"LineEdit_DAT_GPTSoVITS_OutputDirName")
        self.LineEdit_DAT_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_104.addWidget(self.LineEdit_DAT_GPTSoVITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_68.addWidget(self.Frame_DAT_GPTSoVITS_OutputDirName)


        self.verticalLayout_109.addWidget(self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings)

        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_DAT_GPTSoVITS_OutputParams)
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings")
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 105))
        self.verticalLayout_108 = QVBoxLayout(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_FileListName = QFrame(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_GPTSoVITS_FileListName.setObjectName(u"Frame_DAT_GPTSoVITS_FileListName")
        self.Frame_DAT_GPTSoVITS_FileListName.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_FileListName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_105 = QGridLayout(self.Frame_DAT_GPTSoVITS_FileListName)
        self.gridLayout_105.setSpacing(12)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.gridLayout_105.setContentsMargins(21, 12, 21, 12)
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_FileListName)
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_FileListName_MoreActions")
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_105.addWidget(self.Button_DAT_GPTSoVITS_FileListName_MoreActions, 0, 2, 1, 1)

        self.Label_DAT_GPTSoVITS_FileListName = LabelBase(self.Frame_DAT_GPTSoVITS_FileListName)
        self.Label_DAT_GPTSoVITS_FileListName.setObjectName(u"Label_DAT_GPTSoVITS_FileListName")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_FileListName.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_FileListName.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_FileListName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_105.addWidget(self.Label_DAT_GPTSoVITS_FileListName, 0, 0, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_FileListName = LineEditBase(self.Frame_DAT_GPTSoVITS_FileListName)
        self.LineEdit_DAT_GPTSoVITS_FileListName.setObjectName(u"LineEdit_DAT_GPTSoVITS_FileListName")
        self.LineEdit_DAT_GPTSoVITS_FileListName.setMinimumSize(QSize(0, 27))

        self.gridLayout_105.addWidget(self.LineEdit_DAT_GPTSoVITS_FileListName, 1, 0, 1, 3)

        self.HorizontalSpacer_DAT_GPTSoVITS_FileListName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_105.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_FileListName, 0, 1, 1, 1)


        self.verticalLayout_108.addWidget(self.Frame_DAT_GPTSoVITS_FileListName)

        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_109.addWidget(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings)


        self.verticalLayout_63.addWidget(self.GroupBox_DAT_GPTSoVITS_OutputParams)

        self.VerticalSpacer_DAT_GPTSoVITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.VerticalSpacer_DAT_GPTSoVITS)

        self.ScrollArea_Middle_DAT_GPTSoVITS.setWidget(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)

        self.gridLayout_108.addWidget(self.ScrollArea_Middle_DAT_GPTSoVITS, 0, 1, 1, 1)

        self.Widget_Right_DAT_GPTSoVITS = QWidget(self.Subpage_DAT_GPTSoVITS)
        self.Widget_Right_DAT_GPTSoVITS.setObjectName(u"Widget_Right_DAT_GPTSoVITS")
        self.Widget_Right_DAT_GPTSoVITS.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.Widget_Right_DAT_GPTSoVITS)
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_DAT_GPTSoVITS = TextBrowserBase(self.Widget_Right_DAT_GPTSoVITS)
        self.TextBrowser_Params_DAT_GPTSoVITS.setObjectName(u"TextBrowser_Params_DAT_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_DAT_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_DAT_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_DAT_GPTSoVITS.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_5.addWidget(self.TextBrowser_Params_DAT_GPTSoVITS, 0, 0, 1, 3)

        self.Button_ResetSettings_DAT_GPTSoVITS = HollowButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_ResetSettings_DAT_GPTSoVITS.setObjectName(u"Button_ResetSettings_DAT_GPTSoVITS")

        self.gridLayout_5.addWidget(self.Button_ResetSettings_DAT_GPTSoVITS, 1, 0, 1, 1)

        self.Button_ImportSettings_DAT_GPTSoVITS = HollowButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_ImportSettings_DAT_GPTSoVITS.setObjectName(u"Button_ImportSettings_DAT_GPTSoVITS")

        self.gridLayout_5.addWidget(self.Button_ImportSettings_DAT_GPTSoVITS, 1, 1, 1, 1)

        self.Button_ExportSettings_DAT_GPTSoVITS = HollowButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_ExportSettings_DAT_GPTSoVITS.setObjectName(u"Button_ExportSettings_DAT_GPTSoVITS")

        self.gridLayout_5.addWidget(self.Button_ExportSettings_DAT_GPTSoVITS, 1, 2, 1, 1)

        self.Button_CheckOutput_DAT_GPTSoVITS = HollowButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_CheckOutput_DAT_GPTSoVITS.setObjectName(u"Button_CheckOutput_DAT_GPTSoVITS")

        self.gridLayout_5.addWidget(self.Button_CheckOutput_DAT_GPTSoVITS, 2, 0, 1, 3)


        self.gridLayout_108.addWidget(self.Widget_Right_DAT_GPTSoVITS, 0, 2, 1, 1)

        self.ProgressBar_DAT_GPTSoVITS = ProgressBarBase(self.Subpage_DAT_GPTSoVITS)
        self.ProgressBar_DAT_GPTSoVITS.setObjectName(u"ProgressBar_DAT_GPTSoVITS")
        self.ProgressBar_DAT_GPTSoVITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_DAT_GPTSoVITS.setValue(0)
        self.ProgressBar_DAT_GPTSoVITS.setTextVisible(False)
        self.horizontalLayout_42 = QHBoxLayout(self.ProgressBar_DAT_GPTSoVITS)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_DAT_GPTSoVITS = QStackedWidget(self.ProgressBar_DAT_GPTSoVITS)
        self.StackedWidget_DAT_GPTSoVITS.setObjectName(u"StackedWidget_DAT_GPTSoVITS")
        self.StackedWidget_DAT_GPTSoVITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_DAT_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_DAT_GPTSoVITS_Execute = QWidget()
        self.Page_DAT_GPTSoVITS_Execute.setObjectName(u"Page_DAT_GPTSoVITS_Execute")
        self.verticalLayout_101 = QVBoxLayout(self.Page_DAT_GPTSoVITS_Execute)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_GPTSoVITS_Execute = HollowButton(self.Page_DAT_GPTSoVITS_Execute)
        self.Button_DAT_GPTSoVITS_Execute.setObjectName(u"Button_DAT_GPTSoVITS_Execute")
        sizePolicy2.setHeightForWidth(self.Button_DAT_GPTSoVITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_DAT_GPTSoVITS_Execute.setSizePolicy(sizePolicy2)
        self.Button_DAT_GPTSoVITS_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_101.addWidget(self.Button_DAT_GPTSoVITS_Execute)

        self.StackedWidget_DAT_GPTSoVITS.addWidget(self.Page_DAT_GPTSoVITS_Execute)
        self.Page_DAT_GPTSoVITS_Terminate = QWidget()
        self.Page_DAT_GPTSoVITS_Terminate.setObjectName(u"Page_DAT_GPTSoVITS_Terminate")
        self.verticalLayout_103 = QVBoxLayout(self.Page_DAT_GPTSoVITS_Terminate)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_GPTSoVITS_Terminate = HollowButton(self.Page_DAT_GPTSoVITS_Terminate)
        self.Button_DAT_GPTSoVITS_Terminate.setObjectName(u"Button_DAT_GPTSoVITS_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_DAT_GPTSoVITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_DAT_GPTSoVITS_Terminate.setSizePolicy(sizePolicy2)
        self.Button_DAT_GPTSoVITS_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_103.addWidget(self.Button_DAT_GPTSoVITS_Terminate)

        self.StackedWidget_DAT_GPTSoVITS.addWidget(self.Page_DAT_GPTSoVITS_Terminate)

        self.horizontalLayout_42.addWidget(self.StackedWidget_DAT_GPTSoVITS)


        self.gridLayout_108.addWidget(self.ProgressBar_DAT_GPTSoVITS, 1, 0, 1, 3)

        self.gridLayout_108.setColumnStretch(0, 3)
        self.gridLayout_108.setColumnStretch(1, 10)
        self.gridLayout_108.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Dataset.addWidget(self.Subpage_DAT_GPTSoVITS)
        self.Subpage_DAT_VITS = QWidget()
        self.Subpage_DAT_VITS.setObjectName(u"Subpage_DAT_VITS")
        self.gridLayout_8 = QGridLayout(self.Subpage_DAT_VITS)
        self.gridLayout_8.setSpacing(12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_DAT_VITS = QWidget(self.Subpage_DAT_VITS)
        self.Widget_Left_DAT_VITS.setObjectName(u"Widget_Left_DAT_VITS")
        self.Widget_Left_DAT_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_DAT_VITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.Widget_Left_DAT_VITS)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_DAT_VITS = TreeWidgetBase(self.Widget_Left_DAT_VITS)
        __qtreewidgetitem3 = QTreeWidgetItem(self.TreeWidget_Catalogue_DAT_VITS)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.TreeWidget_Catalogue_DAT_VITS.setObjectName(u"TreeWidget_Catalogue_DAT_VITS")

        self.verticalLayout_9.addWidget(self.TreeWidget_Catalogue_DAT_VITS)


        self.gridLayout_8.addWidget(self.Widget_Left_DAT_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_DAT_VITS = ScrollAreaBase(self.Subpage_DAT_VITS)
        self.ScrollArea_Middle_DAT_VITS.setObjectName(u"ScrollArea_Middle_DAT_VITS")
        self.ScrollArea_Middle_DAT_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_DAT_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_DAT_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_DAT_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_DAT_VITS")
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setGeometry(QRect(0, 0, 586, 985))
        self.verticalLayout_36 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.verticalLayout_36.setSpacing(12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_DAT_VITS_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_InputParams.setObjectName(u"GroupBox_DAT_VITS_InputParams")
        self.verticalLayout_111 = QVBoxLayout(self.GroupBox_DAT_VITS_InputParams)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_InputParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_InputParams)
        self.Frame_DAT_VITS_InputParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_InputParams_BasicSettings")
        self.verticalLayout_29 = QVBoxLayout(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_AudioSpeakersDataPath = QFrame(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.Frame_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"Frame_DAT_VITS_AudioSpeakersDataPath")
        self.Frame_DAT_VITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AudioSpeakersDataPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_46 = QGridLayout(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.gridLayout_46.setSpacing(12)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AudioSpeakersDataPath = LabelBase(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.Label_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"Label_DAT_VITS_AudioSpeakersDataPath")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_AudioSpeakersDataPath.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AudioSpeakersDataPath.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_AudioSpeakersDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_46.addWidget(self.Label_DAT_VITS_AudioSpeakersDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_InputParams = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.HorizontalSpacer_DAT_VITS_InputParams, 0, 1, 1, 1)

        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions = MenuButton(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setObjectName(u"Button_DAT_VITS_AudioSpeakersDataPath_MoreActions")
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_46.addWidget(self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_AudioSpeakersDataPath = LineEditBase(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.LineEdit_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"LineEdit_DAT_VITS_AudioSpeakersDataPath")
        self.LineEdit_DAT_VITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_46.addWidget(self.LineEdit_DAT_VITS_AudioSpeakersDataPath, 1, 0, 1, 3)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_AudioSpeakersDataPath)

        self.Frame_DAT_VITS_SRTDir = QFrame(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.Frame_DAT_VITS_SRTDir.setObjectName(u"Frame_DAT_VITS_SRTDir")
        self.Frame_DAT_VITS_SRTDir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SRTDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_47 = QGridLayout(self.Frame_DAT_VITS_SRTDir)
        self.gridLayout_47.setSpacing(12)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SRTDir = LabelBase(self.Frame_DAT_VITS_SRTDir)
        self.Label_DAT_VITS_SRTDir.setObjectName(u"Label_DAT_VITS_SRTDir")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_SRTDir.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SRTDir.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_SRTDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_47.addWidget(self.Label_DAT_VITS_SRTDir, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SRTDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.HorizontalSpacer_DAT_VITS_SRTDir, 0, 1, 1, 1)

        self.Button_DAT_VITS_SRTDir_MoreActions = MenuButton(self.Frame_DAT_VITS_SRTDir)
        self.Button_DAT_VITS_SRTDir_MoreActions.setObjectName(u"Button_DAT_VITS_SRTDir_MoreActions")
        self.Button_DAT_VITS_SRTDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRTDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRTDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_47.addWidget(self.Button_DAT_VITS_SRTDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_SRTDir = LineEditBase(self.Frame_DAT_VITS_SRTDir)
        self.LineEdit_DAT_VITS_SRTDir.setObjectName(u"LineEdit_DAT_VITS_SRTDir")
        self.LineEdit_DAT_VITS_SRTDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_47.addWidget(self.LineEdit_DAT_VITS_SRTDir, 1, 0, 1, 3)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_SRTDir)


        self.verticalLayout_111.addWidget(self.Frame_DAT_VITS_InputParams_BasicSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_InputParams)

        self.GroupBox_DAT_VITS_VITSParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_VITSParams.setObjectName(u"GroupBox_DAT_VITS_VITSParams")
        self.verticalLayout_115 = QVBoxLayout(self.GroupBox_DAT_VITS_VITSParams)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_VITSParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_VITSParams)
        self.Frame_DAT_VITS_VITSParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_VITSParams_BasicSettings")
        self.verticalLayout_30 = QVBoxLayout(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_DataFormat = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_DataFormat.setObjectName(u"Frame_DAT_VITS_DataFormat")
        self.Frame_DAT_VITS_DataFormat.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_DataFormat.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_76 = QGridLayout(self.Frame_DAT_VITS_DataFormat)
        self.gridLayout_76.setSpacing(12)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_76.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_DataFormat = LabelBase(self.Frame_DAT_VITS_DataFormat)
        self.Label_DAT_VITS_DataFormat.setObjectName(u"Label_DAT_VITS_DataFormat")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_DataFormat.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_DataFormat.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_DataFormat.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_76.addWidget(self.Label_DAT_VITS_DataFormat, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_DataFormat = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_76.addItem(self.HorizontalSpacer_DAT_VITS_DataFormat, 0, 1, 1, 1)

        self.Button_DAT_VITS_DataFormat_MoreActions = MenuButton(self.Frame_DAT_VITS_DataFormat)
        self.Button_DAT_VITS_DataFormat_MoreActions.setObjectName(u"Button_DAT_VITS_DataFormat_MoreActions")
        self.Button_DAT_VITS_DataFormat_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_DataFormat_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_DataFormat_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_76.addWidget(self.Button_DAT_VITS_DataFormat_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_DataFormat = LineEditBase(self.Frame_DAT_VITS_DataFormat)
        self.LineEdit_DAT_VITS_DataFormat.setObjectName(u"LineEdit_DAT_VITS_DataFormat")
        self.LineEdit_DAT_VITS_DataFormat.setMinimumSize(QSize(0, 27))

        self.gridLayout_76.addWidget(self.LineEdit_DAT_VITS_DataFormat, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_DataFormat)

        self.Frame_DAT_VITS_AddAuxiliaryData = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_AddAuxiliaryData.setObjectName(u"Frame_DAT_VITS_AddAuxiliaryData")
        self.Frame_DAT_VITS_AddAuxiliaryData.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_48 = QGridLayout(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.gridLayout_48.setSpacing(12)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AddAuxiliaryData = LabelBase(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.Label_DAT_VITS_AddAuxiliaryData.setObjectName(u"Label_DAT_VITS_AddAuxiliaryData")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_AddAuxiliaryData.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AddAuxiliaryData.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_48.addWidget(self.Label_DAT_VITS_AddAuxiliaryData, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_AddAuxiliaryData = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.HorizontalSpacer_DAT_VITS_AddAuxiliaryData, 0, 1, 1, 1)

        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions = MenuButton(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setObjectName(u"Button_DAT_VITS_AddAuxiliaryData_MoreActions")
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_48.addWidget(self.Button_DAT_VITS_AddAuxiliaryData_MoreActions, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_AddAuxiliaryData = CheckBoxBase(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setObjectName(u"CheckBox_DAT_VITS_AddAuxiliaryData")
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setMinimumSize(QSize(0, 27))

        self.gridLayout_48.addWidget(self.CheckBox_DAT_VITS_AddAuxiliaryData, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_AddAuxiliaryData)

        self.Frame_DAT_VITS_AuxiliaryDataPath = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_AuxiliaryDataPath.setObjectName(u"Frame_DAT_VITS_AuxiliaryDataPath")
        self.Frame_DAT_VITS_AuxiliaryDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AuxiliaryDataPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_53 = QGridLayout(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.gridLayout_53.setSpacing(12)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AuxiliaryDataPath = LabelBase(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.Label_DAT_VITS_AuxiliaryDataPath.setObjectName(u"Label_DAT_VITS_AuxiliaryDataPath")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_AuxiliaryDataPath.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AuxiliaryDataPath.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_AuxiliaryDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_53.addWidget(self.Label_DAT_VITS_AuxiliaryDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_AuxiliaryDataPath = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.HorizontalSpacer_DAT_VITS_AuxiliaryDataPath, 0, 1, 1, 1)

        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions = MenuButton(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setObjectName(u"Button_DAT_VITS_AuxiliaryDataPath_MoreActions")
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_53.addWidget(self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_AuxiliaryDataPath = LineEditBase(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.LineEdit_DAT_VITS_AuxiliaryDataPath.setObjectName(u"LineEdit_DAT_VITS_AuxiliaryDataPath")
        self.LineEdit_DAT_VITS_AuxiliaryDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_53.addWidget(self.LineEdit_DAT_VITS_AuxiliaryDataPath, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_AuxiliaryDataPath)


        self.verticalLayout_115.addWidget(self.Frame_DAT_VITS_VITSParams_BasicSettings)

        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_DAT_VITS_VITSParams)
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setObjectName(u"ToolBox_DAT_VITS_VITSParams_AdvanceSettings")
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 162, 420))
        self.verticalLayout_53 = QVBoxLayout(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_TrainRatio = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_TrainRatio.setObjectName(u"Frame_DAT_VITS_TrainRatio")
        self.Frame_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_TrainRatio.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_49 = QGridLayout(self.Frame_DAT_VITS_TrainRatio)
        self.gridLayout_49.setSpacing(12)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_TrainRatio = LabelBase(self.Frame_DAT_VITS_TrainRatio)
        self.Label_DAT_VITS_TrainRatio.setObjectName(u"Label_DAT_VITS_TrainRatio")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_TrainRatio.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_TrainRatio.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_TrainRatio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_49.addWidget(self.Label_DAT_VITS_TrainRatio, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_TrainRatio = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_49.addItem(self.HorizontalSpacer_DAT_VITS_TrainRatio, 0, 1, 1, 1)

        self.Button_DAT_VITS_TrainRatio_MoreActions = MenuButton(self.Frame_DAT_VITS_TrainRatio)
        self.Button_DAT_VITS_TrainRatio_MoreActions.setObjectName(u"Button_DAT_VITS_TrainRatio_MoreActions")
        self.Button_DAT_VITS_TrainRatio_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_TrainRatio_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_TrainRatio_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_49.addWidget(self.Button_DAT_VITS_TrainRatio_MoreActions, 0, 2, 1, 1)

        self.DoubleSpinBox_DAT_VITS_TrainRatio = DoubleSpinBoxBase(self.Frame_DAT_VITS_TrainRatio)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setObjectName(u"DoubleSpinBox_DAT_VITS_TrainRatio")
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setEnabled(True)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMaximum(999999.000000000000000)

        self.gridLayout_49.addWidget(self.DoubleSpinBox_DAT_VITS_TrainRatio, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_TrainRatio)

        self.Frame_DAT_VITS_SampleRate = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_SampleRate.setObjectName(u"Frame_DAT_VITS_SampleRate")
        self.Frame_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleRate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_50 = QGridLayout(self.Frame_DAT_VITS_SampleRate)
        self.gridLayout_50.setSpacing(12)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SampleRate = LabelBase(self.Frame_DAT_VITS_SampleRate)
        self.Label_DAT_VITS_SampleRate.setObjectName(u"Label_DAT_VITS_SampleRate")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_SampleRate.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SampleRate.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_SampleRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_50.addWidget(self.Label_DAT_VITS_SampleRate, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SampleRate = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.HorizontalSpacer_DAT_VITS_SampleRate, 0, 1, 1, 1)

        self.Button_DAT_VITS_SampleRate_MoreActions = MenuButton(self.Frame_DAT_VITS_SampleRate)
        self.Button_DAT_VITS_SampleRate_MoreActions.setObjectName(u"Button_DAT_VITS_SampleRate_MoreActions")
        self.Button_DAT_VITS_SampleRate_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleRate_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleRate_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_50.addWidget(self.Button_DAT_VITS_SampleRate_MoreActions, 0, 2, 1, 1)

        self.ComboBox_DAT_VITS_SampleRate = ComboBoxBase(self.Frame_DAT_VITS_SampleRate)
        self.ComboBox_DAT_VITS_SampleRate.setObjectName(u"ComboBox_DAT_VITS_SampleRate")
        self.ComboBox_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 27))

        self.gridLayout_50.addWidget(self.ComboBox_DAT_VITS_SampleRate, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_SampleRate)

        self.Frame_DAT_VITS_SampleWidth = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_SampleWidth.setObjectName(u"Frame_DAT_VITS_SampleWidth")
        self.Frame_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleWidth.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_51 = QGridLayout(self.Frame_DAT_VITS_SampleWidth)
        self.gridLayout_51.setSpacing(12)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SampleWidth = LabelBase(self.Frame_DAT_VITS_SampleWidth)
        self.Label_DAT_VITS_SampleWidth.setObjectName(u"Label_DAT_VITS_SampleWidth")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_SampleWidth.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SampleWidth.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_SampleWidth.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_51.addWidget(self.Label_DAT_VITS_SampleWidth, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SampleWidth = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.HorizontalSpacer_DAT_VITS_SampleWidth, 0, 1, 1, 1)

        self.Button_DAT_VITS_SampleWidth_MoreActions = MenuButton(self.Frame_DAT_VITS_SampleWidth)
        self.Button_DAT_VITS_SampleWidth_MoreActions.setObjectName(u"Button_DAT_VITS_SampleWidth_MoreActions")
        self.Button_DAT_VITS_SampleWidth_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleWidth_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleWidth_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_51.addWidget(self.Button_DAT_VITS_SampleWidth_MoreActions, 0, 2, 1, 1)

        self.ComboBox_DAT_VITS_SampleWidth = ComboBoxBase(self.Frame_DAT_VITS_SampleWidth)
        self.ComboBox_DAT_VITS_SampleWidth.setObjectName(u"ComboBox_DAT_VITS_SampleWidth")
        self.ComboBox_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 27))

        self.gridLayout_51.addWidget(self.ComboBox_DAT_VITS_SampleWidth, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_SampleWidth)

        self.Frame_DAT_VITS_ToMono = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_ToMono.setObjectName(u"Frame_DAT_VITS_ToMono")
        self.Frame_DAT_VITS_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_ToMono.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_52 = QGridLayout(self.Frame_DAT_VITS_ToMono)
        self.gridLayout_52.setSpacing(12)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_ToMono = LabelBase(self.Frame_DAT_VITS_ToMono)
        self.Label_DAT_VITS_ToMono.setObjectName(u"Label_DAT_VITS_ToMono")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_ToMono.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_ToMono.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_ToMono.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_52.addWidget(self.Label_DAT_VITS_ToMono, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_ToMono = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.HorizontalSpacer_DAT_VITS_ToMono, 0, 1, 1, 1)

        self.Button_DAT_VITS_ToMono_MoreActions = MenuButton(self.Frame_DAT_VITS_ToMono)
        self.Button_DAT_VITS_ToMono_MoreActions.setObjectName(u"Button_DAT_VITS_ToMono_MoreActions")
        self.Button_DAT_VITS_ToMono_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToMono_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToMono_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_52.addWidget(self.Button_DAT_VITS_ToMono_MoreActions, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_ToMono = CheckBoxBase(self.Frame_DAT_VITS_ToMono)
        self.CheckBox_DAT_VITS_ToMono.setObjectName(u"CheckBox_DAT_VITS_ToMono")
        self.CheckBox_DAT_VITS_ToMono.setMinimumSize(QSize(0, 27))

        self.gridLayout_52.addWidget(self.CheckBox_DAT_VITS_ToMono, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_ToMono)

        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.addItem(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_115.addWidget(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_VITSParams)

        self.GroupBox_DAT_VITS_OutputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_OutputParams.setObjectName(u"GroupBox_DAT_VITS_OutputParams")
        self.verticalLayout_107 = QVBoxLayout(self.GroupBox_DAT_VITS_OutputParams)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_OutputParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_OutputParams)
        self.Frame_DAT_VITS_OutputParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_OutputParams_BasicSettings")
        self.verticalLayout_31 = QVBoxLayout(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_OutputDirName = QFrame(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.Frame_DAT_VITS_OutputDirName.setObjectName(u"Frame_DAT_VITS_OutputDirName")
        self.Frame_DAT_VITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_54 = QGridLayout(self.Frame_DAT_VITS_OutputDirName)
        self.gridLayout_54.setSpacing(12)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_OutputDirName = LabelBase(self.Frame_DAT_VITS_OutputDirName)
        self.Label_DAT_VITS_OutputDirName.setObjectName(u"Label_DAT_VITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_54.addWidget(self.Label_DAT_VITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.HorizontalSpacer_DAT_VITS_OutputDirName, 0, 1, 1, 1)

        self.Button_DAT_VITS_OutputDirName_MoreActions = MenuButton(self.Frame_DAT_VITS_OutputDirName)
        self.Button_DAT_VITS_OutputDirName_MoreActions.setObjectName(u"Button_DAT_VITS_OutputDirName_MoreActions")
        self.Button_DAT_VITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_54.addWidget(self.Button_DAT_VITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_OutputDirName = LineEditBase(self.Frame_DAT_VITS_OutputDirName)
        self.LineEdit_DAT_VITS_OutputDirName.setObjectName(u"LineEdit_DAT_VITS_OutputDirName")
        self.LineEdit_DAT_VITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_54.addWidget(self.LineEdit_DAT_VITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_31.addWidget(self.Frame_DAT_VITS_OutputDirName)


        self.verticalLayout_107.addWidget(self.Frame_DAT_VITS_OutputParams_BasicSettings)

        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_DAT_VITS_OutputParams)
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_DAT_VITS_OutputParams_AdvanceSettings")
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 210))
        self.verticalLayout_88 = QVBoxLayout(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_FileListNameTraining = QFrame(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_FileListNameTraining.setObjectName(u"Frame_DAT_VITS_FileListNameTraining")
        self.Frame_DAT_VITS_FileListNameTraining.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileListNameTraining.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_55 = QGridLayout(self.Frame_DAT_VITS_FileListNameTraining)
        self.gridLayout_55.setSpacing(12)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(21, 12, 21, 12)
        self.Button_DAT_VITS_FileListNameTraining_MoreActions = MenuButton(self.Frame_DAT_VITS_FileListNameTraining)
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setObjectName(u"Button_DAT_VITS_FileListNameTraining_MoreActions")
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_55.addWidget(self.Button_DAT_VITS_FileListNameTraining_MoreActions, 0, 2, 1, 1)

        self.Label_DAT_VITS_FileListNameTraining = LabelBase(self.Frame_DAT_VITS_FileListNameTraining)
        self.Label_DAT_VITS_FileListNameTraining.setObjectName(u"Label_DAT_VITS_FileListNameTraining")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_FileListNameTraining.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileListNameTraining.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_FileListNameTraining.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_55.addWidget(self.Label_DAT_VITS_FileListNameTraining, 0, 0, 1, 1)

        self.LineEdit_DAT_VITS_FileListNameTraining = LineEditBase(self.Frame_DAT_VITS_FileListNameTraining)
        self.LineEdit_DAT_VITS_FileListNameTraining.setObjectName(u"LineEdit_DAT_VITS_FileListNameTraining")
        self.LineEdit_DAT_VITS_FileListNameTraining.setMinimumSize(QSize(0, 27))

        self.gridLayout_55.addWidget(self.LineEdit_DAT_VITS_FileListNameTraining, 1, 0, 1, 3)

        self.HorizontalSpacer_DAT_VITS_FileListNameTraining = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.HorizontalSpacer_DAT_VITS_FileListNameTraining, 0, 1, 1, 1)


        self.verticalLayout_88.addWidget(self.Frame_DAT_VITS_FileListNameTraining)

        self.Frame_DAT_VITS_FileListNameValidation = QFrame(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_FileListNameValidation.setObjectName(u"Frame_DAT_VITS_FileListNameValidation")
        self.Frame_DAT_VITS_FileListNameValidation.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileListNameValidation.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_56 = QGridLayout(self.Frame_DAT_VITS_FileListNameValidation)
        self.gridLayout_56.setSpacing(12)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_FileListNameValidation = LabelBase(self.Frame_DAT_VITS_FileListNameValidation)
        self.Label_DAT_VITS_FileListNameValidation.setObjectName(u"Label_DAT_VITS_FileListNameValidation")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_FileListNameValidation.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileListNameValidation.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_FileListNameValidation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_56.addWidget(self.Label_DAT_VITS_FileListNameValidation, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_FileListNameValidation = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.HorizontalSpacer_DAT_VITS_FileListNameValidation, 0, 1, 1, 1)

        self.Button_DAT_VITS_FileListNameValidation_MoreActions = MenuButton(self.Frame_DAT_VITS_FileListNameValidation)
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setObjectName(u"Button_DAT_VITS_FileListNameValidation_MoreActions")
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_56.addWidget(self.Button_DAT_VITS_FileListNameValidation_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_FileListNameValidation = LineEditBase(self.Frame_DAT_VITS_FileListNameValidation)
        self.LineEdit_DAT_VITS_FileListNameValidation.setObjectName(u"LineEdit_DAT_VITS_FileListNameValidation")
        self.LineEdit_DAT_VITS_FileListNameValidation.setMinimumSize(QSize(0, 27))

        self.gridLayout_56.addWidget(self.LineEdit_DAT_VITS_FileListNameValidation, 1, 0, 1, 3)


        self.verticalLayout_88.addWidget(self.Frame_DAT_VITS_FileListNameValidation)

        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_107.addWidget(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_OutputParams)

        self.VerticalSpacer_DAT_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.VerticalSpacer_DAT_VITS)

        self.ScrollArea_Middle_DAT_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_DAT_VITS)

        self.gridLayout_8.addWidget(self.ScrollArea_Middle_DAT_VITS, 0, 1, 1, 1)

        self.Widget_Right_DAT_VITS = QWidget(self.Subpage_DAT_VITS)
        self.Widget_Right_DAT_VITS.setObjectName(u"Widget_Right_DAT_VITS")
        self.Widget_Right_DAT_VITS.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_9 = QGridLayout(self.Widget_Right_DAT_VITS)
        self.gridLayout_9.setSpacing(12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_DAT_VITS = TextBrowserBase(self.Widget_Right_DAT_VITS)
        self.TextBrowser_Params_DAT_VITS.setObjectName(u"TextBrowser_Params_DAT_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_DAT_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_DAT_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_DAT_VITS.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_9.addWidget(self.TextBrowser_Params_DAT_VITS, 0, 0, 1, 3)

        self.Button_ResetSettings_DAT_VITS = HollowButton(self.Widget_Right_DAT_VITS)
        self.Button_ResetSettings_DAT_VITS.setObjectName(u"Button_ResetSettings_DAT_VITS")

        self.gridLayout_9.addWidget(self.Button_ResetSettings_DAT_VITS, 1, 0, 1, 1)

        self.Button_ImportSettings_DAT_VITS = HollowButton(self.Widget_Right_DAT_VITS)
        self.Button_ImportSettings_DAT_VITS.setObjectName(u"Button_ImportSettings_DAT_VITS")

        self.gridLayout_9.addWidget(self.Button_ImportSettings_DAT_VITS, 1, 1, 1, 1)

        self.Button_ExportSettings_DAT_VITS = HollowButton(self.Widget_Right_DAT_VITS)
        self.Button_ExportSettings_DAT_VITS.setObjectName(u"Button_ExportSettings_DAT_VITS")

        self.gridLayout_9.addWidget(self.Button_ExportSettings_DAT_VITS, 1, 2, 1, 1)

        self.Button_CheckOutput_DAT_VITS = HollowButton(self.Widget_Right_DAT_VITS)
        self.Button_CheckOutput_DAT_VITS.setObjectName(u"Button_CheckOutput_DAT_VITS")

        self.gridLayout_9.addWidget(self.Button_CheckOutput_DAT_VITS, 2, 0, 1, 3)


        self.gridLayout_8.addWidget(self.Widget_Right_DAT_VITS, 0, 2, 1, 1)

        self.ProgressBar_DAT_VITS = ProgressBarBase(self.Subpage_DAT_VITS)
        self.ProgressBar_DAT_VITS.setObjectName(u"ProgressBar_DAT_VITS")
        self.ProgressBar_DAT_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_DAT_VITS.setValue(0)
        self.ProgressBar_DAT_VITS.setTextVisible(False)
        self.horizontalLayout_37 = QHBoxLayout(self.ProgressBar_DAT_VITS)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_DAT_VITS = QStackedWidget(self.ProgressBar_DAT_VITS)
        self.StackedWidget_DAT_VITS.setObjectName(u"StackedWidget_DAT_VITS")
        self.StackedWidget_DAT_VITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_DAT_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_DAT_VITS_Execute = QWidget()
        self.Page_DAT_VITS_Execute.setObjectName(u"Page_DAT_VITS_Execute")
        self.verticalLayout_92 = QVBoxLayout(self.Page_DAT_VITS_Execute)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_VITS_Execute = HollowButton(self.Page_DAT_VITS_Execute)
        self.Button_DAT_VITS_Execute.setObjectName(u"Button_DAT_VITS_Execute")
        sizePolicy2.setHeightForWidth(self.Button_DAT_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_DAT_VITS_Execute.setSizePolicy(sizePolicy2)
        self.Button_DAT_VITS_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_92.addWidget(self.Button_DAT_VITS_Execute)

        self.StackedWidget_DAT_VITS.addWidget(self.Page_DAT_VITS_Execute)
        self.Page_DAT_VITS_Terminate = QWidget()
        self.Page_DAT_VITS_Terminate.setObjectName(u"Page_DAT_VITS_Terminate")
        self.verticalLayout_93 = QVBoxLayout(self.Page_DAT_VITS_Terminate)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_VITS_Terminate = HollowButton(self.Page_DAT_VITS_Terminate)
        self.Button_DAT_VITS_Terminate.setObjectName(u"Button_DAT_VITS_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_DAT_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_DAT_VITS_Terminate.setSizePolicy(sizePolicy2)
        self.Button_DAT_VITS_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_93.addWidget(self.Button_DAT_VITS_Terminate)

        self.StackedWidget_DAT_VITS.addWidget(self.Page_DAT_VITS_Terminate)

        self.horizontalLayout_37.addWidget(self.StackedWidget_DAT_VITS)


        self.gridLayout_8.addWidget(self.ProgressBar_DAT_VITS, 1, 0, 1, 3)

        self.gridLayout_8.setColumnStretch(0, 3)
        self.gridLayout_8.setColumnStretch(1, 10)
        self.gridLayout_8.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Dataset.addWidget(self.Subpage_DAT_VITS)

        self.verticalLayout_39.addWidget(self.StackedWidget_Pages_Dataset)

        self.StackedWidget_Pages.addWidget(self.Page_Dataset)
        self.Page_Train = QWidget()
        self.Page_Train.setObjectName(u"Page_Train")
        self.verticalLayout_43 = QVBoxLayout(self.Page_Train)
        self.verticalLayout_43.setSpacing(21)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(21, 12, 21, 12)
        self.Frame_Train_Top = QFrame(self.Page_Train)
        self.Frame_Train_Top.setObjectName(u"Frame_Train_Top")
        self.Frame_Train_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Train_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.Frame_Train_Top)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Button_VoiceTrainer_Title_GPTSoVITS = NavigationButton(self.Frame_Train_Top)
        self.Button_VoiceTrainer_Title_GPTSoVITS.setObjectName(u"Button_VoiceTrainer_Title_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.Button_VoiceTrainer_Title_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.Button_VoiceTrainer_Title_GPTSoVITS.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.Button_VoiceTrainer_Title_GPTSoVITS)

        self.Button_VoiceTrainer_Title_VITS = NavigationButton(self.Frame_Train_Top)
        self.Button_VoiceTrainer_Title_VITS.setObjectName(u"Button_VoiceTrainer_Title_VITS")
        sizePolicy1.setHeightForWidth(self.Button_VoiceTrainer_Title_VITS.sizePolicy().hasHeightForWidth())
        self.Button_VoiceTrainer_Title_VITS.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.Button_VoiceTrainer_Title_VITS)

        self.HorizontalSpacer_VoiceTrainer_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.HorizontalSpacer_VoiceTrainer_Title)

        self.Button_VoiceTrainer_Help = QPushButton(self.Frame_Train_Top)
        self.Button_VoiceTrainer_Help.setObjectName(u"Button_VoiceTrainer_Help")
        self.Button_VoiceTrainer_Help.setMinimumSize(QSize(45, 45))
        self.Button_VoiceTrainer_Help.setStyleSheet(u"QPushButton {\n"
"	image-position: center;\n"
"	image: url(:/Button_Icon/images/icons/Question.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_15.addWidget(self.Button_VoiceTrainer_Help)


        self.verticalLayout_43.addWidget(self.Frame_Train_Top)

        self.StackedWidget_Pages_Train = QStackedWidget(self.Page_Train)
        self.StackedWidget_Pages_Train.setObjectName(u"StackedWidget_Pages_Train")
        self.StackedWidget_Pages_Train.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_Train_GPTSoVITS = QWidget()
        self.Subpage_Train_GPTSoVITS.setObjectName(u"Subpage_Train_GPTSoVITS")
        self.gridLayout_85 = QGridLayout(self.Subpage_Train_GPTSoVITS)
        self.gridLayout_85.setSpacing(12)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.gridLayout_85.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Train_GPTSoVITS = QWidget(self.Subpage_Train_GPTSoVITS)
        self.Widget_Left_Train_GPTSoVITS.setObjectName(u"Widget_Left_Train_GPTSoVITS")
        self.Widget_Left_Train_GPTSoVITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Train_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_59 = QVBoxLayout(self.Widget_Left_Train_GPTSoVITS)
        self.verticalLayout_59.setSpacing(12)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Train_GPTSoVITS = TreeWidgetBase(self.Widget_Left_Train_GPTSoVITS)
        __qtreewidgetitem4 = QTreeWidgetItem(self.TreeWidget_Catalogue_Train_GPTSoVITS)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setObjectName(u"TreeWidget_Catalogue_Train_GPTSoVITS")

        self.verticalLayout_59.addWidget(self.TreeWidget_Catalogue_Train_GPTSoVITS)


        self.gridLayout_85.addWidget(self.Widget_Left_Train_GPTSoVITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_Train_GPTSoVITS = ScrollAreaBase(self.Subpage_Train_GPTSoVITS)
        self.ScrollArea_Middle_Train_GPTSoVITS.setObjectName(u"ScrollArea_Middle_Train_GPTSoVITS")
        self.ScrollArea_Middle_Train_GPTSoVITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Train_GPTSoVITS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Train_GPTSoVITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS.setObjectName(u"ScrollArea_Middle_WidgetContents_Train_GPTSoVITS")
        self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS.setGeometry(QRect(0, 0, 586, 1088))
        self.verticalLayout_52 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.verticalLayout_52.setSpacing(12)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Train_GPTSoVITS_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.GroupBox_Train_GPTSoVITS_InputParams.setObjectName(u"GroupBox_Train_GPTSoVITS_InputParams")
        self.verticalLayout_121 = QVBoxLayout(self.GroupBox_Train_GPTSoVITS_InputParams)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_GPTSoVITS_InputParams_BasicSettings = QFrame(self.GroupBox_Train_GPTSoVITS_InputParams)
        self.Frame_Train_GPTSoVITS_InputParams_BasicSettings.setObjectName(u"Frame_Train_GPTSoVITS_InputParams_BasicSettings")
        self.verticalLayout_55 = QVBoxLayout(self.Frame_Train_GPTSoVITS_InputParams_BasicSettings)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_FileListPath = QFrame(self.Frame_Train_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_FileListPath.setObjectName(u"Frame_Train_GPTSoVITS_FileListPath")
        self.Frame_Train_GPTSoVITS_FileListPath.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_FileListPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_81 = QGridLayout(self.Frame_Train_GPTSoVITS_FileListPath)
        self.gridLayout_81.setSpacing(12)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_FileListPath = LabelBase(self.Frame_Train_GPTSoVITS_FileListPath)
        self.Label_Train_GPTSoVITS_FileListPath.setObjectName(u"Label_Train_GPTSoVITS_FileListPath")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_FileListPath.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_FileListPath.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_FileListPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_81.addWidget(self.Label_Train_GPTSoVITS_FileListPath, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_FileListPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_81.addItem(self.HorizontalSpacer_Train_GPTSoVITS_FileListPath, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_FileListPath_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_FileListPath)
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_FileListPath_MoreActions")
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_81.addWidget(self.Button_Train_GPTSoVITS_FileListPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_FileListPath = LineEditBase(self.Frame_Train_GPTSoVITS_FileListPath)
        self.LineEdit_Train_GPTSoVITS_FileListPath.setObjectName(u"LineEdit_Train_GPTSoVITS_FileListPath")
        self.LineEdit_Train_GPTSoVITS_FileListPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_81.addWidget(self.LineEdit_Train_GPTSoVITS_FileListPath, 1, 0, 1, 3)


        self.verticalLayout_55.addWidget(self.Frame_Train_GPTSoVITS_FileListPath)


        self.verticalLayout_121.addWidget(self.Frame_Train_GPTSoVITS_InputParams_BasicSettings)


        self.verticalLayout_52.addWidget(self.GroupBox_Train_GPTSoVITS_InputParams)

        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setObjectName(u"GroupBox_Train_GPTSoVITS_GPTSoVITSParams")
        self.verticalLayout_122 = QVBoxLayout(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings = QFrame(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)
        self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings.setObjectName(u"Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings")
        self.verticalLayout_56 = QVBoxLayout(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1 = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1.setObjectName(u"Frame_Train_GPTSoVITS_ModelPathPretrainedS1")
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_88 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.gridLayout_88.setSpacing(12)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_88.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1 = LabelBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setObjectName(u"Label_Train_GPTSoVITS_ModelPathPretrainedS1")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_88.addWidget(self.Label_Train_GPTSoVITS_ModelPathPretrainedS1, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS1 = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_88.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS1, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions")
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_88.addWidget(self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1 = LineEditBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1")
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.setMinimumSize(QSize(0, 27))

        self.gridLayout_88.addWidget(self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)

        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G.setObjectName(u"Frame_Train_GPTSoVITS_ModelPathPretrainedS2G")
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_86 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.gridLayout_86.setSpacing(12)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.gridLayout_86.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G = LabelBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setObjectName(u"Label_Train_GPTSoVITS_ModelPathPretrainedS2G")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_86.addWidget(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2G = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_86.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2G, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions")
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_86.addWidget(self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G = LineEditBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G")
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.setMinimumSize(QSize(0, 27))

        self.gridLayout_86.addWidget(self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)

        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert.setObjectName(u"Frame_Train_GPTSoVITS_ModelDirPretrainedBert")
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_89 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.gridLayout_89.setSpacing(12)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.gridLayout_89.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert = LabelBase(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setObjectName(u"Label_Train_GPTSoVITS_ModelDirPretrainedBert")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_89.addWidget(self.Label_Train_GPTSoVITS_ModelDirPretrainedBert, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedBert = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_89.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedBert, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions")
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_89.addWidget(self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert = LineEditBase(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert")
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.setMinimumSize(QSize(0, 27))

        self.gridLayout_89.addWidget(self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)

        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL.setObjectName(u"Frame_Train_GPTSoVITS_ModelDirPretrainedSSL")
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_95 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.gridLayout_95.setSpacing(12)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL = LabelBase(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setObjectName(u"Label_Train_GPTSoVITS_ModelDirPretrainedSSL")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_95.addWidget(self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedSSL = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_95.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedSSL, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions")
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_95.addWidget(self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL = LineEditBase(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL")
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.setMinimumSize(QSize(0, 27))

        self.gridLayout_95.addWidget(self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)

        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D.setObjectName(u"Frame_Train_GPTSoVITS_ModelPathPretrainedS2D")
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_87 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.gridLayout_87.setSpacing(12)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.gridLayout_87.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D = LabelBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setObjectName(u"Label_Train_GPTSoVITS_ModelPathPretrainedS2D")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_87.addWidget(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2D = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_87.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2D, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions")
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_87.addWidget(self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D = LineEditBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D")
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.setMinimumSize(QSize(0, 27))

        self.gridLayout_87.addWidget(self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)


        self.verticalLayout_122.addWidget(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)

        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setObjectName(u"ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings")
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 105))
        self.verticalLayout_57 = QVBoxLayout(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_FP16Run = QFrame(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content)
        self.Frame_Train_GPTSoVITS_FP16Run.setObjectName(u"Frame_Train_GPTSoVITS_FP16Run")
        self.Frame_Train_GPTSoVITS_FP16Run.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_FP16Run.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_91 = QGridLayout(self.Frame_Train_GPTSoVITS_FP16Run)
        self.gridLayout_91.setSpacing(12)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_91.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_FP16Run = LabelBase(self.Frame_Train_GPTSoVITS_FP16Run)
        self.Label_Train_GPTSoVITS_FP16Run.setObjectName(u"Label_Train_GPTSoVITS_FP16Run")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_FP16Run.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_FP16Run.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_FP16Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_91.addWidget(self.Label_Train_GPTSoVITS_FP16Run, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_FP16Run = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_91.addItem(self.HorizontalSpacer_Train_GPTSoVITS_FP16Run, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_FP16Run_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_FP16Run)
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_FP16Run_MoreActions")
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_91.addWidget(self.Button_Train_GPTSoVITS_FP16Run_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_GPTSoVITS_FP16Run = CheckBoxBase(self.Frame_Train_GPTSoVITS_FP16Run)
        self.CheckBox_Train_GPTSoVITS_FP16Run.setObjectName(u"CheckBox_Train_GPTSoVITS_FP16Run")
        self.CheckBox_Train_GPTSoVITS_FP16Run.setMinimumSize(QSize(0, 27))

        self.gridLayout_91.addWidget(self.CheckBox_Train_GPTSoVITS_FP16Run, 1, 0, 1, 3)


        self.verticalLayout_57.addWidget(self.Frame_Train_GPTSoVITS_FP16Run)

        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.addItem(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_122.addWidget(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings)


        self.verticalLayout_52.addWidget(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)

        self.GroupBox_Train_GPTSoVITS_OutputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.GroupBox_Train_GPTSoVITS_OutputParams.setObjectName(u"GroupBox_Train_GPTSoVITS_OutputParams")
        self.verticalLayout_77 = QVBoxLayout(self.GroupBox_Train_GPTSoVITS_OutputParams)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings = QFrame(self.GroupBox_Train_GPTSoVITS_OutputParams)
        self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings.setObjectName(u"Frame_Train_GPTSoVITS_OutputParams_BasicSettings")
        self.verticalLayout_58 = QVBoxLayout(self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_OutputDirName = QFrame(self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_OutputDirName.setObjectName(u"Frame_Train_GPTSoVITS_OutputDirName")
        self.Frame_Train_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_98 = QGridLayout(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.gridLayout_98.setSpacing(12)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gridLayout_98.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_OutputDirName = LabelBase(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.Label_Train_GPTSoVITS_OutputDirName.setObjectName(u"Label_Train_GPTSoVITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_98.addWidget(self.Label_Train_GPTSoVITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_98.addItem(self.HorizontalSpacer_Train_GPTSoVITS_OutputDirName, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_OutputDirName_MoreActions")
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_98.addWidget(self.Button_Train_GPTSoVITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_OutputDirName = LineEditBase(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.LineEdit_Train_GPTSoVITS_OutputDirName.setObjectName(u"LineEdit_Train_GPTSoVITS_OutputDirName")
        self.LineEdit_Train_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_98.addWidget(self.LineEdit_Train_GPTSoVITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_58.addWidget(self.Frame_Train_GPTSoVITS_OutputDirName)


        self.verticalLayout_77.addWidget(self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings)

        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_GPTSoVITS_OutputParams)
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings")
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 105))
        self.verticalLayout_60 = QVBoxLayout(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_LogDir = QFrame(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Train_GPTSoVITS_LogDir.setObjectName(u"Frame_Train_GPTSoVITS_LogDir")
        self.Frame_Train_GPTSoVITS_LogDir.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_LogDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_110 = QGridLayout(self.Frame_Train_GPTSoVITS_LogDir)
        self.gridLayout_110.setSpacing(12)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gridLayout_110.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_LogDir = LabelBase(self.Frame_Train_GPTSoVITS_LogDir)
        self.Label_Train_GPTSoVITS_LogDir.setObjectName(u"Label_Train_GPTSoVITS_LogDir")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_LogDir.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_LogDir.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_LogDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_110.addWidget(self.Label_Train_GPTSoVITS_LogDir, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_LogDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_110.addItem(self.HorizontalSpacer_Train_GPTSoVITS_LogDir, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_LogDir_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_LogDir)
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_LogDir_MoreActions")
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_110.addWidget(self.Button_Train_GPTSoVITS_LogDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_LogDir = LineEditBase(self.Frame_Train_GPTSoVITS_LogDir)
        self.LineEdit_Train_GPTSoVITS_LogDir.setObjectName(u"LineEdit_Train_GPTSoVITS_LogDir")
        self.LineEdit_Train_GPTSoVITS_LogDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_110.addWidget(self.LineEdit_Train_GPTSoVITS_LogDir, 1, 0, 1, 3)


        self.verticalLayout_60.addWidget(self.Frame_Train_GPTSoVITS_LogDir)

        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_77.addWidget(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings)


        self.verticalLayout_52.addWidget(self.GroupBox_Train_GPTSoVITS_OutputParams)

        self.VerticalSpacer_Train_GPTSoVITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.VerticalSpacer_Train_GPTSoVITS)

        self.ScrollArea_Middle_Train_GPTSoVITS.setWidget(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)

        self.gridLayout_85.addWidget(self.ScrollArea_Middle_Train_GPTSoVITS, 0, 1, 1, 1)

        self.Widget_Right_Train_GPTSoVITS = QWidget(self.Subpage_Train_GPTSoVITS)
        self.Widget_Right_Train_GPTSoVITS.setObjectName(u"Widget_Right_Train_GPTSoVITS")
        self.Widget_Right_Train_GPTSoVITS.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_14 = QGridLayout(self.Widget_Right_Train_GPTSoVITS)
        self.gridLayout_14.setSpacing(12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Train_GPTSoVITS = TextBrowserBase(self.Widget_Right_Train_GPTSoVITS)
        self.TextBrowser_Params_Train_GPTSoVITS.setObjectName(u"TextBrowser_Params_Train_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Train_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Train_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Train_GPTSoVITS.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_14.addWidget(self.TextBrowser_Params_Train_GPTSoVITS, 0, 0, 1, 3)

        self.Button_ResetSettings_Train_GPTSoVITS = HollowButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_ResetSettings_Train_GPTSoVITS.setObjectName(u"Button_ResetSettings_Train_GPTSoVITS")

        self.gridLayout_14.addWidget(self.Button_ResetSettings_Train_GPTSoVITS, 1, 0, 1, 1)

        self.Button_ImportSettings_Train_GPTSoVITS = HollowButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_ImportSettings_Train_GPTSoVITS.setObjectName(u"Button_ImportSettings_Train_GPTSoVITS")

        self.gridLayout_14.addWidget(self.Button_ImportSettings_Train_GPTSoVITS, 1, 1, 1, 1)

        self.Button_ExportSettings_Train_GPTSoVITS = HollowButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_ExportSettings_Train_GPTSoVITS.setObjectName(u"Button_ExportSettings_Train_GPTSoVITS")

        self.gridLayout_14.addWidget(self.Button_ExportSettings_Train_GPTSoVITS, 1, 2, 1, 1)

        self.Button_RunTensorboard_Train_GPTSoVITS = HollowButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_RunTensorboard_Train_GPTSoVITS.setObjectName(u"Button_RunTensorboard_Train_GPTSoVITS")

        self.gridLayout_14.addWidget(self.Button_RunTensorboard_Train_GPTSoVITS, 2, 0, 1, 3)

        self.Button_CheckOutput_Train_GPTSoVITS = HollowButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_CheckOutput_Train_GPTSoVITS.setObjectName(u"Button_CheckOutput_Train_GPTSoVITS")

        self.gridLayout_14.addWidget(self.Button_CheckOutput_Train_GPTSoVITS, 3, 0, 1, 3)


        self.gridLayout_85.addWidget(self.Widget_Right_Train_GPTSoVITS, 0, 2, 1, 1)

        self.ProgressBar_Train_GPTSoVITS = ProgressBarBase(self.Subpage_Train_GPTSoVITS)
        self.ProgressBar_Train_GPTSoVITS.setObjectName(u"ProgressBar_Train_GPTSoVITS")
        self.ProgressBar_Train_GPTSoVITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Train_GPTSoVITS.setValue(0)
        self.ProgressBar_Train_GPTSoVITS.setTextVisible(False)
        self.horizontalLayout_41 = QHBoxLayout(self.ProgressBar_Train_GPTSoVITS)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Train_GPTSoVITS = QStackedWidget(self.ProgressBar_Train_GPTSoVITS)
        self.StackedWidget_Train_GPTSoVITS.setObjectName(u"StackedWidget_Train_GPTSoVITS")
        self.StackedWidget_Train_GPTSoVITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Train_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_Train_GPTSoVITS_Execute = QWidget()
        self.Page_Train_GPTSoVITS_Execute.setObjectName(u"Page_Train_GPTSoVITS_Execute")
        self.verticalLayout_96 = QVBoxLayout(self.Page_Train_GPTSoVITS_Execute)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_GPTSoVITS_Execute = HollowButton(self.Page_Train_GPTSoVITS_Execute)
        self.Button_Train_GPTSoVITS_Execute.setObjectName(u"Button_Train_GPTSoVITS_Execute")
        sizePolicy2.setHeightForWidth(self.Button_Train_GPTSoVITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Train_GPTSoVITS_Execute.setSizePolicy(sizePolicy2)
        self.Button_Train_GPTSoVITS_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_96.addWidget(self.Button_Train_GPTSoVITS_Execute)

        self.StackedWidget_Train_GPTSoVITS.addWidget(self.Page_Train_GPTSoVITS_Execute)
        self.Page_Train_GPTSoVITS_Terminate = QWidget()
        self.Page_Train_GPTSoVITS_Terminate.setObjectName(u"Page_Train_GPTSoVITS_Terminate")
        self.verticalLayout_97 = QVBoxLayout(self.Page_Train_GPTSoVITS_Terminate)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_GPTSoVITS_Terminate = HollowButton(self.Page_Train_GPTSoVITS_Terminate)
        self.Button_Train_GPTSoVITS_Terminate.setObjectName(u"Button_Train_GPTSoVITS_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_Train_GPTSoVITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Train_GPTSoVITS_Terminate.setSizePolicy(sizePolicy2)
        self.Button_Train_GPTSoVITS_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_97.addWidget(self.Button_Train_GPTSoVITS_Terminate)

        self.StackedWidget_Train_GPTSoVITS.addWidget(self.Page_Train_GPTSoVITS_Terminate)

        self.horizontalLayout_41.addWidget(self.StackedWidget_Train_GPTSoVITS)


        self.gridLayout_85.addWidget(self.ProgressBar_Train_GPTSoVITS, 1, 0, 1, 3)

        self.gridLayout_85.setColumnStretch(0, 3)
        self.gridLayout_85.setColumnStretch(1, 10)
        self.gridLayout_85.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Train.addWidget(self.Subpage_Train_GPTSoVITS)
        self.Subpage_Train_VITS = QWidget()
        self.Subpage_Train_VITS.setObjectName(u"Subpage_Train_VITS")
        self.gridLayout_22 = QGridLayout(self.Subpage_Train_VITS)
        self.gridLayout_22.setSpacing(12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.Widget_Right_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Right_Train_VITS.setObjectName(u"Widget_Right_Train_VITS")
        self.Widget_Right_Train_VITS.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout = QGridLayout(self.Widget_Right_Train_VITS)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Train_VITS = TextBrowserBase(self.Widget_Right_Train_VITS)
        self.TextBrowser_Params_Train_VITS.setObjectName(u"TextBrowser_Params_Train_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Train_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Train_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Train_VITS.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout.addWidget(self.TextBrowser_Params_Train_VITS, 0, 0, 1, 3)

        self.Button_ResetSettings_Train_VITS = HollowButton(self.Widget_Right_Train_VITS)
        self.Button_ResetSettings_Train_VITS.setObjectName(u"Button_ResetSettings_Train_VITS")

        self.gridLayout.addWidget(self.Button_ResetSettings_Train_VITS, 1, 0, 1, 1)

        self.Button_ImportSettings_Train_VITS = HollowButton(self.Widget_Right_Train_VITS)
        self.Button_ImportSettings_Train_VITS.setObjectName(u"Button_ImportSettings_Train_VITS")

        self.gridLayout.addWidget(self.Button_ImportSettings_Train_VITS, 1, 1, 1, 1)

        self.Button_ExportSettings_Train_VITS = HollowButton(self.Widget_Right_Train_VITS)
        self.Button_ExportSettings_Train_VITS.setObjectName(u"Button_ExportSettings_Train_VITS")

        self.gridLayout.addWidget(self.Button_ExportSettings_Train_VITS, 1, 2, 1, 1)

        self.Button_RunTensorboard_Train_VITS = HollowButton(self.Widget_Right_Train_VITS)
        self.Button_RunTensorboard_Train_VITS.setObjectName(u"Button_RunTensorboard_Train_VITS")

        self.gridLayout.addWidget(self.Button_RunTensorboard_Train_VITS, 2, 0, 1, 3)

        self.Button_CheckOutput_Train_VITS = HollowButton(self.Widget_Right_Train_VITS)
        self.Button_CheckOutput_Train_VITS.setObjectName(u"Button_CheckOutput_Train_VITS")

        self.gridLayout.addWidget(self.Button_CheckOutput_Train_VITS, 3, 0, 1, 3)


        self.gridLayout_22.addWidget(self.Widget_Right_Train_VITS, 0, 2, 1, 1)

        self.Widget_Left_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Left_Train_VITS.setObjectName(u"Widget_Left_Train_VITS")
        self.Widget_Left_Train_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Train_VITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.Widget_Left_Train_VITS)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Train_VITS = TreeWidgetBase(self.Widget_Left_Train_VITS)
        __qtreewidgetitem5 = QTreeWidgetItem(self.TreeWidget_Catalogue_Train_VITS)
        QTreeWidgetItem(__qtreewidgetitem5)
        self.TreeWidget_Catalogue_Train_VITS.setObjectName(u"TreeWidget_Catalogue_Train_VITS")

        self.verticalLayout_10.addWidget(self.TreeWidget_Catalogue_Train_VITS)


        self.gridLayout_22.addWidget(self.Widget_Left_Train_VITS, 0, 0, 1, 1)

        self.ProgressBar_Train_VITS = ProgressBarBase(self.Subpage_Train_VITS)
        self.ProgressBar_Train_VITS.setObjectName(u"ProgressBar_Train_VITS")
        self.ProgressBar_Train_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Train_VITS.setValue(0)
        self.ProgressBar_Train_VITS.setTextVisible(False)
        self.horizontalLayout_39 = QHBoxLayout(self.ProgressBar_Train_VITS)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Train_VITS = QStackedWidget(self.ProgressBar_Train_VITS)
        self.StackedWidget_Train_VITS.setObjectName(u"StackedWidget_Train_VITS")
        self.StackedWidget_Train_VITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Train_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_Train_VITS_Execute = QWidget()
        self.Page_Train_VITS_Execute.setObjectName(u"Page_Train_VITS_Execute")
        self.verticalLayout_94 = QVBoxLayout(self.Page_Train_VITS_Execute)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_VITS_Execute = HollowButton(self.Page_Train_VITS_Execute)
        self.Button_Train_VITS_Execute.setObjectName(u"Button_Train_VITS_Execute")
        sizePolicy2.setHeightForWidth(self.Button_Train_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Train_VITS_Execute.setSizePolicy(sizePolicy2)
        self.Button_Train_VITS_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_94.addWidget(self.Button_Train_VITS_Execute)

        self.StackedWidget_Train_VITS.addWidget(self.Page_Train_VITS_Execute)
        self.Page_Train_VITS_Terminate = QWidget()
        self.Page_Train_VITS_Terminate.setObjectName(u"Page_Train_VITS_Terminate")
        self.verticalLayout_95 = QVBoxLayout(self.Page_Train_VITS_Terminate)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_VITS_Terminate = HollowButton(self.Page_Train_VITS_Terminate)
        self.Button_Train_VITS_Terminate.setObjectName(u"Button_Train_VITS_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_Train_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Train_VITS_Terminate.setSizePolicy(sizePolicy2)
        self.Button_Train_VITS_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_95.addWidget(self.Button_Train_VITS_Terminate)

        self.StackedWidget_Train_VITS.addWidget(self.Page_Train_VITS_Terminate)

        self.horizontalLayout_39.addWidget(self.StackedWidget_Train_VITS)


        self.gridLayout_22.addWidget(self.ProgressBar_Train_VITS, 1, 0, 1, 3)

        self.ScrollArea_Middle_Train_VITS = ScrollAreaBase(self.Subpage_Train_VITS)
        self.ScrollArea_Middle_Train_VITS.setObjectName(u"ScrollArea_Middle_Train_VITS")
        self.ScrollArea_Middle_Train_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Train_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Train_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Train_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_Train_VITS")
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setGeometry(QRect(0, 0, 586, 1508))
        self.verticalLayout_28 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.verticalLayout_28.setSpacing(12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Train_VITS_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_InputParams.setObjectName(u"GroupBox_Train_VITS_InputParams")
        self.verticalLayout_116 = QVBoxLayout(self.GroupBox_Train_VITS_InputParams)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_VITS_InputParams_BasicSettings = QFrame(self.GroupBox_Train_VITS_InputParams)
        self.Frame_Train_VITS_InputParams_BasicSettings.setObjectName(u"Frame_Train_VITS_InputParams_BasicSettings")
        self.verticalLayout_18 = QVBoxLayout(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_FileListPathTraining = QFrame(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.Frame_Train_VITS_FileListPathTraining.setObjectName(u"Frame_Train_VITS_FileListPathTraining")
        self.Frame_Train_VITS_FileListPathTraining.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileListPathTraining.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_57 = QGridLayout(self.Frame_Train_VITS_FileListPathTraining)
        self.gridLayout_57.setSpacing(12)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FileListPathTraining = LabelBase(self.Frame_Train_VITS_FileListPathTraining)
        self.Label_Train_VITS_FileListPathTraining.setObjectName(u"Label_Train_VITS_FileListPathTraining")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_FileListPathTraining.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FileListPathTraining.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_FileListPathTraining.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_57.addWidget(self.Label_Train_VITS_FileListPathTraining, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FileListPathTraining = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.HorizontalSpacer_Train_VITS_FileListPathTraining, 0, 1, 1, 1)

        self.Button_Train_VITS_FileListPathTraining_MoreActions = MenuButton(self.Frame_Train_VITS_FileListPathTraining)
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setObjectName(u"Button_Train_VITS_FileListPathTraining_MoreActions")
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_57.addWidget(self.Button_Train_VITS_FileListPathTraining_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_FileListPathTraining = LineEditBase(self.Frame_Train_VITS_FileListPathTraining)
        self.LineEdit_Train_VITS_FileListPathTraining.setObjectName(u"LineEdit_Train_VITS_FileListPathTraining")
        self.LineEdit_Train_VITS_FileListPathTraining.setMinimumSize(QSize(0, 27))

        self.gridLayout_57.addWidget(self.LineEdit_Train_VITS_FileListPathTraining, 1, 0, 1, 3)


        self.verticalLayout_18.addWidget(self.Frame_Train_VITS_FileListPathTraining)

        self.Frame_Train_VITS_FileListPathValidation = QFrame(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.Frame_Train_VITS_FileListPathValidation.setObjectName(u"Frame_Train_VITS_FileListPathValidation")
        self.Frame_Train_VITS_FileListPathValidation.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileListPathValidation.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_58 = QGridLayout(self.Frame_Train_VITS_FileListPathValidation)
        self.gridLayout_58.setSpacing(12)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FileListPathValidation = LabelBase(self.Frame_Train_VITS_FileListPathValidation)
        self.Label_Train_VITS_FileListPathValidation.setObjectName(u"Label_Train_VITS_FileListPathValidation")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_FileListPathValidation.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FileListPathValidation.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_FileListPathValidation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_58.addWidget(self.Label_Train_VITS_FileListPathValidation, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FileListPathValidation = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_58.addItem(self.HorizontalSpacer_Train_VITS_FileListPathValidation, 0, 1, 1, 1)

        self.Button_Train_VITS_FileListPathValidation_MoreActions = MenuButton(self.Frame_Train_VITS_FileListPathValidation)
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setObjectName(u"Button_Train_VITS_FileListPathValidation_MoreActions")
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_58.addWidget(self.Button_Train_VITS_FileListPathValidation_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_FileListPathValidation = LineEditBase(self.Frame_Train_VITS_FileListPathValidation)
        self.LineEdit_Train_VITS_FileListPathValidation.setObjectName(u"LineEdit_Train_VITS_FileListPathValidation")
        self.LineEdit_Train_VITS_FileListPathValidation.setMinimumSize(QSize(0, 27))

        self.gridLayout_58.addWidget(self.LineEdit_Train_VITS_FileListPathValidation, 1, 0, 1, 3)


        self.verticalLayout_18.addWidget(self.Frame_Train_VITS_FileListPathValidation)


        self.verticalLayout_116.addWidget(self.Frame_Train_VITS_InputParams_BasicSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_InputParams)

        self.GroupBox_Train_VITS_VITSParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_VITSParams.setObjectName(u"GroupBox_Train_VITS_VITSParams")
        self.verticalLayout_114 = QVBoxLayout(self.GroupBox_Train_VITS_VITSParams)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_VITS_VITSParams_BasicSettings = QFrame(self.GroupBox_Train_VITS_VITSParams)
        self.Frame_Train_VITS_VITSParams_BasicSettings.setObjectName(u"Frame_Train_VITS_VITSParams_BasicSettings")
        self.verticalLayout_17 = QVBoxLayout(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_Epochs = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_Epochs.setObjectName(u"Frame_Train_VITS_Epochs")
        self.Frame_Train_VITS_Epochs.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Epochs.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_59 = QGridLayout(self.Frame_Train_VITS_Epochs)
        self.gridLayout_59.setSpacing(12)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Epochs = LabelBase(self.Frame_Train_VITS_Epochs)
        self.Label_Train_VITS_Epochs.setObjectName(u"Label_Train_VITS_Epochs")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_Epochs.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Epochs.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_Epochs.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_59.addWidget(self.Label_Train_VITS_Epochs, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_Epochs = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_59.addItem(self.HorizontalSpacer_Train_VITS_Epochs, 0, 1, 1, 1)

        self.Button_Train_VITS_Epochs_MoreActions = MenuButton(self.Frame_Train_VITS_Epochs)
        self.Button_Train_VITS_Epochs_MoreActions.setObjectName(u"Button_Train_VITS_Epochs_MoreActions")
        self.Button_Train_VITS_Epochs_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_Epochs_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_Epochs_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_59.addWidget(self.Button_Train_VITS_Epochs_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_Epochs = SpinBoxBase(self.Frame_Train_VITS_Epochs)
        self.SpinBox_Train_VITS_Epochs.setObjectName(u"SpinBox_Train_VITS_Epochs")
        self.SpinBox_Train_VITS_Epochs.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_Epochs.setMinimum(-999999)
        self.SpinBox_Train_VITS_Epochs.setMaximum(999999)

        self.gridLayout_59.addWidget(self.SpinBox_Train_VITS_Epochs, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Epochs)

        self.Frame_Train_VITS_BatchSize = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_BatchSize.setObjectName(u"Frame_Train_VITS_BatchSize")
        self.Frame_Train_VITS_BatchSize.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_BatchSize.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_60 = QGridLayout(self.Frame_Train_VITS_BatchSize)
        self.gridLayout_60.setSpacing(12)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_BatchSize = LabelBase(self.Frame_Train_VITS_BatchSize)
        self.Label_Train_VITS_BatchSize.setObjectName(u"Label_Train_VITS_BatchSize")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_BatchSize.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_BatchSize.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_BatchSize.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_60.addWidget(self.Label_Train_VITS_BatchSize, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_BatchSize = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.HorizontalSpacer_Train_VITS_BatchSize, 0, 1, 1, 1)

        self.Button_Train_VITS_BatchSize_MoreActions = MenuButton(self.Frame_Train_VITS_BatchSize)
        self.Button_Train_VITS_BatchSize_MoreActions.setObjectName(u"Button_Train_VITS_BatchSize_MoreActions")
        self.Button_Train_VITS_BatchSize_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_BatchSize_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_BatchSize_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_60.addWidget(self.Button_Train_VITS_BatchSize_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_BatchSize = SpinBoxBase(self.Frame_Train_VITS_BatchSize)
        self.SpinBox_Train_VITS_BatchSize.setObjectName(u"SpinBox_Train_VITS_BatchSize")
        self.SpinBox_Train_VITS_BatchSize.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_BatchSize.setMinimum(-999999)
        self.SpinBox_Train_VITS_BatchSize.setMaximum(999999)

        self.gridLayout_60.addWidget(self.SpinBox_Train_VITS_BatchSize, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_BatchSize)

        self.Frame_Train_VITS_UsePretrainedModels = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_UsePretrainedModels.setObjectName(u"Frame_Train_VITS_UsePretrainedModels")
        self.Frame_Train_VITS_UsePretrainedModels.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_UsePretrainedModels.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_61 = QGridLayout(self.Frame_Train_VITS_UsePretrainedModels)
        self.gridLayout_61.setSpacing(12)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_UsePretrainedModels = LabelBase(self.Frame_Train_VITS_UsePretrainedModels)
        self.Label_Train_VITS_UsePretrainedModels.setObjectName(u"Label_Train_VITS_UsePretrainedModels")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_UsePretrainedModels.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_UsePretrainedModels.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_UsePretrainedModels.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_61.addWidget(self.Label_Train_VITS_UsePretrainedModels, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_UsePretrainedModels = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_61.addItem(self.HorizontalSpacer_Train_VITS_UsePretrainedModels, 0, 1, 1, 1)

        self.Button_Train_VITS_UsePretrainedModels_MoreActions = MenuButton(self.Frame_Train_VITS_UsePretrainedModels)
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setObjectName(u"Button_Train_VITS_UsePretrainedModels_MoreActions")
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_61.addWidget(self.Button_Train_VITS_UsePretrainedModels_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_UsePretrainedModels = CheckBoxBase(self.Frame_Train_VITS_UsePretrainedModels)
        self.CheckBox_Train_VITS_UsePretrainedModels.setObjectName(u"CheckBox_Train_VITS_UsePretrainedModels")
        self.CheckBox_Train_VITS_UsePretrainedModels.setMinimumSize(QSize(0, 27))

        self.gridLayout_61.addWidget(self.CheckBox_Train_VITS_UsePretrainedModels, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_UsePretrainedModels)

        self.Frame_Train_VITS_ModelPathPretrainedG = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ModelPathPretrainedG.setObjectName(u"Frame_Train_VITS_ModelPathPretrainedG")
        self.Frame_Train_VITS_ModelPathPretrainedG.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ModelPathPretrainedG.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_65 = QGridLayout(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.gridLayout_65.setSpacing(12)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_ModelPathPretrainedG = LabelBase(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.Label_Train_VITS_ModelPathPretrainedG.setObjectName(u"Label_Train_VITS_ModelPathPretrainedG")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_ModelPathPretrainedG.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_ModelPathPretrainedG.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_ModelPathPretrainedG.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_65.addWidget(self.Label_Train_VITS_ModelPathPretrainedG, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ModelPathPretrainedG = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_65.addItem(self.HorizontalSpacer_Train_VITS_ModelPathPretrainedG, 0, 1, 1, 1)

        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions = MenuButton(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setObjectName(u"Button_Train_VITS_ModelPathPretrainedG_MoreActions")
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_65.addWidget(self.Button_Train_VITS_ModelPathPretrainedG_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ModelPathPretrainedG = LineEditBase(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.LineEdit_Train_VITS_ModelPathPretrainedG.setObjectName(u"LineEdit_Train_VITS_ModelPathPretrainedG")
        self.LineEdit_Train_VITS_ModelPathPretrainedG.setMinimumSize(QSize(0, 27))

        self.gridLayout_65.addWidget(self.LineEdit_Train_VITS_ModelPathPretrainedG, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ModelPathPretrainedG)

        self.Frame_Train_VITS_ModelPathPretrainedD = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ModelPathPretrainedD.setObjectName(u"Frame_Train_VITS_ModelPathPretrainedD")
        self.Frame_Train_VITS_ModelPathPretrainedD.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ModelPathPretrainedD.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_66 = QGridLayout(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.gridLayout_66.setSpacing(12)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_ModelPathPretrainedD = LabelBase(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.Label_Train_VITS_ModelPathPretrainedD.setObjectName(u"Label_Train_VITS_ModelPathPretrainedD")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_ModelPathPretrainedD.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_ModelPathPretrainedD.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_ModelPathPretrainedD.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_66.addWidget(self.Label_Train_VITS_ModelPathPretrainedD, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ModelPathPretrainedD = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_66.addItem(self.HorizontalSpacer_Train_VITS_ModelPathPretrainedD, 0, 1, 1, 1)

        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions = MenuButton(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setObjectName(u"Button_Train_VITS_ModelPathPretrainedD_MoreActions")
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_66.addWidget(self.Button_Train_VITS_ModelPathPretrainedD_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ModelPathPretrainedD = LineEditBase(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.LineEdit_Train_VITS_ModelPathPretrainedD.setObjectName(u"LineEdit_Train_VITS_ModelPathPretrainedD")
        self.LineEdit_Train_VITS_ModelPathPretrainedD.setMinimumSize(QSize(0, 27))

        self.gridLayout_66.addWidget(self.LineEdit_Train_VITS_ModelPathPretrainedD, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ModelPathPretrainedD)

        self.Frame_Train_VITS_KeepOriginalSpeakers = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_KeepOriginalSpeakers.setObjectName(u"Frame_Train_VITS_KeepOriginalSpeakers")
        self.Frame_Train_VITS_KeepOriginalSpeakers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_67 = QGridLayout(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.gridLayout_67.setSpacing(12)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_KeepOriginalSpeakers = LabelBase(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.Label_Train_VITS_KeepOriginalSpeakers.setObjectName(u"Label_Train_VITS_KeepOriginalSpeakers")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_KeepOriginalSpeakers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_KeepOriginalSpeakers.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_67.addWidget(self.Label_Train_VITS_KeepOriginalSpeakers, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_KeepOriginalSpeakers = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_67.addItem(self.HorizontalSpacer_Train_VITS_KeepOriginalSpeakers, 0, 1, 1, 1)

        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions = MenuButton(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setObjectName(u"Button_Train_VITS_KeepOriginalSpeakers_MoreActions")
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_67.addWidget(self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_KeepOriginalSpeakers = CheckBoxBase(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setObjectName(u"CheckBox_Train_VITS_KeepOriginalSpeakers")
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setMinimumSize(QSize(0, 27))

        self.gridLayout_67.addWidget(self.CheckBox_Train_VITS_KeepOriginalSpeakers, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_KeepOriginalSpeakers)

        self.Frame_Train_VITS_ConfigPathLoad = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ConfigPathLoad.setObjectName(u"Frame_Train_VITS_ConfigPathLoad")
        self.Frame_Train_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ConfigPathLoad.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_77 = QGridLayout(self.Frame_Train_VITS_ConfigPathLoad)
        self.gridLayout_77.setSpacing(12)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.gridLayout_77.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_ConfigPathLoad = LabelBase(self.Frame_Train_VITS_ConfigPathLoad)
        self.Label_Train_VITS_ConfigPathLoad.setObjectName(u"Label_Train_VITS_ConfigPathLoad")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_ConfigPathLoad.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_ConfigPathLoad.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_ConfigPathLoad.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_77.addWidget(self.Label_Train_VITS_ConfigPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ConfigPathLoad = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_77.addItem(self.HorizontalSpacer_Train_VITS_ConfigPathLoad, 0, 1, 1, 1)

        self.Button_Train_VITS_ConfigPathLoad_MoreActions = MenuButton(self.Frame_Train_VITS_ConfigPathLoad)
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setObjectName(u"Button_Train_VITS_ConfigPathLoad_MoreActions")
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_77.addWidget(self.Button_Train_VITS_ConfigPathLoad_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ConfigPathLoad = LineEditBase(self.Frame_Train_VITS_ConfigPathLoad)
        self.LineEdit_Train_VITS_ConfigPathLoad.setObjectName(u"LineEdit_Train_VITS_ConfigPathLoad")
        self.LineEdit_Train_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_77.addWidget(self.LineEdit_Train_VITS_ConfigPathLoad, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ConfigPathLoad)


        self.verticalLayout_114.addWidget(self.Frame_Train_VITS_VITSParams_BasicSettings)

        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_VITS_VITSParams)
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setObjectName(u"ToolBox_Train_VITS_VITSParams_AdvanceSettings")
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 210))
        self.verticalLayout_35 = QVBoxLayout(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_NumWorkers = QFrame(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_Train_VITS_NumWorkers.setObjectName(u"Frame_Train_VITS_NumWorkers")
        self.Frame_Train_VITS_NumWorkers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_NumWorkers.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_63 = QGridLayout(self.Frame_Train_VITS_NumWorkers)
        self.gridLayout_63.setSpacing(12)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_NumWorkers = LabelBase(self.Frame_Train_VITS_NumWorkers)
        self.Label_Train_VITS_NumWorkers.setObjectName(u"Label_Train_VITS_NumWorkers")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_NumWorkers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_NumWorkers.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_NumWorkers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_63.addWidget(self.Label_Train_VITS_NumWorkers, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_NumWorkers = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_63.addItem(self.HorizontalSpacer_Train_VITS_NumWorkers, 0, 1, 1, 1)

        self.Button_Train_VITS_NumWorkers_MoreActions = MenuButton(self.Frame_Train_VITS_NumWorkers)
        self.Button_Train_VITS_NumWorkers_MoreActions.setObjectName(u"Button_Train_VITS_NumWorkers_MoreActions")
        self.Button_Train_VITS_NumWorkers_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_NumWorkers_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_NumWorkers_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_63.addWidget(self.Button_Train_VITS_NumWorkers_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_NumWorkers = SpinBoxBase(self.Frame_Train_VITS_NumWorkers)
        self.SpinBox_Train_VITS_NumWorkers.setObjectName(u"SpinBox_Train_VITS_NumWorkers")
        self.SpinBox_Train_VITS_NumWorkers.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_NumWorkers.setMinimum(-999999)
        self.SpinBox_Train_VITS_NumWorkers.setMaximum(999999)

        self.gridLayout_63.addWidget(self.SpinBox_Train_VITS_NumWorkers, 1, 0, 1, 3)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_NumWorkers)

        self.Frame_Train_VITS_FP16Run = QFrame(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_Train_VITS_FP16Run.setObjectName(u"Frame_Train_VITS_FP16Run")
        self.Frame_Train_VITS_FP16Run.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FP16Run.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_64 = QGridLayout(self.Frame_Train_VITS_FP16Run)
        self.gridLayout_64.setSpacing(12)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FP16Run = LabelBase(self.Frame_Train_VITS_FP16Run)
        self.Label_Train_VITS_FP16Run.setObjectName(u"Label_Train_VITS_FP16Run")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_FP16Run.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FP16Run.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_FP16Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_64.addWidget(self.Label_Train_VITS_FP16Run, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FP16Run = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_64.addItem(self.HorizontalSpacer_Train_VITS_FP16Run, 0, 1, 1, 1)

        self.Button_Train_VITS_FP16Run_MoreActions = MenuButton(self.Frame_Train_VITS_FP16Run)
        self.Button_Train_VITS_FP16Run_MoreActions.setObjectName(u"Button_Train_VITS_FP16Run_MoreActions")
        self.Button_Train_VITS_FP16Run_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FP16Run_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FP16Run_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_64.addWidget(self.Button_Train_VITS_FP16Run_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_FP16Run = CheckBoxBase(self.Frame_Train_VITS_FP16Run)
        self.CheckBox_Train_VITS_FP16Run.setObjectName(u"CheckBox_Train_VITS_FP16Run")
        self.CheckBox_Train_VITS_FP16Run.setMinimumSize(QSize(0, 27))

        self.gridLayout_64.addWidget(self.CheckBox_Train_VITS_FP16Run, 1, 0, 1, 3)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_FP16Run)

        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.addItem(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_114.addWidget(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_VITSParams)

        self.GroupBox_Train_VITS_OutputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_OutputParams.setObjectName(u"GroupBox_Train_VITS_OutputParams")
        self.verticalLayout_80 = QVBoxLayout(self.GroupBox_Train_VITS_OutputParams)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.Frame_Train_VITS_OutputParams_BasicSettings = QFrame(self.GroupBox_Train_VITS_OutputParams)
        self.Frame_Train_VITS_OutputParams_BasicSettings.setObjectName(u"Frame_Train_VITS_OutputParams_BasicSettings")
        self.verticalLayout_26 = QVBoxLayout(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_EvalInterval = QFrame(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.Frame_Train_VITS_EvalInterval.setObjectName(u"Frame_Train_VITS_EvalInterval")
        self.Frame_Train_VITS_EvalInterval.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_EvalInterval.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_62 = QGridLayout(self.Frame_Train_VITS_EvalInterval)
        self.gridLayout_62.setSpacing(12)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_EvalInterval = LabelBase(self.Frame_Train_VITS_EvalInterval)
        self.Label_Train_VITS_EvalInterval.setObjectName(u"Label_Train_VITS_EvalInterval")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_EvalInterval.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_EvalInterval.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_EvalInterval.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_62.addWidget(self.Label_Train_VITS_EvalInterval, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_EvalInterval = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_62.addItem(self.HorizontalSpacer_Train_VITS_EvalInterval, 0, 1, 1, 1)

        self.Button_Train_VITS_EvalInterval_MoreActions = MenuButton(self.Frame_Train_VITS_EvalInterval)
        self.Button_Train_VITS_EvalInterval_MoreActions.setObjectName(u"Button_Train_VITS_EvalInterval_MoreActions")
        self.Button_Train_VITS_EvalInterval_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_EvalInterval_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_EvalInterval_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_62.addWidget(self.Button_Train_VITS_EvalInterval_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_EvalInterval = SpinBoxBase(self.Frame_Train_VITS_EvalInterval)
        self.SpinBox_Train_VITS_EvalInterval.setObjectName(u"SpinBox_Train_VITS_EvalInterval")
        self.SpinBox_Train_VITS_EvalInterval.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_EvalInterval.setMinimum(-999999)
        self.SpinBox_Train_VITS_EvalInterval.setMaximum(999999)

        self.gridLayout_62.addWidget(self.SpinBox_Train_VITS_EvalInterval, 1, 0, 1, 3)


        self.verticalLayout_26.addWidget(self.Frame_Train_VITS_EvalInterval)

        self.Frame_Train_VITS_OutputDirName = QFrame(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.Frame_Train_VITS_OutputDirName.setObjectName(u"Frame_Train_VITS_OutputDirName")
        self.Frame_Train_VITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_68 = QGridLayout(self.Frame_Train_VITS_OutputDirName)
        self.gridLayout_68.setSpacing(12)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_OutputDirName = LabelBase(self.Frame_Train_VITS_OutputDirName)
        self.Label_Train_VITS_OutputDirName.setObjectName(u"Label_Train_VITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_68.addWidget(self.Label_Train_VITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_68.addItem(self.HorizontalSpacer_Train_VITS_OutputDirName, 0, 1, 1, 1)

        self.Button_Train_VITS_OutputDirName_MoreActions = MenuButton(self.Frame_Train_VITS_OutputDirName)
        self.Button_Train_VITS_OutputDirName_MoreActions.setObjectName(u"Button_Train_VITS_OutputDirName_MoreActions")
        self.Button_Train_VITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_68.addWidget(self.Button_Train_VITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_OutputDirName = LineEditBase(self.Frame_Train_VITS_OutputDirName)
        self.LineEdit_Train_VITS_OutputDirName.setObjectName(u"LineEdit_Train_VITS_OutputDirName")
        self.LineEdit_Train_VITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_68.addWidget(self.LineEdit_Train_VITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_26.addWidget(self.Frame_Train_VITS_OutputDirName)


        self.verticalLayout_80.addWidget(self.Frame_Train_VITS_OutputParams_BasicSettings)

        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_VITS_OutputParams)
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_Train_VITS_OutputParams_AdvanceSettings")
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 105))
        self.verticalLayout_79 = QVBoxLayout(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_LogDir = QFrame(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Train_VITS_LogDir.setObjectName(u"Frame_Train_VITS_LogDir")
        self.Frame_Train_VITS_LogDir.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_LogDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_111 = QGridLayout(self.Frame_Train_VITS_LogDir)
        self.gridLayout_111.setSpacing(12)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.gridLayout_111.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_LogDir = LabelBase(self.Frame_Train_VITS_LogDir)
        self.Label_Train_VITS_LogDir.setObjectName(u"Label_Train_VITS_LogDir")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_LogDir.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_LogDir.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_LogDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_111.addWidget(self.Label_Train_VITS_LogDir, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_LogDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_111.addItem(self.HorizontalSpacer_Train_VITS_LogDir, 0, 1, 1, 1)

        self.Button_Train_VITS_LogDir_MoreActions = MenuButton(self.Frame_Train_VITS_LogDir)
        self.Button_Train_VITS_LogDir_MoreActions.setObjectName(u"Button_Train_VITS_LogDir_MoreActions")
        self.Button_Train_VITS_LogDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_LogDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_LogDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_111.addWidget(self.Button_Train_VITS_LogDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_LogDir = LineEditBase(self.Frame_Train_VITS_LogDir)
        self.LineEdit_Train_VITS_LogDir.setObjectName(u"LineEdit_Train_VITS_LogDir")
        self.LineEdit_Train_VITS_LogDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_111.addWidget(self.LineEdit_Train_VITS_LogDir, 1, 0, 1, 3)


        self.verticalLayout_79.addWidget(self.Frame_Train_VITS_LogDir)

        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_80.addWidget(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_OutputParams)

        self.VerticalSpacer_Train_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.VerticalSpacer_Train_VITS)

        self.ScrollArea_Middle_Train_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_Train_VITS)

        self.gridLayout_22.addWidget(self.ScrollArea_Middle_Train_VITS, 0, 1, 1, 1)

        self.gridLayout_22.setColumnStretch(0, 3)
        self.gridLayout_22.setColumnStretch(1, 10)
        self.gridLayout_22.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Train.addWidget(self.Subpage_Train_VITS)

        self.verticalLayout_43.addWidget(self.StackedWidget_Pages_Train)

        self.StackedWidget_Pages.addWidget(self.Page_Train)
        self.Page_TTS = QWidget()
        self.Page_TTS.setObjectName(u"Page_TTS")
        self.verticalLayout_42 = QVBoxLayout(self.Page_TTS)
        self.verticalLayout_42.setSpacing(21)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(21, 12, 21, 12)
        self.Frame_TTS_Top = QFrame(self.Page_TTS)
        self.Frame_TTS_Top.setObjectName(u"Frame_TTS_Top")
        self.Frame_TTS_Top.setMinimumSize(QSize(0, 60))
        self.Frame_TTS_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.Frame_TTS_Top)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Button_VoiceConverter_Title_GPTSoVITS = NavigationButton(self.Frame_TTS_Top)
        self.Button_VoiceConverter_Title_GPTSoVITS.setObjectName(u"Button_VoiceConverter_Title_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.Button_VoiceConverter_Title_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.Button_VoiceConverter_Title_GPTSoVITS.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.Button_VoiceConverter_Title_GPTSoVITS)

        self.Button_VoiceConverter_Title_VITS = NavigationButton(self.Frame_TTS_Top)
        self.Button_VoiceConverter_Title_VITS.setObjectName(u"Button_VoiceConverter_Title_VITS")
        sizePolicy1.setHeightForWidth(self.Button_VoiceConverter_Title_VITS.sizePolicy().hasHeightForWidth())
        self.Button_VoiceConverter_Title_VITS.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.Button_VoiceConverter_Title_VITS)

        self.HorizontalSpacer_VoiceConverter_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.HorizontalSpacer_VoiceConverter_Title)

        self.Button_VoiceConverter_Help = QPushButton(self.Frame_TTS_Top)
        self.Button_VoiceConverter_Help.setObjectName(u"Button_VoiceConverter_Help")
        self.Button_VoiceConverter_Help.setMinimumSize(QSize(45, 45))
        self.Button_VoiceConverter_Help.setStyleSheet(u"QPushButton {\n"
"	image-position: center;\n"
"	image: url(:/Button_Icon/images/icons/Question.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_16.addWidget(self.Button_VoiceConverter_Help)


        self.verticalLayout_42.addWidget(self.Frame_TTS_Top)

        self.StackedWidget_Pages_TTS = QStackedWidget(self.Page_TTS)
        self.StackedWidget_Pages_TTS.setObjectName(u"StackedWidget_Pages_TTS")
        self.StackedWidget_Pages_TTS.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_TTS_GPTSoVITS = QWidget()
        self.Subpage_TTS_GPTSoVITS.setObjectName(u"Subpage_TTS_GPTSoVITS")
        self.gridLayout_109 = QGridLayout(self.Subpage_TTS_GPTSoVITS)
        self.gridLayout_109.setSpacing(12)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.gridLayout_109.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_TTS_GPTSoVITS = QWidget(self.Subpage_TTS_GPTSoVITS)
        self.Widget_Left_TTS_GPTSoVITS.setObjectName(u"Widget_Left_TTS_GPTSoVITS")
        self.Widget_Left_TTS_GPTSoVITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_TTS_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_69 = QVBoxLayout(self.Widget_Left_TTS_GPTSoVITS)
        self.verticalLayout_69.setSpacing(12)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_TTS_GPTSoVITS = TreeWidgetBase(self.Widget_Left_TTS_GPTSoVITS)
        __qtreewidgetitem6 = QTreeWidgetItem(self.TreeWidget_Catalogue_TTS_GPTSoVITS)
        QTreeWidgetItem(__qtreewidgetitem6)
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setObjectName(u"TreeWidget_Catalogue_TTS_GPTSoVITS")

        self.verticalLayout_69.addWidget(self.TreeWidget_Catalogue_TTS_GPTSoVITS)


        self.gridLayout_109.addWidget(self.Widget_Left_TTS_GPTSoVITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_TTS_GPTSoVITS = ScrollAreaBase(self.Subpage_TTS_GPTSoVITS)
        self.ScrollArea_Middle_TTS_GPTSoVITS.setObjectName(u"ScrollArea_Middle_TTS_GPTSoVITS")
        self.ScrollArea_Middle_TTS_GPTSoVITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_TTS_GPTSoVITS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_TTS_GPTSoVITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS.setObjectName(u"ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS")
        self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS.setGeometry(QRect(0, 0, 586, 602))
        self.verticalLayout_66 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)
        self.verticalLayout_66.setSpacing(12)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_TTS_GPTSoVITS_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)
        self.GroupBox_TTS_GPTSoVITS_InputParams.setObjectName(u"GroupBox_TTS_GPTSoVITS_InputParams")
        self.verticalLayout_125 = QVBoxLayout(self.GroupBox_TTS_GPTSoVITS_InputParams)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings = QFrame(self.GroupBox_TTS_GPTSoVITS_InputParams)
        self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings.setObjectName(u"Frame_TTS_GPTSoVITS_InputParams_BasicSettings")
        self.verticalLayout_70 = QVBoxLayout(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1 = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1.setObjectName(u"Frame_TTS_GPTSoVITS_ModelPathLoadS1")
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_97 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.gridLayout_97.setSpacing(12)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.gridLayout_97.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1 = LabelBase(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setObjectName(u"Label_TTS_GPTSoVITS_ModelPathLoadS1")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelPathLoadS1.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_97.addWidget(self.Label_TTS_GPTSoVITS_ModelPathLoadS1, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS1 = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_97.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS1, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_97.addWidget(self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1 = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelPathLoadS1")
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.setMinimumSize(QSize(0, 27))

        self.gridLayout_97.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1, 1, 0, 1, 3)


        self.verticalLayout_70.addWidget(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)

        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G.setObjectName(u"Frame_TTS_GPTSoVITS_ModelPathLoadS2G")
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_99 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.gridLayout_99.setSpacing(12)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.gridLayout_99.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G = LabelBase(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setObjectName(u"Label_TTS_GPTSoVITS_ModelPathLoadS2G")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_99.addWidget(self.Label_TTS_GPTSoVITS_ModelPathLoadS2G, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS2G = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_99.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS2G, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_99.addWidget(self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G")
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.setMinimumSize(QSize(0, 27))

        self.gridLayout_99.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G, 1, 0, 1, 3)


        self.verticalLayout_70.addWidget(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)

        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert.setObjectName(u"Frame_TTS_GPTSoVITS_ModelDirLoadBert")
        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_100 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.gridLayout_100.setSpacing(12)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gridLayout_100.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert = LabelBase(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setObjectName(u"Label_TTS_GPTSoVITS_ModelDirLoadBert")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelDirLoadBert.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_100.addWidget(self.Label_TTS_GPTSoVITS_ModelDirLoadBert, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadBert = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_100.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadBert, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_100.addWidget(self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelDirLoadBert")
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.setMinimumSize(QSize(0, 27))

        self.gridLayout_100.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert, 1, 0, 1, 3)


        self.verticalLayout_70.addWidget(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)

        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL.setObjectName(u"Frame_TTS_GPTSoVITS_ModelDirLoadSSL")
        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_101 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.gridLayout_101.setSpacing(12)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.gridLayout_101.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL = LabelBase(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setObjectName(u"Label_TTS_GPTSoVITS_ModelDirLoadSSL")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_101.addWidget(self.Label_TTS_GPTSoVITS_ModelDirLoadSSL, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadSSL = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_101.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadSSL, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_101.addWidget(self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL")
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.setMinimumSize(QSize(0, 27))

        self.gridLayout_101.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL, 1, 0, 1, 3)


        self.verticalLayout_70.addWidget(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)

        self.Frame_TTS_GPTSoVITS_UseWebUI = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_UseWebUI.setObjectName(u"Frame_TTS_GPTSoVITS_UseWebUI")
        self.Frame_TTS_GPTSoVITS_UseWebUI.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_UseWebUI.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_18 = QGridLayout(self.Frame_TTS_GPTSoVITS_UseWebUI)
        self.gridLayout_18.setSpacing(12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_UseWebUI = LabelBase(self.Frame_TTS_GPTSoVITS_UseWebUI)
        self.Label_TTS_GPTSoVITS_UseWebUI.setObjectName(u"Label_TTS_GPTSoVITS_UseWebUI")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_UseWebUI.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_UseWebUI.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_UseWebUI.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_18.addWidget(self.Label_TTS_GPTSoVITS_UseWebUI, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_UseWebUI = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_UseWebUI, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_UseWebUI_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_UseWebUI)
        self.Button_TTS_GPTSoVITS_UseWebUI_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_UseWebUI_MoreActions")
        self.Button_TTS_GPTSoVITS_UseWebUI_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_UseWebUI_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_UseWebUI_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_18.addWidget(self.Button_TTS_GPTSoVITS_UseWebUI_MoreActions, 0, 2, 1, 1)

        self.CheckBox_TTS_GPTSoVITS_UseWebUI = CheckBoxBase(self.Frame_TTS_GPTSoVITS_UseWebUI)
        self.CheckBox_TTS_GPTSoVITS_UseWebUI.setObjectName(u"CheckBox_TTS_GPTSoVITS_UseWebUI")
        self.CheckBox_TTS_GPTSoVITS_UseWebUI.setMinimumSize(QSize(0, 27))

        self.gridLayout_18.addWidget(self.CheckBox_TTS_GPTSoVITS_UseWebUI, 1, 0, 1, 3)


        self.verticalLayout_70.addWidget(self.Frame_TTS_GPTSoVITS_UseWebUI)


        self.verticalLayout_125.addWidget(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)


        self.verticalLayout_66.addWidget(self.GroupBox_TTS_GPTSoVITS_InputParams)

        self.VerticalSpacer_TTS_GPTSoVITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_66.addItem(self.VerticalSpacer_TTS_GPTSoVITS)

        self.ScrollArea_Middle_TTS_GPTSoVITS.setWidget(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)

        self.gridLayout_109.addWidget(self.ScrollArea_Middle_TTS_GPTSoVITS, 0, 1, 1, 1)

        self.Widget_Right_TTS_GPTSoVITS = QWidget(self.Subpage_TTS_GPTSoVITS)
        self.Widget_Right_TTS_GPTSoVITS.setObjectName(u"Widget_Right_TTS_GPTSoVITS")
        self.Widget_Right_TTS_GPTSoVITS.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_15 = QGridLayout(self.Widget_Right_TTS_GPTSoVITS)
        self.gridLayout_15.setSpacing(12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(12, 12, 12, 12)
        self.Button_ResetSettings_TTS_GPTSoVITS = HollowButton(self.Widget_Right_TTS_GPTSoVITS)
        self.Button_ResetSettings_TTS_GPTSoVITS.setObjectName(u"Button_ResetSettings_TTS_GPTSoVITS")

        self.gridLayout_15.addWidget(self.Button_ResetSettings_TTS_GPTSoVITS, 1, 0, 1, 1)

        self.TextBrowser_Params_TTS_GPTSoVITS = TextBrowserBase(self.Widget_Right_TTS_GPTSoVITS)
        self.TextBrowser_Params_TTS_GPTSoVITS.setObjectName(u"TextBrowser_Params_TTS_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_TTS_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_TTS_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_TTS_GPTSoVITS.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_15.addWidget(self.TextBrowser_Params_TTS_GPTSoVITS, 0, 0, 1, 3)

        self.Button_ExportSettings_TTS_GPTSoVITS = HollowButton(self.Widget_Right_TTS_GPTSoVITS)
        self.Button_ExportSettings_TTS_GPTSoVITS.setObjectName(u"Button_ExportSettings_TTS_GPTSoVITS")

        self.gridLayout_15.addWidget(self.Button_ExportSettings_TTS_GPTSoVITS, 1, 2, 1, 1)

        self.Button_ImportSettings_TTS_GPTSoVITS = HollowButton(self.Widget_Right_TTS_GPTSoVITS)
        self.Button_ImportSettings_TTS_GPTSoVITS.setObjectName(u"Button_ImportSettings_TTS_GPTSoVITS")

        self.gridLayout_15.addWidget(self.Button_ImportSettings_TTS_GPTSoVITS, 1, 1, 1, 1)


        self.gridLayout_109.addWidget(self.Widget_Right_TTS_GPTSoVITS, 0, 2, 1, 1)

        self.ProgressBar_TTS_GPTSoVITS = ProgressBarBase(self.Subpage_TTS_GPTSoVITS)
        self.ProgressBar_TTS_GPTSoVITS.setObjectName(u"ProgressBar_TTS_GPTSoVITS")
        self.ProgressBar_TTS_GPTSoVITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_TTS_GPTSoVITS.setValue(0)
        self.ProgressBar_TTS_GPTSoVITS.setTextVisible(False)
        self.horizontalLayout_56 = QHBoxLayout(self.ProgressBar_TTS_GPTSoVITS)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_TTS_GPTSoVITS = QStackedWidget(self.ProgressBar_TTS_GPTSoVITS)
        self.StackedWidget_TTS_GPTSoVITS.setObjectName(u"StackedWidget_TTS_GPTSoVITS")
        self.StackedWidget_TTS_GPTSoVITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_TTS_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_TTS_GPTSoVITS_Execute = QWidget()
        self.Page_TTS_GPTSoVITS_Execute.setObjectName(u"Page_TTS_GPTSoVITS_Execute")
        self.verticalLayout_136 = QVBoxLayout(self.Page_TTS_GPTSoVITS_Execute)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_GPTSoVITS_Execute = HollowButton(self.Page_TTS_GPTSoVITS_Execute)
        self.Button_TTS_GPTSoVITS_Execute.setObjectName(u"Button_TTS_GPTSoVITS_Execute")
        sizePolicy2.setHeightForWidth(self.Button_TTS_GPTSoVITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_TTS_GPTSoVITS_Execute.setSizePolicy(sizePolicy2)
        self.Button_TTS_GPTSoVITS_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_136.addWidget(self.Button_TTS_GPTSoVITS_Execute)

        self.StackedWidget_TTS_GPTSoVITS.addWidget(self.Page_TTS_GPTSoVITS_Execute)
        self.Page_TTS_GPTSoVITS_Terminate = QWidget()
        self.Page_TTS_GPTSoVITS_Terminate.setObjectName(u"Page_TTS_GPTSoVITS_Terminate")
        self.verticalLayout_138 = QVBoxLayout(self.Page_TTS_GPTSoVITS_Terminate)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_GPTSoVITS_Terminate = HollowButton(self.Page_TTS_GPTSoVITS_Terminate)
        self.Button_TTS_GPTSoVITS_Terminate.setObjectName(u"Button_TTS_GPTSoVITS_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_TTS_GPTSoVITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_TTS_GPTSoVITS_Terminate.setSizePolicy(sizePolicy2)
        self.Button_TTS_GPTSoVITS_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_138.addWidget(self.Button_TTS_GPTSoVITS_Terminate)

        self.StackedWidget_TTS_GPTSoVITS.addWidget(self.Page_TTS_GPTSoVITS_Terminate)

        self.horizontalLayout_56.addWidget(self.StackedWidget_TTS_GPTSoVITS)


        self.gridLayout_109.addWidget(self.ProgressBar_TTS_GPTSoVITS, 1, 0, 1, 3)

        self.gridLayout_109.setColumnStretch(0, 3)
        self.gridLayout_109.setColumnStretch(1, 10)
        self.gridLayout_109.setColumnStretch(2, 7)
        self.StackedWidget_Pages_TTS.addWidget(self.Subpage_TTS_GPTSoVITS)
        self.Subpage_TTS_VITS = QWidget()
        self.Subpage_TTS_VITS.setObjectName(u"Subpage_TTS_VITS")
        self.gridLayout_20 = QGridLayout(self.Subpage_TTS_VITS)
        self.gridLayout_20.setSpacing(12)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_TTS_VITS = QWidget(self.Subpage_TTS_VITS)
        self.Widget_Left_TTS_VITS.setObjectName(u"Widget_Left_TTS_VITS")
        self.Widget_Left_TTS_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_TTS_VITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.Widget_Left_TTS_VITS)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_TTS_VITS = TreeWidgetBase(self.Widget_Left_TTS_VITS)
        __qtreewidgetitem7 = QTreeWidgetItem(self.TreeWidget_Catalogue_TTS_VITS)
        QTreeWidgetItem(__qtreewidgetitem7)
        self.TreeWidget_Catalogue_TTS_VITS.setObjectName(u"TreeWidget_Catalogue_TTS_VITS")

        self.verticalLayout_11.addWidget(self.TreeWidget_Catalogue_TTS_VITS)


        self.gridLayout_20.addWidget(self.Widget_Left_TTS_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_TTS_VITS = ScrollAreaBase(self.Subpage_TTS_VITS)
        self.ScrollArea_Middle_TTS_VITS.setObjectName(u"ScrollArea_Middle_TTS_VITS")
        self.ScrollArea_Middle_TTS_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_TTS_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_TTS_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_TTS_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_TTS_VITS")
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setGeometry(QRect(0, 0, 586, 856))
        self.verticalLayout_19 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.verticalLayout_19.setSpacing(12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_TTS_VITS_InputParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_InputParams.setObjectName(u"GroupBox_TTS_VITS_InputParams")
        self.verticalLayout_120 = QVBoxLayout(self.GroupBox_TTS_VITS_InputParams)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_VITS_InputParams_BasicSettings = QFrame(self.GroupBox_TTS_VITS_InputParams)
        self.Frame_TTS_VITS_InputParams_BasicSettings.setObjectName(u"Frame_TTS_VITS_InputParams_BasicSettings")
        self.verticalLayout_132 = QVBoxLayout(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_ConfigPathLoad = QFrame(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.Frame_TTS_VITS_ConfigPathLoad.setObjectName(u"Frame_TTS_VITS_ConfigPathLoad")
        self.Frame_TTS_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_ConfigPathLoad.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_69 = QGridLayout(self.Frame_TTS_VITS_ConfigPathLoad)
        self.gridLayout_69.setSpacing(12)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_ConfigPathLoad = LabelBase(self.Frame_TTS_VITS_ConfigPathLoad)
        self.Label_TTS_VITS_ConfigPathLoad.setObjectName(u"Label_TTS_VITS_ConfigPathLoad")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_ConfigPathLoad.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_ConfigPathLoad.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_ConfigPathLoad.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_69.addWidget(self.Label_TTS_VITS_ConfigPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_ConfigPathLoad = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_69.addItem(self.HorizontalSpacer_TTS_VITS_ConfigPathLoad, 0, 1, 1, 1)

        self.Button_TTS_VITS_ConfigPathLoad_MoreActions = MenuButton(self.Frame_TTS_VITS_ConfigPathLoad)
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setObjectName(u"Button_TTS_VITS_ConfigPathLoad_MoreActions")
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_69.addWidget(self.Button_TTS_VITS_ConfigPathLoad_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_VITS_ConfigPathLoad = LineEditBase(self.Frame_TTS_VITS_ConfigPathLoad)
        self.LineEdit_TTS_VITS_ConfigPathLoad.setObjectName(u"LineEdit_TTS_VITS_ConfigPathLoad")
        self.LineEdit_TTS_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_69.addWidget(self.LineEdit_TTS_VITS_ConfigPathLoad, 1, 0, 1, 3)


        self.verticalLayout_132.addWidget(self.Frame_TTS_VITS_ConfigPathLoad)

        self.Frame_TTS_VITS_ModelPathLoad = QFrame(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.Frame_TTS_VITS_ModelPathLoad.setObjectName(u"Frame_TTS_VITS_ModelPathLoad")
        self.Frame_TTS_VITS_ModelPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_ModelPathLoad.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_70 = QGridLayout(self.Frame_TTS_VITS_ModelPathLoad)
        self.gridLayout_70.setSpacing(12)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_ModelPathLoad = LabelBase(self.Frame_TTS_VITS_ModelPathLoad)
        self.Label_TTS_VITS_ModelPathLoad.setObjectName(u"Label_TTS_VITS_ModelPathLoad")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_ModelPathLoad.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_ModelPathLoad.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_ModelPathLoad.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_70.addWidget(self.Label_TTS_VITS_ModelPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_ModelPathLoad = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_70.addItem(self.HorizontalSpacer_TTS_VITS_ModelPathLoad, 0, 1, 1, 1)

        self.Button_TTS_VITS_ModelPathLoad_MoreActions = MenuButton(self.Frame_TTS_VITS_ModelPathLoad)
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setObjectName(u"Button_TTS_VITS_ModelPathLoad_MoreActions")
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_70.addWidget(self.Button_TTS_VITS_ModelPathLoad_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_VITS_ModelPathLoad = LineEditBase(self.Frame_TTS_VITS_ModelPathLoad)
        self.LineEdit_TTS_VITS_ModelPathLoad.setObjectName(u"LineEdit_TTS_VITS_ModelPathLoad")
        self.LineEdit_TTS_VITS_ModelPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_70.addWidget(self.LineEdit_TTS_VITS_ModelPathLoad, 1, 0, 1, 3)


        self.verticalLayout_132.addWidget(self.Frame_TTS_VITS_ModelPathLoad)


        self.verticalLayout_120.addWidget(self.Frame_TTS_VITS_InputParams_BasicSettings)


        self.verticalLayout_19.addWidget(self.GroupBox_TTS_VITS_InputParams)

        self.GroupBox_TTS_VITS_VITSParams = GroupBoxBase(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_VITSParams.setObjectName(u"GroupBox_TTS_VITS_VITSParams")
        self.verticalLayout_117 = QVBoxLayout(self.GroupBox_TTS_VITS_VITSParams)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_VITS_VITSParams_BasicSettings = QFrame(self.GroupBox_TTS_VITS_VITSParams)
        self.Frame_TTS_VITS_VITSParams_BasicSettings.setObjectName(u"Frame_TTS_VITS_VITSParams_BasicSettings")
        self.verticalLayout_131 = QVBoxLayout(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_Text = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Text.setObjectName(u"Frame_TTS_VITS_Text")
        self.Frame_TTS_VITS_Text.setMinimumSize(QSize(0, 222))
        self.Frame_TTS_VITS_Text.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.verticalLayout_98 = QVBoxLayout(self.Frame_TTS_VITS_Text)
        self.verticalLayout_98.setSpacing(12)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Text = LabelBase(self.Frame_TTS_VITS_Text)
        self.Label_TTS_VITS_Text.setObjectName(u"Label_TTS_VITS_Text")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_Text.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Text.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_Text.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_98.addWidget(self.Label_TTS_VITS_Text)

        self.PlainTextEdit_TTS_VITS_Text = TextEditBase(self.Frame_TTS_VITS_Text)
        self.PlainTextEdit_TTS_VITS_Text.setObjectName(u"PlainTextEdit_TTS_VITS_Text")
        sizePolicy2.setHeightForWidth(self.PlainTextEdit_TTS_VITS_Text.sizePolicy().hasHeightForWidth())
        self.PlainTextEdit_TTS_VITS_Text.setSizePolicy(sizePolicy2)

        self.verticalLayout_98.addWidget(self.PlainTextEdit_TTS_VITS_Text)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Text)

        self.Frame_TTS_VITS_Language = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Language.setObjectName(u"Frame_TTS_VITS_Language")
        self.Frame_TTS_VITS_Language.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Language.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_79 = QGridLayout(self.Frame_TTS_VITS_Language)
        self.gridLayout_79.setSpacing(12)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.gridLayout_79.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Language = LabelBase(self.Frame_TTS_VITS_Language)
        self.Label_TTS_VITS_Language.setObjectName(u"Label_TTS_VITS_Language")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_Language.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Language.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_79.addWidget(self.Label_TTS_VITS_Language, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_Language = QSpacerItem(415, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_79.addItem(self.HorizontalSpacer_TTS_VITS_Language, 0, 1, 1, 1)

        self.Button_TTS_VITS_Language_MoreActions = MenuButton(self.Frame_TTS_VITS_Language)
        self.Button_TTS_VITS_Language_MoreActions.setObjectName(u"Button_TTS_VITS_Language_MoreActions")
        self.Button_TTS_VITS_Language_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_Language_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_Language_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_79.addWidget(self.Button_TTS_VITS_Language_MoreActions, 0, 2, 1, 1)

        self.ComboBox_TTS_VITS_Language = ComboBoxBase(self.Frame_TTS_VITS_Language)
        self.ComboBox_TTS_VITS_Language.setObjectName(u"ComboBox_TTS_VITS_Language")
        self.ComboBox_TTS_VITS_Language.setMinimumSize(QSize(0, 27))

        self.gridLayout_79.addWidget(self.ComboBox_TTS_VITS_Language, 1, 0, 1, 3)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Language)

        self.Frame_TTS_VITS_Speaker = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Speaker.setObjectName(u"Frame_TTS_VITS_Speaker")
        self.Frame_TTS_VITS_Speaker.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Speaker.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.verticalLayout_104 = QVBoxLayout(self.Frame_TTS_VITS_Speaker)
        self.verticalLayout_104.setSpacing(12)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Speaker = LabelBase(self.Frame_TTS_VITS_Speaker)
        self.Label_TTS_VITS_Speaker.setObjectName(u"Label_TTS_VITS_Speaker")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_Speaker.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Speaker.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_Speaker.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_104.addWidget(self.Label_TTS_VITS_Speaker)

        self.ComboBox_TTS_VITS_Speaker = ComboBoxBase(self.Frame_TTS_VITS_Speaker)
        self.ComboBox_TTS_VITS_Speaker.setObjectName(u"ComboBox_TTS_VITS_Speaker")
        self.ComboBox_TTS_VITS_Speaker.setMinimumSize(QSize(0, 27))

        self.verticalLayout_104.addWidget(self.ComboBox_TTS_VITS_Speaker)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Speaker)


        self.verticalLayout_117.addWidget(self.Frame_TTS_VITS_VITSParams_BasicSettings)

        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_TTS_VITS_VITSParams)
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.setObjectName(u"ToolBox_TTS_VITS_VITSParams_AdvanceSettings")
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 315))
        self.verticalLayout_118 = QVBoxLayout(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_EmotionStrength = QFrame(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_TTS_VITS_EmotionStrength.setObjectName(u"Frame_TTS_VITS_EmotionStrength")
        self.Frame_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_71 = QGridLayout(self.Frame_TTS_VITS_EmotionStrength)
        self.gridLayout_71.setSpacing(12)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_EmotionStrength = LabelBase(self.Frame_TTS_VITS_EmotionStrength)
        self.Label_TTS_VITS_EmotionStrength.setObjectName(u"Label_TTS_VITS_EmotionStrength")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_EmotionStrength.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_71.addWidget(self.Label_TTS_VITS_EmotionStrength, 0, 0, 1, 1)

        self.Button_TTS_VITS_EmotionStrength_MoreActions = MenuButton(self.Frame_TTS_VITS_EmotionStrength)
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setObjectName(u"Button_TTS_VITS_EmotionStrength_MoreActions")
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_71.addWidget(self.Button_TTS_VITS_EmotionStrength_MoreActions, 0, 2, 1, 1)

        self.HorizontalSpacer_TTS_VITS_EmotionStrength = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_71.addItem(self.HorizontalSpacer_TTS_VITS_EmotionStrength, 0, 1, 1, 1)

        self.ChildFrame_TTS_VITS_EmotionStrength = QFrame(self.Frame_TTS_VITS_EmotionStrength)
        self.ChildFrame_TTS_VITS_EmotionStrength.setObjectName(u"ChildFrame_TTS_VITS_EmotionStrength")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_43 = QHBoxLayout(self.ChildFrame_TTS_VITS_EmotionStrength)
        self.horizontalLayout_43.setSpacing(12)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_TTS_VITS_EmotionStrength = Frame_RangeSetting(self.ChildFrame_TTS_VITS_EmotionStrength)
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setObjectName(u"HorizontalSlider_TTS_VITS_EmotionStrength")
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 27))
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_43.addWidget(self.HorizontalSlider_TTS_VITS_EmotionStrength)


        self.gridLayout_71.addWidget(self.ChildFrame_TTS_VITS_EmotionStrength, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_EmotionStrength)

        self.Frame_TTS_VITS_PhonemeDuration = QFrame(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_TTS_VITS_PhonemeDuration.setObjectName(u"Frame_TTS_VITS_PhonemeDuration")
        self.Frame_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_72 = QGridLayout(self.Frame_TTS_VITS_PhonemeDuration)
        self.gridLayout_72.setSpacing(12)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_PhonemeDuration = LabelBase(self.Frame_TTS_VITS_PhonemeDuration)
        self.Label_TTS_VITS_PhonemeDuration.setObjectName(u"Label_TTS_VITS_PhonemeDuration")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_PhonemeDuration.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_72.addWidget(self.Label_TTS_VITS_PhonemeDuration, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_PhonemeDuration = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_72.addItem(self.HorizontalSpacer_TTS_VITS_PhonemeDuration, 0, 1, 1, 1)

        self.Button_TTS_VITS_PhonemeDuration_MoreActions = MenuButton(self.Frame_TTS_VITS_PhonemeDuration)
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setObjectName(u"Button_TTS_VITS_PhonemeDuration_MoreActions")
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_72.addWidget(self.Button_TTS_VITS_PhonemeDuration_MoreActions, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_PhonemeDuration = QFrame(self.Frame_TTS_VITS_PhonemeDuration)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setObjectName(u"ChildFrame_TTS_VITS_PhonemeDuration")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.ChildFrame_TTS_VITS_PhonemeDuration)
        self.horizontalLayout_44.setSpacing(12)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_TTS_VITS_PhonemeDuration = Frame_RangeSetting(self.ChildFrame_TTS_VITS_PhonemeDuration)
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setObjectName(u"HorizontalSlider_TTS_VITS_PhonemeDuration")
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 27))
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_44.addWidget(self.HorizontalSlider_TTS_VITS_PhonemeDuration)


        self.gridLayout_72.addWidget(self.ChildFrame_TTS_VITS_PhonemeDuration, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_PhonemeDuration)

        self.Frame_TTS_VITS_SpeechRate = QFrame(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_TTS_VITS_SpeechRate.setObjectName(u"Frame_TTS_VITS_SpeechRate")
        self.Frame_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_73 = QGridLayout(self.Frame_TTS_VITS_SpeechRate)
        self.gridLayout_73.setSpacing(12)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_SpeechRate = LabelBase(self.Frame_TTS_VITS_SpeechRate)
        self.Label_TTS_VITS_SpeechRate.setObjectName(u"Label_TTS_VITS_SpeechRate")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_SpeechRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_73.addWidget(self.Label_TTS_VITS_SpeechRate, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_SpeechRate = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_73.addItem(self.HorizontalSpacer_TTS_VITS_SpeechRate, 0, 1, 1, 1)

        self.Button_TTS_VITS_SpeechRate_MoreActions = MenuButton(self.Frame_TTS_VITS_SpeechRate)
        self.Button_TTS_VITS_SpeechRate_MoreActions.setObjectName(u"Button_TTS_VITS_SpeechRate_MoreActions")
        self.Button_TTS_VITS_SpeechRate_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_SpeechRate_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_SpeechRate_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_73.addWidget(self.Button_TTS_VITS_SpeechRate_MoreActions, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_SpeechRate = QFrame(self.Frame_TTS_VITS_SpeechRate)
        self.ChildFrame_TTS_VITS_SpeechRate.setObjectName(u"ChildFrame_TTS_VITS_SpeechRate")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_45 = QHBoxLayout(self.ChildFrame_TTS_VITS_SpeechRate)
        self.horizontalLayout_45.setSpacing(12)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_TTS_VITS_SpeechRate = Frame_RangeSetting(self.ChildFrame_TTS_VITS_SpeechRate)
        self.HorizontalSlider_TTS_VITS_SpeechRate.setObjectName(u"HorizontalSlider_TTS_VITS_SpeechRate")
        self.HorizontalSlider_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 27))
        self.HorizontalSlider_TTS_VITS_SpeechRate.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_45.addWidget(self.HorizontalSlider_TTS_VITS_SpeechRate)


        self.gridLayout_73.addWidget(self.ChildFrame_TTS_VITS_SpeechRate, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_SpeechRate)

        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.addItem(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_117.addWidget(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_19.addWidget(self.GroupBox_TTS_VITS_VITSParams)

        self.VerticalSpacer_TTS_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.VerticalSpacer_TTS_VITS)

        self.ScrollArea_Middle_TTS_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_TTS_VITS)

        self.gridLayout_20.addWidget(self.ScrollArea_Middle_TTS_VITS, 0, 1, 1, 1)

        self.Widget_Right_TTS_VITS = QWidget(self.Subpage_TTS_VITS)
        self.Widget_Right_TTS_VITS.setObjectName(u"Widget_Right_TTS_VITS")
        self.Widget_Right_TTS_VITS.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_16 = QGridLayout(self.Widget_Right_TTS_VITS)
        self.gridLayout_16.setSpacing(12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_TTS_VITS = TextBrowserBase(self.Widget_Right_TTS_VITS)
        self.TextBrowser_Params_TTS_VITS.setObjectName(u"TextBrowser_Params_TTS_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_TTS_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_TTS_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_TTS_VITS.setStyleSheet(u"QTextBrowser {\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_16.addWidget(self.TextBrowser_Params_TTS_VITS, 0, 0, 1, 3)

        self.Button_ResetSettings_TTS_VITS = HollowButton(self.Widget_Right_TTS_VITS)
        self.Button_ResetSettings_TTS_VITS.setObjectName(u"Button_ResetSettings_TTS_VITS")

        self.gridLayout_16.addWidget(self.Button_ResetSettings_TTS_VITS, 1, 0, 1, 1)

        self.Button_ImportSettings_TTS_VITS = HollowButton(self.Widget_Right_TTS_VITS)
        self.Button_ImportSettings_TTS_VITS.setObjectName(u"Button_ImportSettings_TTS_VITS")

        self.gridLayout_16.addWidget(self.Button_ImportSettings_TTS_VITS, 1, 1, 1, 1)

        self.Button_ExportSettings_TTS_VITS = HollowButton(self.Widget_Right_TTS_VITS)
        self.Button_ExportSettings_TTS_VITS.setObjectName(u"Button_ExportSettings_TTS_VITS")

        self.gridLayout_16.addWidget(self.Button_ExportSettings_TTS_VITS, 1, 2, 1, 1)

        self.Button_CheckOutput_TTS_VITS = HollowButton(self.Widget_Right_TTS_VITS)
        self.Button_CheckOutput_TTS_VITS.setObjectName(u"Button_CheckOutput_TTS_VITS")

        self.gridLayout_16.addWidget(self.Button_CheckOutput_TTS_VITS, 2, 0, 1, 3)


        self.gridLayout_20.addWidget(self.Widget_Right_TTS_VITS, 0, 2, 1, 1)

        self.ProgressBar_TTS_VITS = ProgressBarBase(self.Subpage_TTS_VITS)
        self.ProgressBar_TTS_VITS.setObjectName(u"ProgressBar_TTS_VITS")
        self.ProgressBar_TTS_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_TTS_VITS.setValue(0)
        self.ProgressBar_TTS_VITS.setTextVisible(False)
        self.horizontalLayout_48 = QHBoxLayout(self.ProgressBar_TTS_VITS)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_TTS_VITS = QStackedWidget(self.ProgressBar_TTS_VITS)
        self.StackedWidget_TTS_VITS.setObjectName(u"StackedWidget_TTS_VITS")
        self.StackedWidget_TTS_VITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_TTS_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_TTS_VITS_Execute = QWidget()
        self.Page_TTS_VITS_Execute.setObjectName(u"Page_TTS_VITS_Execute")
        self.verticalLayout_112 = QVBoxLayout(self.Page_TTS_VITS_Execute)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_VITS_Execute = HollowButton(self.Page_TTS_VITS_Execute)
        self.Button_TTS_VITS_Execute.setObjectName(u"Button_TTS_VITS_Execute")
        sizePolicy2.setHeightForWidth(self.Button_TTS_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_TTS_VITS_Execute.setSizePolicy(sizePolicy2)
        self.Button_TTS_VITS_Execute.setMinimumSize(QSize(0, 30))

        self.verticalLayout_112.addWidget(self.Button_TTS_VITS_Execute)

        self.StackedWidget_TTS_VITS.addWidget(self.Page_TTS_VITS_Execute)
        self.Page_TTS_VITS_Terminate = QWidget()
        self.Page_TTS_VITS_Terminate.setObjectName(u"Page_TTS_VITS_Terminate")
        self.verticalLayout_113 = QVBoxLayout(self.Page_TTS_VITS_Terminate)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_VITS_Terminate = HollowButton(self.Page_TTS_VITS_Terminate)
        self.Button_TTS_VITS_Terminate.setObjectName(u"Button_TTS_VITS_Terminate")
        sizePolicy2.setHeightForWidth(self.Button_TTS_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_TTS_VITS_Terminate.setSizePolicy(sizePolicy2)
        self.Button_TTS_VITS_Terminate.setMinimumSize(QSize(0, 30))

        self.verticalLayout_113.addWidget(self.Button_TTS_VITS_Terminate)

        self.StackedWidget_TTS_VITS.addWidget(self.Page_TTS_VITS_Terminate)

        self.horizontalLayout_48.addWidget(self.StackedWidget_TTS_VITS)


        self.gridLayout_20.addWidget(self.ProgressBar_TTS_VITS, 1, 0, 1, 3)

        self.gridLayout_20.setColumnStretch(0, 3)
        self.gridLayout_20.setColumnStretch(1, 10)
        self.gridLayout_20.setColumnStretch(2, 7)
        self.StackedWidget_Pages_TTS.addWidget(self.Subpage_TTS_VITS)

        self.verticalLayout_42.addWidget(self.StackedWidget_Pages_TTS)

        self.StackedWidget_Pages.addWidget(self.Page_TTS)
        self.Page_Settings = QWidget()
        self.Page_Settings.setObjectName(u"Page_Settings")
        self.verticalLayout_78 = QVBoxLayout(self.Page_Settings)
        self.verticalLayout_78.setSpacing(21)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(21, 12, 21, 12)
        self.Frame_Settings_Top = QFrame(self.Page_Settings)
        self.Frame_Settings_Top.setObjectName(u"Frame_Settings_Top")
        self.Frame_Settings_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Settings_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Settings_Top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Button_Settings_Title_Client = NavigationButton(self.Frame_Settings_Top)
        self.Button_Settings_Title_Client.setObjectName(u"Button_Settings_Title_Client")
        sizePolicy1.setHeightForWidth(self.Button_Settings_Title_Client.sizePolicy().hasHeightForWidth())
        self.Button_Settings_Title_Client.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.Button_Settings_Title_Client)

        self.Button_Settings_Title_Tools = NavigationButton(self.Frame_Settings_Top)
        self.Button_Settings_Title_Tools.setObjectName(u"Button_Settings_Title_Tools")
        sizePolicy1.setHeightForWidth(self.Button_Settings_Title_Tools.sizePolicy().hasHeightForWidth())
        self.Button_Settings_Title_Tools.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.Button_Settings_Title_Tools)

        self.Frame_Settings_Title_Spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.Frame_Settings_Title_Spacer)


        self.verticalLayout_78.addWidget(self.Frame_Settings_Top)

        self.StackedWidget_Pages_Settings = QStackedWidget(self.Page_Settings)
        self.StackedWidget_Pages_Settings.setObjectName(u"StackedWidget_Pages_Settings")
        self.StackedWidget_Pages_Settings.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.SubPage_Settings_Client = QWidget()
        self.SubPage_Settings_Client.setObjectName(u"SubPage_Settings_Client")
        self.gridLayout_80 = QGridLayout(self.SubPage_Settings_Client)
        self.gridLayout_80.setSpacing(12)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gridLayout_80.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Settings_Client = ScrollAreaBase(self.SubPage_Settings_Client)
        self.ScrollArea_Settings_Client.setObjectName(u"ScrollArea_Settings_Client")
        self.ScrollArea_Settings_Client.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Settings_Client = QWidget()
        self.ScrollAreaWidgetContents_Settings_Client.setObjectName(u"ScrollAreaWidgetContents_Settings_Client")
        self.ScrollAreaWidgetContents_Settings_Client.setGeometry(QRect(0, 0, 246, 483))
        self.verticalLayout_106 = QVBoxLayout(self.ScrollAreaWidgetContents_Settings_Client)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Settings_Client_Outlook = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Outlook.setObjectName(u"GroupBox_Settings_Client_Outlook")
        self.verticalLayout_13 = QVBoxLayout(self.GroupBox_Settings_Client_Outlook)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_Theme = QFrame(self.GroupBox_Settings_Client_Outlook)
        self.Frame_Setting_Theme.setObjectName(u"Frame_Setting_Theme")
        self.Frame_Setting_Theme.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Theme.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_72 = QHBoxLayout(self.Frame_Setting_Theme)
        self.horizontalLayout_72.setSpacing(12)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Theme = LabelBase(self.Frame_Setting_Theme)
        self.Label_Setting_Theme.setObjectName(u"Label_Setting_Theme")
        sizePolicy4.setHeightForWidth(self.Label_Setting_Theme.sizePolicy().hasHeightForWidth())
        self.Label_Setting_Theme.setSizePolicy(sizePolicy4)
        self.Label_Setting_Theme.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_72.addWidget(self.Label_Setting_Theme)

        self.ComboBox_Setting_Theme = ComboBoxBase(self.Frame_Setting_Theme)
        self.ComboBox_Setting_Theme.setObjectName(u"ComboBox_Setting_Theme")
        self.ComboBox_Setting_Theme.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_72.addWidget(self.ComboBox_Setting_Theme)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Theme)

        self.Frame_Setting_Language = QFrame(self.GroupBox_Settings_Client_Outlook)
        self.Frame_Setting_Language.setObjectName(u"Frame_Setting_Language")
        self.Frame_Setting_Language.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Language.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_66 = QHBoxLayout(self.Frame_Setting_Language)
        self.horizontalLayout_66.setSpacing(12)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Language = LabelBase(self.Frame_Setting_Language)
        self.Label_Setting_Language.setObjectName(u"Label_Setting_Language")
        sizePolicy4.setHeightForWidth(self.Label_Setting_Language.sizePolicy().hasHeightForWidth())
        self.Label_Setting_Language.setSizePolicy(sizePolicy4)
        self.Label_Setting_Language.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_66.addWidget(self.Label_Setting_Language)

        self.ComboBox_Setting_Language = ComboBoxBase(self.Frame_Setting_Language)
        self.ComboBox_Setting_Language.setObjectName(u"ComboBox_Setting_Language")
        self.ComboBox_Setting_Language.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_66.addWidget(self.ComboBox_Setting_Language)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Language)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Outlook)

        self.GroupBox_Settings_Client_Function = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Function.setObjectName(u"GroupBox_Settings_Client_Function")
        self.verticalLayout_84 = QVBoxLayout(self.GroupBox_Settings_Client_Function)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_AutoUpdate = QFrame(self.GroupBox_Settings_Client_Function)
        self.Frame_Setting_AutoUpdate.setObjectName(u"Frame_Setting_AutoUpdate")
        self.Frame_Setting_AutoUpdate.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_AutoUpdate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_65 = QHBoxLayout(self.Frame_Setting_AutoUpdate)
        self.horizontalLayout_65.setSpacing(12)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_AutoUpdate = LabelBase(self.Frame_Setting_AutoUpdate)
        self.Label_Setting_AutoUpdate.setObjectName(u"Label_Setting_AutoUpdate")
        sizePolicy4.setHeightForWidth(self.Label_Setting_AutoUpdate.sizePolicy().hasHeightForWidth())
        self.Label_Setting_AutoUpdate.setSizePolicy(sizePolicy4)
        self.Label_Setting_AutoUpdate.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_65.addWidget(self.Label_Setting_AutoUpdate)

        self.CheckBox_Setting_AutoUpdate = CheckBoxBase(self.Frame_Setting_AutoUpdate)
        self.CheckBox_Setting_AutoUpdate.setObjectName(u"CheckBox_Setting_AutoUpdate")
        self.CheckBox_Setting_AutoUpdate.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_65.addWidget(self.CheckBox_Setting_AutoUpdate)


        self.verticalLayout_84.addWidget(self.Frame_Setting_AutoUpdate)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Function)

        self.GroupBox_Settings_Client_Operation = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Operation.setObjectName(u"GroupBox_Settings_Client_Operation")
        self.verticalLayout_85 = QVBoxLayout(self.GroupBox_Settings_Client_Operation)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_Operation = QFrame(self.GroupBox_Settings_Client_Operation)
        self.Frame_Setting_Operation.setObjectName(u"Frame_Setting_Operation")
        self.Frame_Setting_Operation.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Operation.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.Frame_Setting_Operation)
        self.horizontalLayout_6.setSpacing(42)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(21, 12, 21, 12)
        self.Button_Setting_IntegrityChecker = HollowButton(self.Frame_Setting_Operation)
        self.Button_Setting_IntegrityChecker.setObjectName(u"Button_Setting_IntegrityChecker")

        self.horizontalLayout_6.addWidget(self.Button_Setting_IntegrityChecker)

        self.HorizontalSpacer_Setting_Operation = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.HorizontalSpacer_Setting_Operation)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 6)

        self.verticalLayout_85.addWidget(self.Frame_Setting_Operation)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Operation)

        self.VerticalSpacer_Settings_Client = QSpacerItem(20, 174, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_106.addItem(self.VerticalSpacer_Settings_Client)

        self.ScrollArea_Settings_Client.setWidget(self.ScrollAreaWidgetContents_Settings_Client)

        self.gridLayout_80.addWidget(self.ScrollArea_Settings_Client, 0, 0, 1, 1)

        self.StackedWidget_Pages_Settings.addWidget(self.SubPage_Settings_Client)
        self.SubPage_Settings_Tools = QWidget()
        self.SubPage_Settings_Tools.setObjectName(u"SubPage_Settings_Tools")
        self.gridLayout_93 = QGridLayout(self.SubPage_Settings_Tools)
        self.gridLayout_93.setSpacing(12)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.gridLayout_93.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Settings_Tools = ScrollAreaBase(self.SubPage_Settings_Tools)
        self.ScrollArea_Settings_Tools.setObjectName(u"ScrollArea_Settings_Tools")
        self.ScrollArea_Settings_Tools.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Settings_Tools = QWidget()
        self.ScrollAreaWidgetContents_Settings_Tools.setObjectName(u"ScrollAreaWidgetContents_Settings_Tools")
        self.ScrollAreaWidgetContents_Settings_Tools.setGeometry(QRect(0, 0, 246, 907))
        self.verticalLayout_34 = QVBoxLayout(self.ScrollAreaWidgetContents_Settings_Tools)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Settings_Tools_Function = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Tools)
        self.GroupBox_Settings_Tools_Function.setObjectName(u"GroupBox_Settings_Tools_Function")
        self.verticalLayout_76 = QVBoxLayout(self.GroupBox_Settings_Tools_Function)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_AutoReset = QFrame(self.GroupBox_Settings_Tools_Function)
        self.Frame_Setting_AutoReset.setObjectName(u"Frame_Setting_AutoReset")
        self.Frame_Setting_AutoReset.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_AutoReset.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_75 = QHBoxLayout(self.Frame_Setting_AutoReset)
        self.horizontalLayout_75.setSpacing(12)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_AutoReset = LabelBase(self.Frame_Setting_AutoReset)
        self.Label_Setting_AutoReset.setObjectName(u"Label_Setting_AutoReset")
        sizePolicy4.setHeightForWidth(self.Label_Setting_AutoReset.sizePolicy().hasHeightForWidth())
        self.Label_Setting_AutoReset.setSizePolicy(sizePolicy4)
        self.Label_Setting_AutoReset.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_75.addWidget(self.Label_Setting_AutoReset)

        self.CheckBox_Setting_AutoReset = CheckBoxBase(self.Frame_Setting_AutoReset)
        self.CheckBox_Setting_AutoReset.setObjectName(u"CheckBox_Setting_AutoReset")
        self.CheckBox_Setting_AutoReset.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_75.addWidget(self.CheckBox_Setting_AutoReset)


        self.verticalLayout_76.addWidget(self.Frame_Setting_AutoReset)

        self.Frame_Setting_Synchronizer = QFrame(self.GroupBox_Settings_Tools_Function)
        self.Frame_Setting_Synchronizer.setObjectName(u"Frame_Setting_Synchronizer")
        self.Frame_Setting_Synchronizer.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Synchronizer.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_74 = QHBoxLayout(self.Frame_Setting_Synchronizer)
        self.horizontalLayout_74.setSpacing(12)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Synchronizer = LabelBase(self.Frame_Setting_Synchronizer)
        self.Label_Setting_Synchronizer.setObjectName(u"Label_Setting_Synchronizer")
        sizePolicy4.setHeightForWidth(self.Label_Setting_Synchronizer.sizePolicy().hasHeightForWidth())
        self.Label_Setting_Synchronizer.setSizePolicy(sizePolicy4)
        self.Label_Setting_Synchronizer.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_74.addWidget(self.Label_Setting_Synchronizer)

        self.CheckBox_Setting_Synchronizer = CheckBoxBase(self.Frame_Setting_Synchronizer)
        self.CheckBox_Setting_Synchronizer.setObjectName(u"CheckBox_Setting_Synchronizer")
        self.CheckBox_Setting_Synchronizer.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_74.addWidget(self.CheckBox_Setting_Synchronizer)


        self.verticalLayout_76.addWidget(self.Frame_Setting_Synchronizer)


        self.verticalLayout_34.addWidget(self.GroupBox_Settings_Tools_Function)

        self.GroupBox_Settings_Tools_Path = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Tools)
        self.GroupBox_Settings_Tools_Path.setObjectName(u"GroupBox_Settings_Tools_Path")
        self.verticalLayout_83 = QVBoxLayout(self.GroupBox_Settings_Tools_Path)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_Process_OutputRoot.setObjectName(u"Frame_Process_OutputRoot")
        self.Frame_Process_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_Process_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.Frame_Process_OutputRoot)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_OutputRoot = LabelBase(self.Frame_Process_OutputRoot)
        self.Label_Process_OutputRoot.setObjectName(u"Label_Process_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_Process_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_Process_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_Process_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_19.addWidget(self.Label_Process_OutputRoot)

        self.LineEdit_Process_OutputRoot = LineEditBase(self.Frame_Process_OutputRoot)
        self.LineEdit_Process_OutputRoot.setObjectName(u"LineEdit_Process_OutputRoot")
        self.LineEdit_Process_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_19.addWidget(self.LineEdit_Process_OutputRoot)

        self.Button_Process_OutputRoot_MoreActions = MenuButton(self.Frame_Process_OutputRoot)
        self.Button_Process_OutputRoot_MoreActions.setObjectName(u"Button_Process_OutputRoot_MoreActions")
        self.Button_Process_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_Process_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_19.addWidget(self.Button_Process_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_Process_OutputRoot)

        self.Frame_VPR_TDNN_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_VPR_TDNN_OutputRoot.setObjectName(u"Frame_VPR_TDNN_OutputRoot")
        self.Frame_VPR_TDNN_OutputRoot.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.Frame_VPR_TDNN_OutputRoot)
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_OutputRoot = LabelBase(self.Frame_VPR_TDNN_OutputRoot)
        self.Label_VPR_TDNN_OutputRoot.setObjectName(u"Label_VPR_TDNN_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_VPR_TDNN_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_VPR_TDNN_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_25.addWidget(self.Label_VPR_TDNN_OutputRoot)

        self.LineEdit_VPR_TDNN_OutputRoot = LineEditBase(self.Frame_VPR_TDNN_OutputRoot)
        self.LineEdit_VPR_TDNN_OutputRoot.setObjectName(u"LineEdit_VPR_TDNN_OutputRoot")
        self.LineEdit_VPR_TDNN_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_25.addWidget(self.LineEdit_VPR_TDNN_OutputRoot)

        self.Button_VPR_TDNN_OutputRoot_MoreActions = MenuButton(self.Frame_VPR_TDNN_OutputRoot)
        self.Button_VPR_TDNN_OutputRoot_MoreActions.setObjectName(u"Button_VPR_TDNN_OutputRoot_MoreActions")
        self.Button_VPR_TDNN_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_VPR_TDNN_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_25.addWidget(self.Button_VPR_TDNN_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_VPR_TDNN_OutputRoot)

        self.Frame_ASR_Whisper_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_ASR_Whisper_OutputRoot.setObjectName(u"Frame_ASR_Whisper_OutputRoot")
        self.Frame_ASR_Whisper_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_ASR_Whisper_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.Frame_ASR_Whisper_OutputRoot)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_OutputRoot = LabelBase(self.Frame_ASR_Whisper_OutputRoot)
        self.Label_ASR_Whisper_OutputRoot.setObjectName(u"Label_ASR_Whisper_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_ASR_Whisper_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_ASR_Whisper_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_20.addWidget(self.Label_ASR_Whisper_OutputRoot)

        self.LineEdit_ASR_Whisper_OutputRoot = LineEditBase(self.Frame_ASR_Whisper_OutputRoot)
        self.LineEdit_ASR_Whisper_OutputRoot.setObjectName(u"LineEdit_ASR_Whisper_OutputRoot")
        self.LineEdit_ASR_Whisper_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_20.addWidget(self.LineEdit_ASR_Whisper_OutputRoot)

        self.Button_ASR_Whisper_OutputRoot_MoreActions = MenuButton(self.Frame_ASR_Whisper_OutputRoot)
        self.Button_ASR_Whisper_OutputRoot_MoreActions.setObjectName(u"Button_ASR_Whisper_OutputRoot_MoreActions")
        self.Button_ASR_Whisper_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_ASR_Whisper_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_20.addWidget(self.Button_ASR_Whisper_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_ASR_Whisper_OutputRoot)

        self.Frame_DAT_GPTSoVITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_DAT_GPTSoVITS_OutputRoot.setObjectName(u"Frame_DAT_GPTSoVITS_OutputRoot")
        self.Frame_DAT_GPTSoVITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_DAT_GPTSoVITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.horizontalLayout_21.setSpacing(12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_OutputRoot = LabelBase(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.Label_DAT_GPTSoVITS_OutputRoot.setObjectName(u"Label_DAT_GPTSoVITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_DAT_GPTSoVITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_DAT_GPTSoVITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_21.addWidget(self.Label_DAT_GPTSoVITS_OutputRoot)

        self.LineEdit_DAT_GPTSoVITS_OutputRoot = LineEditBase(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.LineEdit_DAT_GPTSoVITS_OutputRoot.setObjectName(u"LineEdit_DAT_GPTSoVITS_OutputRoot")
        self.LineEdit_DAT_GPTSoVITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.LineEdit_DAT_GPTSoVITS_OutputRoot)

        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_OutputRoot_MoreActions")
        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_21.addWidget(self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_DAT_GPTSoVITS_OutputRoot)

        self.Frame_DAT_VITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_DAT_VITS_OutputRoot.setObjectName(u"Frame_DAT_VITS_OutputRoot")
        self.Frame_DAT_VITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_DAT_VITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.Frame_DAT_VITS_OutputRoot)
        self.horizontalLayout_22.setSpacing(12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_OutputRoot = LabelBase(self.Frame_DAT_VITS_OutputRoot)
        self.Label_DAT_VITS_OutputRoot.setObjectName(u"Label_DAT_VITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_DAT_VITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_DAT_VITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_22.addWidget(self.Label_DAT_VITS_OutputRoot)

        self.LineEdit_DAT_VITS_OutputRoot = LineEditBase(self.Frame_DAT_VITS_OutputRoot)
        self.LineEdit_DAT_VITS_OutputRoot.setObjectName(u"LineEdit_DAT_VITS_OutputRoot")
        self.LineEdit_DAT_VITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_22.addWidget(self.LineEdit_DAT_VITS_OutputRoot)

        self.Button_DAT_VITS_OutputRoot_MoreActions = MenuButton(self.Frame_DAT_VITS_OutputRoot)
        self.Button_DAT_VITS_OutputRoot_MoreActions.setObjectName(u"Button_DAT_VITS_OutputRoot_MoreActions")
        self.Button_DAT_VITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_DAT_VITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_22.addWidget(self.Button_DAT_VITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_DAT_VITS_OutputRoot)

        self.Frame_Train_GPTSoVITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_Train_GPTSoVITS_OutputRoot.setObjectName(u"Frame_Train_GPTSoVITS_OutputRoot")
        self.Frame_Train_GPTSoVITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_Train_GPTSoVITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_23 = QHBoxLayout(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.horizontalLayout_23.setSpacing(12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_OutputRoot = LabelBase(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.Label_Train_GPTSoVITS_OutputRoot.setObjectName(u"Label_Train_GPTSoVITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_Train_GPTSoVITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_Train_GPTSoVITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_23.addWidget(self.Label_Train_GPTSoVITS_OutputRoot)

        self.LineEdit_Train_GPTSoVITS_OutputRoot = LineEditBase(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.LineEdit_Train_GPTSoVITS_OutputRoot.setObjectName(u"LineEdit_Train_GPTSoVITS_OutputRoot")
        self.LineEdit_Train_GPTSoVITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_23.addWidget(self.LineEdit_Train_GPTSoVITS_OutputRoot)

        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_OutputRoot_MoreActions")
        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_23.addWidget(self.Button_Train_GPTSoVITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_Train_GPTSoVITS_OutputRoot)

        self.Frame_Train_VITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_Train_VITS_OutputRoot.setObjectName(u"Frame_Train_VITS_OutputRoot")
        self.Frame_Train_VITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_Train_VITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_24 = QHBoxLayout(self.Frame_Train_VITS_OutputRoot)
        self.horizontalLayout_24.setSpacing(12)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_OutputRoot = LabelBase(self.Frame_Train_VITS_OutputRoot)
        self.Label_Train_VITS_OutputRoot.setObjectName(u"Label_Train_VITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_Train_VITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_Train_VITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_24.addWidget(self.Label_Train_VITS_OutputRoot)

        self.LineEdit_Train_VITS_OutputRoot = LineEditBase(self.Frame_Train_VITS_OutputRoot)
        self.LineEdit_Train_VITS_OutputRoot.setObjectName(u"LineEdit_Train_VITS_OutputRoot")
        self.LineEdit_Train_VITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_24.addWidget(self.LineEdit_Train_VITS_OutputRoot)

        self.Button_Train_VITS_OutputRoot_MoreActions = MenuButton(self.Frame_Train_VITS_OutputRoot)
        self.Button_Train_VITS_OutputRoot_MoreActions.setObjectName(u"Button_Train_VITS_OutputRoot_MoreActions")
        self.Button_Train_VITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_Train_VITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_24.addWidget(self.Button_Train_VITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_Train_VITS_OutputRoot)


        self.verticalLayout_34.addWidget(self.GroupBox_Settings_Tools_Path)

        self.VerticalSpacer_Settings_Tools = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.VerticalSpacer_Settings_Tools)

        self.ScrollArea_Settings_Tools.setWidget(self.ScrollAreaWidgetContents_Settings_Tools)

        self.gridLayout_93.addWidget(self.ScrollArea_Settings_Tools, 0, 0, 1, 1)

        self.StackedWidget_Pages_Settings.addWidget(self.SubPage_Settings_Tools)

        self.verticalLayout_78.addWidget(self.StackedWidget_Pages_Settings)

        self.StackedWidget_Pages.addWidget(self.Page_Settings)
        self.Page_Info = QWidget()
        self.Page_Info.setObjectName(u"Page_Info")
        self.verticalLayout_25 = QVBoxLayout(self.Page_Info)
        self.verticalLayout_25.setSpacing(21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(21, 12, 21, 12)
        self.Frame_Info_Top = QFrame(self.Page_Info)
        self.Frame_Info_Top.setObjectName(u"Frame_Info_Top")
        self.Frame_Info_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Info_Top.setStyleSheet(u"QFrame {\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.Frame_Info_Top)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Button_Info_Title = NavigationButton(self.Frame_Info_Top)
        self.Button_Info_Title.setObjectName(u"Button_Info_Title")
        sizePolicy1.setHeightForWidth(self.Button_Info_Title.sizePolicy().hasHeightForWidth())
        self.Button_Info_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_29.addWidget(self.Button_Info_Title)

        self.Frame_Info_Title_Spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.Frame_Info_Title_Spacer)


        self.verticalLayout_25.addWidget(self.Frame_Info_Top)

        self.Frame_Info_Middle = QFrame(self.Page_Info)
        self.Frame_Info_Middle.setObjectName(u"Frame_Info_Middle")
        self.Frame_Info_Middle.setStyleSheet(u"QFrame {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.Frame_Info_Middle)
        self.verticalLayout_22.setSpacing(21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 0, 12, 0)
        self.TextBrowser_Text_Info = TextBrowserBase(self.Frame_Info_Middle)
        self.TextBrowser_Text_Info.setObjectName(u"TextBrowser_Text_Info")
        self.TextBrowser_Text_Info.setStyleSheet(u"QTextBrowser {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"	border-radius: 6px;\n"
"}\n"
"QTextBrowser:hover {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;"
                        "\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	backg"
                        "round-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_22.addWidget(self.TextBrowser_Text_Info)


        self.verticalLayout_25.addWidget(self.Frame_Info_Middle)

        self.StackedWidget_Pages.addWidget(self.Page_Info)
        self.Splitter_Pages.addWidget(self.StackedWidget_Pages)
        self.Frame_Console = QFrame(self.Splitter_Pages)
        self.Frame_Console.setObjectName(u"Frame_Console")
        self.Frame_Console.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px 0px 0px 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: rgba(45, 45, 45, 135);\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.Frame_Console)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Frame_Console_Top = QFrame(self.Frame_Console)
        self.Frame_Console_Top.setObjectName(u"Frame_Console_Top")
        self.Frame_Console_Top.setMinimumSize(QSize(0, 24))
        self.Frame_Console_Top.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_14 = QHBoxLayout(self.Frame_Console_Top)
        self.horizontalLayout_14.setSpacing(21)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(21, 0, 21, 0)
        self.Button_Console_Title = ButtonBase(self.Frame_Console_Top)
        self.Button_Console_Title.setObjectName(u"Button_Console_Title")

        self.horizontalLayout_14.addWidget(self.Button_Console_Title)

        self.horizontalSpacer = QSpacerItem(826, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.Button_Console_Copy = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Copy.setObjectName(u"Button_Console_Copy")
        self.Button_Console_Copy.setMaximumSize(QSize(24, 24))
        self.Button_Console_Copy.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/images/icons/Clipboard.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_14.addWidget(self.Button_Console_Copy)

        self.Button_Console_Clear = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Clear.setObjectName(u"Button_Console_Clear")
        self.Button_Console_Clear.setMaximumSize(QSize(24, 24))
        self.Button_Console_Clear.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/images/icons/TrashCan.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_14.addWidget(self.Button_Console_Clear)

        self.Button_Console_Fold = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Fold.setObjectName(u"Button_Console_Fold")
        self.Button_Console_Fold.setMaximumSize(QSize(24, 24))
        self.Button_Console_Fold.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/images/icons/DownArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_14.addWidget(self.Button_Console_Fold)


        self.verticalLayout_23.addWidget(self.Frame_Console_Top)

        self.ScrollArea_Console = QScrollArea(self.Frame_Console)
        self.ScrollArea_Console.setObjectName(u"ScrollArea_Console")
        self.ScrollArea_Console.setStyleSheet(u"QScrollArea, QScrollArea QWidget {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(210, 210, 210, 123);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: rgba(210, 210, 210, 210);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 21"
                        "0);\n"
"}")
        self.ScrollArea_Console.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Console = QWidget()
        self.ScrollAreaWidgetContents_Console.setObjectName(u"ScrollAreaWidgetContents_Console")
        self.ScrollAreaWidgetContents_Console.setGeometry(QRect(0, 0, 1070, 175))
        self.verticalLayout_50 = QVBoxLayout(self.ScrollAreaWidgetContents_Console)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.PlainTextEdit_Console = TextEditBase(self.ScrollAreaWidgetContents_Console)
        self.PlainTextEdit_Console.setObjectName(u"PlainTextEdit_Console")

        self.verticalLayout_50.addWidget(self.PlainTextEdit_Console)

        self.ScrollArea_Console.setWidget(self.ScrollAreaWidgetContents_Console)

        self.verticalLayout_23.addWidget(self.ScrollArea_Console)

        self.Splitter_Pages.addWidget(self.Frame_Console)

        self.verticalLayout_5.addWidget(self.Splitter_Pages)


        self.horizontalLayout_2.addWidget(self.Frame_Pages)


        self.verticalLayout.addWidget(self.Content)

        self.StatusBar = QFrame(self.CentralWidget)
        self.StatusBar.setObjectName(u"StatusBar")
        self.StatusBar.setMinimumSize(QSize(0, 24))
        self.StatusBar.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_52 = QHBoxLayout(self.StatusBar)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.Frame_Bottom_Toggle_Console = QFrame(self.StatusBar)
        self.Frame_Bottom_Toggle_Console.setObjectName(u"Frame_Bottom_Toggle_Console")
        self.Frame_Bottom_Toggle_Console.setMinimumSize(QSize(48, 0))
        self.Frame_Bottom_Toggle_Console.setMaximumSize(QSize(48, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.Frame_Bottom_Toggle_Console)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Button_Toggle_Console = QPushButton(self.Frame_Bottom_Toggle_Console)
        self.Button_Toggle_Console.setObjectName(u"Button_Toggle_Console")
        sizePolicy.setHeightForWidth(self.Button_Toggle_Console.sizePolicy().hasHeightForWidth())
        self.Button_Toggle_Console.setSizePolicy(sizePolicy)
        self.Button_Toggle_Console.setStyleSheet(u"QPushButton {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	image: url(:/Button_Icon/images/icons/Console.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 1.5px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"QPushButton:checked {\n"
"	/*background-color: rgb(45, 45, 45);*/\n"
"}")

        self.verticalLayout_6.addWidget(self.Button_Toggle_Console)


        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Toggle_Console)

        self.Frame_Bottom_Left = QFrame(self.StatusBar)
        self.Frame_Bottom_Left.setObjectName(u"Frame_Bottom_Left")
        self.horizontalLayout = QHBoxLayout(self.Frame_Bottom_Left)
        self.horizontalLayout.setSpacing(21)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 0, 0, 0)
        self.Label_ToolsStatus = LabelBase(self.Frame_Bottom_Left)
        self.Label_ToolsStatus.setObjectName(u"Label_ToolsStatus")
        self.horizontalLayout_49 = QHBoxLayout(self.Label_ToolsStatus)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(60, 0, 0, 0)

        self.horizontalLayout.addWidget(self.Label_ToolsStatus)

        self.HorizontalSpacer_Bottom_Left = QSpacerItem(182, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.HorizontalSpacer_Bottom_Left)


        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Left)

        self.Frame_Bottom_Others = QFrame(self.StatusBar)
        self.Frame_Bottom_Others.setObjectName(u"Frame_Bottom_Others")
        self.Frame_Bottom_Others.setMinimumSize(QSize(666, 0))

        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Others)

        self.Frame_Bottom_Right = QFrame(self.StatusBar)
        self.Frame_Bottom_Right.setObjectName(u"Frame_Bottom_Right")
        self.horizontalLayout_50 = QHBoxLayout(self.Frame_Bottom_Right)
        self.horizontalLayout_50.setSpacing(21)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 30, 0)
        self.Label_Usage_CPU = LabelBase(self.Frame_Bottom_Right)
        self.Label_Usage_CPU.setObjectName(u"Label_Usage_CPU")
        self.Label_Usage_CPU.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_62 = QHBoxLayout(self.Label_Usage_CPU)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_50.addWidget(self.Label_Usage_CPU)

        self.Label_Usage_GPU = LabelBase(self.Frame_Bottom_Right)
        self.Label_Usage_GPU.setObjectName(u"Label_Usage_GPU")
        self.Label_Usage_GPU.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_64 = QHBoxLayout(self.Label_Usage_GPU)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_50.addWidget(self.Label_Usage_GPU)

        self.Label_Version = LabelBase(self.Frame_Bottom_Right)
        self.Label_Version.setObjectName(u"Label_Version")
        self.horizontalLayout_51 = QHBoxLayout(self.Label_Version)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_50.addWidget(self.Label_Version)


        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Right)


        self.verticalLayout.addWidget(self.StatusBar)

        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget_Pages.setCurrentIndex(0)
        self.StackedWidget_Pages_Env.setCurrentIndex(0)
        self.StackedWidget_Pages_Models.setCurrentIndex(0)
        self.StackedWidget_Pages_VPR.setCurrentIndex(0)
        self.StackedWidget_Pages_ASR.setCurrentIndex(0)
        self.StackedWidget_Pages_Dataset.setCurrentIndex(0)
        self.StackedWidget_DAT_GPTSoVITS.setCurrentIndex(0)
        self.StackedWidget_DAT_VITS.setCurrentIndex(0)
        self.StackedWidget_Pages_Train.setCurrentIndex(0)
        self.StackedWidget_Train_GPTSoVITS.setCurrentIndex(0)
        self.StackedWidget_Train_VITS.setCurrentIndex(0)
        self.StackedWidget_Pages_TTS.setCurrentIndex(0)
        self.StackedWidget_Pages_Settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
#if QT_CONFIG(tooltip)
        self.Button_Toggle_Menu.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u4ee5\u5c55\u5f00/\u6298\u53e0\u83dc\u5355", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Button_Menu_Home.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Env.setToolTip(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Env.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Models.setToolTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ba1\u7406", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Models.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Process.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u97f3\u9891\u5904\u7406", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Process.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_VPR.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u8bed\u97f3\u8bc6\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_VPR.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_ASR.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u8bed\u97f3\u8f6c\u6587\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_ASR.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5f55", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Dataset.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u6570\u636e\u96c6\u5236\u4f5c", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Dataset.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Train.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u6a21\u578b\u8bad\u7ec3", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Train.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_TTS.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u8bed\u97f3\u5408\u6210", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_TTS.setText(QCoreApplication.translate("MainWindow", u"\u5408\u6210", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Settings.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u7aef\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Info.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u672c\u8f6f\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Info.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.TextBrowser_Text_Home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:840;\">\u4ecb\u7ecd</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:420;\"><br />\u4e00\u4e2a\u57fa\u4e8eWhisper\u3001VITS\u7b49\u9879\u76ee\u5b9e\u73b0\u7684\u7b80\u6613\u8bed\u97f3\u5de5\u5177\u7bb1\uff0c\u63d0\u4f9b"
                        "\u4e86\u5305\u62ec\u8bed\u97f3\u6a21\u578b\u8bad\u7ec3\u5728\u5185\u7684\u591a\u79cd\u81ea\u52a8\u5316\u97f3\u9891\u5de5\u5177<br /><br />\u5de5\u5177\u7bb1\u76ee\u524d\u5305 \u542b\u4ee5\u4e0b\u529f\u80fd\uff1a<br />\u97f3\u9891\u5904\u7406<br />\u8bed\u97f3\u8bc6\u522b<br />\u8bed\u97f3\u8f6c\u5f55<br />\u6570\u636e\u96c6\u5236\u4f5c<br />\u6a21\u578b\u8bad\u7ec3<br />\u8bed\u97f3\u5408\u6210<br /><br />\u8fd9\u4e9b\u529f\u80fd\u5f7c\u6b64\u4e4b\u95f4\u76f8\u4e92\u72ec\u7acb\uff0c\u4f46\u53c8\u80fd\u65e0\u7f1d\u8854\u63a5\u5730\u5f62\u6210\u4e00\u5957\u5b8c\u6574\u7684\u5de5\u4f5c\u6d41<br />\u7528\u6237\u53ef\u4ee5\u6839\u636e\u81ea\u5df1\u7684\u9700\u6c42\u6709\u9009\u62e9\u6027\u5730\u4f7f\u7528\uff0c\u4ea6\u6216\u8005\u4f9d\u6b21\u901a\u8fc7\u8fd9\u4e9b\u5de5\u5177\u5c06\u672a\u7ecf\u5904\u7406\u7684\u8bed\u97f3\u6587\u4ef6\u9010\u6b65\u53d8\u4e3a\u7406\u60f3\u7684\u8bed\u97f3\u6a21\u578b<br /></span></p></body></html>", None))
        self.Label_Demo_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u89c6\u9891\u6f14\u793a</font>", None))
        self.Label_Server_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u4e91\u7aef\u7248\u672c</font>", None))
        self.Label_Repo_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u9879\u76ee\u4ed3\u5e93</font>", None))
        self.Label_Donate_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u8d5e\u52a9\u4f5c\u8005</font>", None))
        self.Button_Env_Install_Title.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u914d\u7f6e", None))
        self.Button_Env_Manage_Title.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u88c5\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.Button_Install_Aria2.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u6d4b\u5b89\u88c5", None))
#endif // QT_CONFIG(tooltip)
        self.Label_Env_Install_Aria2_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_Aria2.setText(QCoreApplication.translate("MainWindow", u"Aria2", None))
#if QT_CONFIG(tooltip)
        self.Button_Install_FFmpeg.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u6d4b\u5b89\u88c5", None))
#endif // QT_CONFIG(tooltip)
        self.Label_Env_Install_FFmpeg_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_FFmpeg.setText(QCoreApplication.translate("MainWindow", u"FFmpeg", None))
#if QT_CONFIG(tooltip)
        self.Button_Install_Python.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u6d4b\u5b89\u88c5", None))
#endif // QT_CONFIG(tooltip)
        self.Label_Env_Install_Python_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_Python.setText(QCoreApplication.translate("MainWindow", u"Python", None))
#if QT_CONFIG(tooltip)
        self.Button_Install_PyReqs.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u6d4b\u5b89\u88c5", None))
#endif // QT_CONFIG(tooltip)
        self.Label_Env_Install_PyReqs_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_PyReqs.setText(QCoreApplication.translate("MainWindow", u"Python Requirements", None))
#if QT_CONFIG(tooltip)
        self.Button_Install_Pytorch.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u6d4b\u5b89\u88c5", None))
#endif // QT_CONFIG(tooltip)
        self.Label_Env_Install_Pytorch_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_Pytorch.setText(QCoreApplication.translate("MainWindow", u"Pytorch", None))
        self.Label_Env_Manage_Pytorch_Version.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9Pytorch\u7248\u672c", None))
        self.Button_Env_Manage_Pytorch_Install.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u88c5", None))
        self.ToolBox_Env_Manage_Pytorch.setItemText(self.ToolBox_Env_Manage_Pytorch.indexOf(self.ToolBox_Env_Manage_Pytorch_Page1Content), "")
        self.Button_Models_Process_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Models_VPR_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Models_ASR_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Models_TTS_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.TabWidget_Models_Process.setTabText(self.TabWidget_Models_Process.indexOf(self.Tab_Models_Process_UVR), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_VPR.setTabText(self.TabWidget_Models_VPR.indexOf(self.Tab_Models_VPR_TDNN), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_ASR.setTabText(self.TabWidget_Models_ASR.indexOf(self.Tab_Models_ASR_Whisper), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_TTS.setTabText(self.TabWidget_Models_TTS.indexOf(self.Tab_Models_TTS_GPTSoVITS), QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.TabWidget_Models_TTS.setTabText(self.TabWidget_Models_TTS.indexOf(self.Tab_Models_TTS_VITS), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.Button_VoiceIdentifier_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem = self.TreeWidget_Catalogue_VPR_TDNN.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled = self.TreeWidget_Catalogue_VPR_TDNN.isSortingEnabled()
        self.TreeWidget_Catalogue_VPR_TDNN.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.TreeWidget_Catalogue_VPR_TDNN.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_VPR_TDNN.setSortingEnabled(__sortingEnabled)

        self.GroupBox_VPR_TDNN_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_VPR_TDNN_AudioDirInput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_StdAudioSpeaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_VPR_TDNN_VPRParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_VPR_TDNN_DecisionThreshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_ModelPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_ModelType.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_FeatureMethod.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_DurationOfAudio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings.setItemText(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings.indexOf(self.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_VPR_TDNN_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_VPR_TDNN_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_AudioSpeakersDataName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.setItemText(self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.indexOf(self.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings_Page1Content), "")
        self.Button_VoiceTranscriber_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem3 = self.TreeWidget_Catalogue_ASR_Whisper.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled1 = self.TreeWidget_Catalogue_ASR_Whisper.isSortingEnabled()
        self.TreeWidget_Catalogue_ASR_Whisper.setSortingEnabled(False)
        ___qtreewidgetitem4 = self.TreeWidget_Catalogue_ASR_Whisper.topLevelItem(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_ASR_Whisper.setSortingEnabled(__sortingEnabled1)

        self.GroupBox_ASR_Whisper_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_ASR_Whisper_AudioDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_ASR_Whisper_WhisperParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_ASR_Whisper_AddLanguageInfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_ASR_Whisper_AddLanguageInfo.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_ASR_Whisper_ModelPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_ASR_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.CheckBox_ASR_Whisper_ConditionOnPreviousText.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_ASR_Whisper_ConditionOnPreviousText.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_ASR_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings.setItemText(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings.indexOf(self.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_ASR_Whisper_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_ASR_Whisper_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DatasetCreator_Title_GPTSoVITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_DatasetCreator_Title_VITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem6 = self.TreeWidget_Catalogue_DAT_GPTSoVITS.headerItem()
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled2 = self.TreeWidget_Catalogue_DAT_GPTSoVITS.isSortingEnabled()
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setSortingEnabled(False)
        ___qtreewidgetitem7 = self.TreeWidget_Catalogue_DAT_GPTSoVITS.topLevelItem(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setSortingEnabled(__sortingEnabled2)

        self.GroupBox_DAT_GPTSoVITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_SRTDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_DAT_GPTSoVITS_DataFormat.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_GPTSoVITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_DAT_GPTSoVITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_FileListName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content), "")
        ___qtreewidgetitem9 = self.TreeWidget_Catalogue_DAT_VITS.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled3 = self.TreeWidget_Catalogue_DAT_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_DAT_VITS.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.TreeWidget_Catalogue_DAT_VITS.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_DAT_VITS.setSortingEnabled(__sortingEnabled3)

        self.GroupBox_DAT_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_DAT_VITS_AudioSpeakersDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SRTDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_DAT_VITS_DataFormat.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_AddAuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_DAT_VITS_AuxiliaryDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_TrainRatio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleWidth.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setItemText(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.indexOf(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_DAT_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_DAT_VITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_FileListNameTraining.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_FileListNameValidation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content), "")
        self.Button_VoiceTrainer_Title_GPTSoVITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_VoiceTrainer_Title_VITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem12 = self.TreeWidget_Catalogue_Train_GPTSoVITS.headerItem()
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled4 = self.TreeWidget_Catalogue_Train_GPTSoVITS.isSortingEnabled()
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setSortingEnabled(False)
        ___qtreewidgetitem13 = self.TreeWidget_Catalogue_Train_GPTSoVITS.topLevelItem(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setSortingEnabled(__sortingEnabled4)

        self.GroupBox_Train_GPTSoVITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_Train_GPTSoVITS_FileListPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_GPTSoVITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setItemText(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.indexOf(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_Train_GPTSoVITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Train_GPTSoVITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_LogDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content), "")
        ___qtreewidgetitem15 = self.TreeWidget_Catalogue_Train_VITS.headerItem()
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled5 = self.TreeWidget_Catalogue_Train_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_Train_VITS.setSortingEnabled(False)
        ___qtreewidgetitem16 = self.TreeWidget_Catalogue_Train_VITS.topLevelItem(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Train_VITS.setSortingEnabled(__sortingEnabled5)

        self.GroupBox_Train_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_Train_VITS_FileListPathTraining.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_FileListPathValidation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Train_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Train_VITS_Epochs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_BatchSize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_UsePretrainedModels.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_UsePretrainedModels.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Train_VITS_ModelPathPretrainedG.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_ModelPathPretrainedD.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_KeepOriginalSpeakers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Train_VITS_ConfigPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_NumWorkers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setItemText(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.indexOf(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_Train_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Train_VITS_EvalInterval.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_LogDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content), "")
        self.Button_VoiceConverter_Title_GPTSoVITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_VoiceConverter_Title_VITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem18 = self.TreeWidget_Catalogue_TTS_GPTSoVITS.headerItem()
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled6 = self.TreeWidget_Catalogue_TTS_GPTSoVITS.isSortingEnabled()
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setSortingEnabled(False)
        ___qtreewidgetitem19 = self.TreeWidget_Catalogue_TTS_GPTSoVITS.topLevelItem(0)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setSortingEnabled(__sortingEnabled6)

        self.GroupBox_TTS_GPTSoVITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_UseWebUI.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_TTS_GPTSoVITS_UseWebUI.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        ___qtreewidgetitem21 = self.TreeWidget_Catalogue_TTS_VITS.headerItem()
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled7 = self.TreeWidget_Catalogue_TTS_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_TTS_VITS.setSortingEnabled(False)
        ___qtreewidgetitem22 = self.TreeWidget_Catalogue_TTS_VITS.topLevelItem(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_TTS_VITS.setSortingEnabled(__sortingEnabled7)

        self.GroupBox_TTS_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_TTS_VITS_ConfigPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_ModelPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_TTS_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_TTS_VITS_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Speaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_EmotionStrength.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_PhonemeDuration.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_SpeechRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.setItemText(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.indexOf(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content), "")
        self.Button_Settings_Title_Client.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Settings_Title_Tools.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.GroupBox_Settings_Client_Outlook.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_Theme.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Setting_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Settings_Client_Function.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_Settings_Client_Operation.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.GroupBox_Settings_Tools_Function.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_AutoReset.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoReset.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_Settings_Tools_Path.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Process_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_Whisper_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Info_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Console_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_ToolsStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Usage_CPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Usage_GPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass
    # retranslateUi