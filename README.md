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

# 1)
Manually way with Windows: (supports 2FA)
download this repo: https://github.com/NyaMisty/actions-iTunes-header
install iTunes 12.6.5.3, from https://secure-appldnld.apple.com/itunes12/091-87819-20180912-69177170-B085-11E8-B6AB-C1D03409AD2A6/iTunes64Setup.exe

# 2)
patch the iTunes using
```
python3 actions-iTunes-header/workflow_helper/iTunesInstall/patch_itunes.py
```
to make it work, python should be run as administrator as itunes.exe will be modified.

# 3)
open iTunes, sign out & re-login your account

# 4)
authorize itunes on the computer
buy something on app store, to remember password (maybe not needed)

# 5)
install frida:
```
pip3 install frida
python3 actions-iTunes-header/workflow_helper/iTunesDownload/get_header.py
```
check ip address of local server (127.0.0.1), and ip of local machine (avoid using vpn)

7)
open web page on browser on apple store, id is on the link address. for example Chrome apple store is:
```
https://apps.apple.com/it/app/google-chrome/id535886823
```
and id is 535886823

9)
I have not found a way to know the version and ios compatibility in advance, so I download everything
```
python3 main.py download -s http://127.0.0.1:9000 --appId 535886823 --downloadAllVersion
```

Output example
```
  E:\Winpython\ipatool-py-master>python main.py download -s http://127.0.0.1:9000 --appId 535886823 --downloadAllVersion
  [19:05:28] INFO     Retrieving history version for appId 535886823                                          main.py:357
             INFO     Using iTunes interface http://127.0.0.1:9000 to download app!                           main.py:241
             INFO     Retrieving download info for appId 535886823                                            main.py:362
  [19:05:30] INFO     Got available version ids [8682551, 10009450, 10288631, 10685471, 12047844, 12846865,   main.py:379
                      13058434, 14159802, 14550546, 14937994, 15149813, 15368203, 15757367, 15933992,
                      16447860, 27612639, 63212670, 105682665, 266852636, 363732632, 384252639, 437392635,
                      863458320, 863762150, 863770065, 863868659, 864035341, 864424982]
             INFO     Downloading appId 535886823 appVerId 8682551                                            main.py:450
             INFO     Retrieving download info for appId 535886823 with versionId 8682551                     main.py:458
  [19:05:31] INFO     Downloading app Chrome (com.google.chrome.ios) with appId 535886823 (version            main.py:476
                      19.0.1084.60, versionId 8682551)
             INFO     Downloading ipa to .\com.google.chrome.ios-19.0.1084.60-535886823-8682551.ipa           main.py:487
  [19:05:32] INFO     Download progress: 7.83% (  1.0M / 12.8M)                                                main.py:81
             INFO     Download progress: 15.67% (  2.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 23.50% (  3.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 31.33% (  4.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 39.16% (  5.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 47.00% (  6.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 54.83% (  7.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 62.66% (  8.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 70.49% (  9.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 78.33% ( 10.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 86.16% ( 11.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 93.99% ( 12.0M / 12.8M)                                               main.py:81
             INFO     Download progress: 100.00% ( 12.8M / 12.8M)                                              main.py:81
             INFO     Download success in retry 0                                                              main.py:59
             INFO     Writing out iTunesMetadata.plist...                                                     main.py:493
             INFO     Manifest.plist does not exist! Assuming it is an old app without one...                 main.py:528
             INFO     Downloaded ipa to com.google.chrome.ios-19.0.1084.60-535886823-8682551.ipa              main.py:537
          
```

8) use script provided to parse all .ipa files, and select the suitable ones
```
e:/Winpython/WPy64-31040/python-3.10.4.amd64/python.exe e:/Winpython/ipatool-py-master/parse_ipa.py
+-------------------------------------------------------------------------------------------+-------------+----------------+
| File                                                                                      | Version     |   IOS required |
|-------------------------------------------------------------------------------------------+-------------+----------------|
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-19.0.1084.60-535886823-8682551.ipa   | 19.1084.60  |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-21.0.1180.77-535886823-10009450.ipa  | 21.1180.77  |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-21.0.1180.80-535886823-10288631.ipa  | 21.1180.80  |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-21.0.1180.82-535886823-10685471.ipa  | 21.1180.82  |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-23.0.1271.100-535886823-13058434.ipa | 23.1271.100 |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-23.0.1271.91-535886823-12047844.ipa  | 23.1271.91  |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-23.0.1271.96-535886823-12846865.ipa  | 23.1271.96  |            4.3 |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-25.0.1364.124-535886823-14550546.ipa | 25.1364.124 |            5   |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-25.0.1364.86-535886823-14159802.ipa  | 25.1364.86  |            5   |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-26.0.1410.50-535886823-14937994.ipa  | 26.1410.50  |            5   |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-27.0.1453.10-535886823-15368203.ipa  | 27.1453.10  |            5   |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-28.0.1500.12-535886823-15757367.ipa  | 28.1500.12  |            5   |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-28.0.1500.16-535886823-15933992.ipa  | 28.1500.16  |            5   |
| E:/Winpython/ipatool-py-master/com.google.chrome.ios-29.0.1547.11-535886823-16447860.ipa  | 29.1547.11  |            5   |
+-------------------------------------------------------------------------------------------+-------------+----------------+
```

