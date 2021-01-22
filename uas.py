<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>827</width>
    <height>632</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>UAS WEB MINNING 17062</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="lineEdit">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>30</y>
      <width>541</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>URL =</string>
    </property>
   </widget>
   <widget class="QPushButton" name="crawl">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>30</y>
      <width>75</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Crawl</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Text =</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>340</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Text Summarization =</string>
    </property>
   </widget>
   <widget class="QPushButton" name="summ">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>730</x>
      <y>30</y>
      <width>75</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ringkaskan</string>
    </property>
   </widget>
   <widget class="QPushButton" name="openfile">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>30</y>
      <width>75</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Open File</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>90</y>
      <width>801</width>
      <height>251</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_2">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>360</y>
      <width>801</width>
      <height>231</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>827</width>
     <height>21</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuHelp">
    <property name="title">
     <string>Help</string>
    </property>
    <addaction name="about"/>
    <addaction name="actionAbout_2"/>
   </widget>
   <widget class="QMenu" name="menuText_sum">
    <property name="title">
     <string>Text sum</string>
    </property>
    <addaction name="file"/>
    <addaction name="webb"/>
    <addaction name="actionMengetik"/>
   </widget>
   <addaction name="menuText_sum"/>
   <addaction name="menuHelp"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="file">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="text">
    <string>From File</string>
   </property>
  </action>
  <action name="webb">
   <property name="text">
    <string>From Website</string>
   </property>
  </action>
  <action name="about">
   <property name="text">
    <string>Help</string>
   </property>
  </action>
  <action name="actionAbout_2">
   <property name="text">
    <string>About</string>
   </property>
  </action>
  <action name="actionMengetik">
   <property name="text">
    <string>Mengetik</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
