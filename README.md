to download older apps, that are delisted from apple store:
1) install itunes 12.6.5.3
2) patch itunes
3) login itunes to apple store
4) authorize itunes
5) start local app store web service
6) find app to download from app store web page
7) download all .ipa of the app
8) use script to filter the .ipa that meet ios requirement


following the instruction from https://github.com/NyaMisty/ipatool-py

1)
Manually way with Windows: (supports 2FA)
download this repo: https://github.com/NyaMisty/actions-iTunes-header
install iTunes 12.6.5.3, from https://secure-appldnld.apple.com/itunes12/091-87819-20180912-69177170-B085-11E8-B6AB-C1D03409AD2A6/iTunes64Setup.exe
2)
patch the iTunes using actions-iTunes-header/workflow_helper/iTunesInstall/patch_itunes.py

3)
open iTunes, sign out & re-login your account

4)
authorize itunes on the computer
buy something on app store, to remember password (maybe not needed)

5)
install frida: pip3 install frida
run: actions-iTunes-header/workflow_helper/iTunesDownload/get_header.py
check ip address of local server (127.0.0.1), and ip of local machine (avoid using vpn)

6)
open web page on browser on apple store, id is on the link address

7)
I have not found a way to know the version and ios compatibility in advance, so I download everything
python main.py download -s http://127.0.0.1:9000 --appId 1064769019 --downloadAllVersion

8) use script provided to parse all .ipa files, and select the suitable ones



