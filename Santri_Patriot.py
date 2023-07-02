#WEB library

from fileinput import close
import pickle
from pathlib import Path
from tkinter import Button
import streamlit_authenticator as stauth

from unittest import result
# from db_fxns import bacadata, create_table,add_data
from ctypes.wintypes import SIZE
from turtle import width
import tkinter as TK
from MySQLdb import Date
import streamlit.components.v1 as components
import streamlit.components.v1 as stc
# import plotly.express as px 
from secrets import choice
import streamlit as st
import camZ
from PIL import Image
from pandas import read_table, read_sql_table, read_csv
#opencv library
# import face_recognition
from datetime import date, datetime
from PIL import Image
import pandas as pd
import numpy as np
import cv2
import os
import time
import io
import csv
# st.image('jempol.jpg')


# autentikasi pengguna
names = ["Pembina","Neng Iin", "Koordinator"]
usernames = ["pembina","tutor spat", "koordinator spat"]
# loadhashedpassword
file_path=Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
    # hashed_passwords = pickle.load(file)

hashed_passwords = stauth.Hasher(['123', '456']).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
    "santripatriot_dashboard", "abcdef")

name, authentication_status,username = authenticator.login("Login","main")
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    buffer = io.BytesIO()


    # st.beta_set_page_config(page_title='Santri Patriot', page_icon='jempol')

    FRAME_WINDOW = st.image([]) #frame window

    hhide_st_style = """ 
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hhide_st_style, unsafe_allow_html=True) #hide streamlit menu
    # st.beta_set_page_config(page_title='Santri Patriot', page_icon='jempol.jpg')

    # st.sidebar.image("pol.png")
    st.sidebar.title(f"Welcome {name}")
    menu = ["HOME","ABSEN", "REGISTER", "DATA","MENU IJIN","GALERI KEGIATAN", "ABOUT"] #menu
    choice = st.sidebar.selectbox("Menu", menu) #sidebar menu

    # path = 'absensi' #path to save image
    images = [] #list of image
    classNames = [] #list of class
    # myList = os.listdir(path) #list of image



    col1, col2, col3 = st.columns(3) #columns
    cap = cv2.VideoCapture(0) #capture video
    if choice == 'ABSEN':
        # st.button(
        # label='Absensi Apel',
        # )
        # st.button(label='Absensi Magang', key=str, on_click='apel.html')
        # st.button(label='Absensi Soft Skill', key=str, on_click='apel.html')
    
        absen = ["Absensi Apel","Absensi Magang", "Absensi Soft Skill"] #menu
        choice = st.sidebar.selectbox("Menu Absensi", absen) #sidebar menu
        path = 'absensi' #path to save image
        images = [] #list of image
        classNames = [] #list of class
        myList = os.listdir(path) #list of image

    


        col1, col2, col3 = st.columns(3) #columns
        cap = cv2.VideoCapture(0) #capture video
        if choice =='Absensi Apel':
            with col1: #column 1
                st.subheader("ABSENSI APEL")
                run = st.checkbox("Run camera") #checkbox
            if run == True:
                for cl in myList: #loop
                    curlImg = cv2.imread(f'{path}/{cl}') #read image
                    images.append(curlImg)
                    classNames.append(os.path.splitext(cl)[0]) #split image name
                print(classNames)
                def findEncodings(images): #find encoding
                    encodeList = []
                    for img in images:
                        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                        # encode = face_recognition.face_encodings(img)[0]
                        # encodeList.append(encode)
                    return encodeList
                def faceList(name):
                    with open('absensi_apel.csv', 'r+') as f:
                        myDataList = f.readlines()
                        nameList = []
                        for line in myDataList:
                            entry = line.split(',')
                            nameList.append(entry[0])
                        if name not in nameList:
                            now = datetime.now()
                            dtString = now.strftime('%H:%M:%S')
                            # skrang = datetime.now() 
                            dtint = now.strftime('%d/%m/%y')  
                            f.writelines(f'\n{name},{dtint},{dtString}')
                encodeListUnkown = findEncodings(images)
                print('encoding complate!')
                
                while True:
                    success, img = cap.read()
                    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
                    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
                    faceCurFrame = []
                    encodeCurFrame = []
                    for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
                        matches = []
                        faceDis = []
                        #print(faceDis)
                        matchesIndex = np.argmin(faceDis)
                        y1,x2,y2,x1 = faceLoc
                        y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                        if matches[matchesIndex]:
                            name = classNames[matchesIndex].upper()
                            print(name)
                            camZ.updateBLOB("Cicik SR", "apel.jpg", "absensi_apel.csv")
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            faceList(name)
                            time.sleep(3)
                        else:
                            y1,x2,y2,x1 = faceLoc
                            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                            cv2.putText(img,"Unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    FRAME_WINDOW.image(img)
                    cv2.waitKey(1)
            # else:
            #     pass

        elif choice == 'Absensi Magang':
            # st.markdown("<h2 style='text-align: center; color: black;'>ATTEDANCE</h2>", unsafe_allow_html=True) #title
            with col1: #column 1
                st.subheader("ABSENSI MAGANG")
                run = st.checkbox("Run camera") #checkbox
            if run == True:
                for cl in myList: #loop
                    curlImg = cv2.imread(f'{path}/{cl}') #read image
                    images.append(curlImg)
                    classNames.append(os.path.splitext(cl)[0]) #split image name
                print(classNames)

                def findEncodings(images): #find encoding
                    encodeList = []
                    # for img in images:
                    #     img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                    #     encode = face_recognition.face_encodings(img)[0]
                    #     encodeList.append(encode)
                    return encodeList

                def faceList(name):
                    with open('absensi_magang.csv', 'r+') as f:
                        myDataList = f.readlines()
                        nameList = []
                        for line in myDataList:
                            entry = line.split(',')
                            nameList.append(entry[0])
                        if name not in nameList:
                            now = datetime.now()
                            # skrang = date.now()
                            dtString = now.strftime('%H:%M:%S') 
                            dtint = now.strftime('%d/%m/%y')  
                            f.writelines(f'\n{name},{dtint},{dtString}')
                            

                encodeListUnkown = findEncodings(images)
                print('encoding complate!')
                while True:
                    success, img = cap.read()
                    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
                    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
                    faceCurFrame = []
                    encodeCurFrame = []

                    for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
                        matches = []
                        faceDis = []
                        #print(faceDis)
                        matchesIndex = np.argmin(faceDis)
                        
                        y1,x2,y2,x1 = faceLoc
                        y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

                        if matches[matchesIndex]:
                            name = classNames[matchesIndex].upper()
                            print(name)
                            camZ.updateBLOB("Cicik SR", "apel.jpg", "absensi_magang.csv")
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            faceList(name)

                            time.sleep(3)
                        
                        else:
                            y1,x2,y2,x1 = faceLoc
                            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                            cv2.putText(img,"Unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    FRAME_WINDOW.image(img)
                    cv2.waitKey(1)

        elif choice =='Absensi Soft Skill':    
            with col1: #column 1
                st.subheader("ABSENSI SOFTSKILL")
                run = st.checkbox("Run camera") #checkbox
            if run == True:
                for cl in myList: #loop
                    curlImg = cv2.imread(f'{path}/{cl}') #read image
                    images.append(curlImg)
                    classNames.append(os.path.splitext(cl)[0]) #split image name
                print(classNames)

                def findEncodings(images): #find encoding
                    encodeList = []
                    # for img in images:
                    #     img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                    #     encode = face_recognition.face_encodings(img)[0]
                    #     encodeList.append(encode)
                    return encodeList

                def faceList(name):
                    with open('absensi_softskill.csv', 'r+') as f:
                        myDataList = f.readlines()
                        nameList = []
                        for line in myDataList:
                            entry = line.split(',')
                            nameList.append(entry[0])
                        if name not in nameList:
                            now = datetime.now()
                            # skrang = date.now()
                            dtString = now.strftime('%H:%M:%S') 
                            dtint = now.strftime('%d/%m/%y')  
                            f.writelines(f'\n{name},{dtint},{dtString}')
                            

                encodeListUnkown = findEncodings(images)
                print('encoding complate!')
                while True:
                    success, img = cap.read()
                    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
                    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
                    faceCurFrame = []
                    encodeCurFrame = []

                    for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
                        matches = []
                        faceDis = []
                        #print(faceDis)
                        matchesIndex = np.argmin(faceDis)
                        
                        y1,x2,y2,x1 = faceLoc
                        y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

                        if matches[matchesIndex]:
                            name = classNames[matchesIndex].upper()
                            print(name)
                            camZ.updateBLOB("Cicik SR", "apel.jpg", "absensi_softskill.csv")
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            faceList(name)

                            time.sleep(3)
                        
                        else:
                            y1,x2,y2,x1 = faceLoc
                            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                            cv2.putText(img,"Unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    FRAME_WINDOW.image(img)
                    cv2.waitKey(1)

    #register menu
    elif choice == 'REGISTER':
        if st.button("get data"):
            print('bajingan')
            print(type(camZ.getData.di))
            print(camZ.getData.di)
            p1 = camZ.getData.di
            for x in range(1, len(p1)+1):
                camZ.readBLOB(x)
            with col1:
                st.subheader("REGISTER")
                st.write("<h2 style='text-align: center; color: black;'>REGISTER</h2>", unsafe_allow_html=True)
        with col2:
            st.subheader("REGISTER")
        def load_image(image_file):
            img = Image.open(image_file)
            # camZ.insertBLOB(5, "user", "chloe.jpg", "user.txt")
            return img

        image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
        if image_file is not None:
            file_details = {"FileName":image_file.name,"FileType":image_file.type}
            st.write(file_details)
            img = load_image(image_file)
            with open(os.path.join("absensi",image_file.name),"wb") as f: 
                f.write(image_file.getbuffer())  
                print(image_file.name)
                imgFile = "D:\ABSENSIPATRIOT\\absensi\{}".format(image_file.name) #sesuaikan path folder punya kalian
                camZ.insertBLOB(image_file.name, imgFile, "absensi_apel.csv")
            st.success("Saved File")

    #read data menu
    elif choice == 'DATA':
        data = ["Data Absensi Apel","Data Absensi Magang", "Data Absensi Soft Skill"] #menu
        choice = st.sidebar.selectbox("Data Absensi", data) #sidebar menu
        if choice =='Data Absensi Apel':
            df = pd.read_csv('absensi_apel.csv')
            st.subheader("HASIL ABSENSI APEL")
            df = pd.read_csv('absensi_apel.csv')
            st.table(df)
            #st.button(download='absensi.csv', "Download Excel")
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Absensi Apel')
                writer.save()
                st.download_button(
                label="Download Excel",
                data=buffer,
                file_name="Absensi Apel.xlsx",
                mime="application/vnd.ms-excel"
            )
        elif choice == 'Data Absensi Magang':
            df = pd.read_csv('absensi_magang.csv')
            st.subheader("HASIL ABSENSI MAGANG")
            df = pd.read_csv('absensi_magang.csv')
            st.table(df)
            #st.button(download='absensi.csv', "Download Excel")
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Absensi Magang')
                writer.save()
                st.download_button(
                label="Download Excel",
                data=buffer,
                file_name="Absensi Magang.xlsx",
                mime="application/vnd.ms-excel"
            )
        elif choice == 'Data Absensi Soft Skill':
            df = pd.read_csv('absensi_softskill.csv')
            st.subheader("HASIL ABSENSI PELATIHAN SOFT SKILL")
            df = pd.read_csv('absensi_softskill.csv')
            st.table(df)
            #st.button(download='absensi.csv', "Download Excel")
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Absensi Soft Skill')
                writer.save()
                st.download_button(
                label="Download Excel",
                data=buffer,
                file_name="Absensi Soft Skill.xlsx",
                mime="application/vnd.ms-excel"
            )

    elif choice == 'HOME':
        with col1:
            st.image("apel.jpg",width=990, caption="Apel Rutin") 


    elif choice == "ABOUT":
        st.markdown("<h1 style='text-align: center; color: black;'>ABOUT</h1>", unsafe_allow_html=True) #title
        st.write("SANTRI PATRIOT ( S.Pat ) adalah Program untuk mencetak KADER :")
        st.write("SANTRI ( Istiqomah melaksanakan ajaran Islam )")
        st.write("PATRIOT ( Cinta tanah air  , siap berbuat untuk kebaikan bangsa  , sebagai pelaksanaan dari Panca Kesadaran --> Kesadaran Berbangsa & bernegara <-- )")
        st.write("Hak S.Pat : Bebas Biaya Kuliah")
        st.write("Kewajiban S.Pat : Membantu PPNJ  & UNUJA sesuai Perintah Pimpinan")
        st.write("Setiap Santri Patriot harus punya tugas sebagai Pengurus atau pembantu Pengurus Setiap Santri Patriot diharapkan mempunyai Skill  :  * Memasak * Laundry * Office  ( Word  , Excell  , Powerpoint )")
            
    elif choice == 'GALERI KEGIATAN':
        st.markdown("<h1 style='text-align: center;'>Galeri Kegiatan Santri Patriot</h1>", unsafe_allow_html=True) #title
        st.image("galeri/apel.jpg", caption="Apel Rutin Setiap Kamis")
        st.image("galeri/apell.jpg", caption="Apel Rutin Setiap Kamis")
        st.image("galeri/dadargulung.jpg", caption="Dadar Gulung Hasil Pelatihan Soft Skill Level Advance")
        st.image("galeri/jeli.jpg", caption="Jely Mata Sapi Hasil Pelatihan Soft Skill Level Advance")
        st.image("galeri/kajian.jpg", caption="Kajian Furudlul Ainiyah")
        st.image("galeri/office.jpg", caption="Tes Office Santri Patriot Angkatan 20")
        st.image("galeri/onde.jpg", caption="Onde-onde Hasil Pelatihan Soft Skill Level Advance")
        st.image("galeri/persiapan.jpg", caption="Persiapan Tes Office Santri Patriot Angkatan 21")
        st.image("galeri/rapat.jpg", caption="Rapat Koordinasi Santri Patriot Wilayah Az-Zainiyah")
        st.image("galeri/rapatall.jpg", caption="Rapat Koordinasi Seluruh Angkatan Santri Patriot")
        st.image("galeri/rapatsatelit.jpg", caption="Rapat Koordinasi Santri Patriot Wilayah Satelit")
        st.image("galeri/tes.jpg", caption="Tes Materi Memasak Dasar")


    elif choice == "MENU IJIN":
        def main():
            st.title("Tambah Data Ijin")
            ijin = ["BUAT IJIN"] #menu
            choice = st.sidebar.selectbox("Menu Ijin", ijin) #sidebar menu
            if choice == "BUAT IJIN":
                with open('data_ijin.csv', 'r+') as f:
                    name = st.text_input("Masukkan Nama")
                    kegiatan = st.selectbox("Kegiatan",["Apel","Pelatihan Soft Skill", "Magang"])
                    status =st.selectbox("Status",["Alfa","Ijin","Sakit"])
                    tanggal= st.date_input("Masukkan Tanggal")
                    button=st.button("Buat Ijin")
                    if button:
                        f.writelines(f'\n{name},{kegiatan},{status},{tanggal}')
                        myDataList = f.readlines()
                        nameList = []
                        for line in myDataList:
                            entry = line.split(',')
                            nameList.append(entry[0])
                        df = pd.read_csv('data_ijin.csv')
                        st.table(df)
                        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                            df.to_excel(writer, sheet_name='Data Perijinan')
                            writer.save()
                            st.download_button(
                            label="Download Excel",
                            data=buffer,
                            file_name="Data Perijinan.xlsx",
                            mime="application/vnd.ms-excel"
                        )   
                close()
                        
                          
                # if button:
                #   st.write(f'Nama : {nama}')
                    # st.write(f'Kegiatan : {kegiatan}')
                    # st.write(f'Status : {status}')
                    # st.write(f'Tanggal : {tanggal}')
                      


            # elif choice == "Data Ijin":
                
            #     df = pd.read_csv('data_ijin.csv')
            #     st.table(df)
                        

            #         # st.table(f)
            #     f.writelines(f'\n{name},{kegiatan},{status},{tanggal}')
            #     st.table(df)
            #     with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                            
            #         df.to_excel(writer, sheet_name='Data Perijinan')
            #         writer.save()
            #         st.download_button(
            #         label="Download Excel",
            #         data=buffer,
            #         file_name="Data Perijinan.xlsx",
            #         mime="application/vnd.ms-excel"
            #     ) 
            # elif choice == "Data Ijin":
            #     st.subheader("Data Ijin")
            # elif choice == "Data Ijin":
            #     st.subheader("Data Ijin")

            # else:
            #     st.subheader("Tentang Perijinan")


if __name__=='__main__':
    # main()     
    authenticator.logout("Logout","sidebar")
    
        