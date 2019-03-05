# Lab 2 answers

## Names: Sara Díaz - Gabriela Martinez

## Task 2.1: Getting Started with NLTK

### Q211 (WordCountTensorFlow_1.py): 

C:\Users\gabim\AppData\Local\Programs\Python\Python37-32\python.exe C:/Users/gabim/PycharmProjects/Lab2_CC/WordCountTensorFlow_1.py<br/>
[nltk_data] Downloading package punkt to<br/>
[nltk_data]     C:\Users\gabim\AppData\Roaming\nltk_data...<br/>
[nltk_data]   Package punkt is already up-to-date!<br/>
[('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 470), (':', 454), ('in', 417)]<br/>
3383<br/>
<br/>
Process finished with exit code 0<br/>

### Q212 (WordCountTensorFlow_2.py): 

C:\Users\gabim\AppData\Local\Programs\Python\Python37-32\python.exe C:/Users/gabim/PycharmProjects/Lab2_CC/WordCountTensorFlow_2.py<br/>
[nltk_data] Downloading package punkt to<br/>
[nltk_data]     C:\Users\gabim\AppData\Roaming\nltk_data...<br/>
[nltk_data]   Package punkt is already up-to-date!<br/>
[('the', 1444), ('of', 586), ('to', 531), ('in', 506), ('a', 481), ('and', 346), ('is', 289), ('we', 279), ('that', 275), ('this', 268)]<br/>
3117<br/>
<br/>
Process finished with exit code 0<br/>

### Q213a (stopwords): 

#### Why "Tensorflow" is not the most frequent word? <br/>
Because before removing the stopwords, many of these prepositions were written more many times than "TensorFlow"<br/>
<br/>
#### Which are the Stop Words? <br/>
the, of, to, in, a, and, is, we, that, this...<br/>
<br/>
### Q213b (WordCountTensorFlow_3.py): 
C:\Users\gabim\AppData\Local\Programs\Python\Python37-32\python.exe C:/Users/gabim/PycharmProjects/Lab2_CC/WordCountTensorFlow_3.py<br/>
[nltk_data] Downloading package punkt to<br/>
[nltk_data]     C:\Users\gabim\AppData\Roaming\nltk_data...<br/>
[nltk_data]   Package punkt is already up-to-date!<br/>
[nltk_data] Downloading package stopwords to<br/>
[nltk_data]     C:\Users\gabim\AppData\Roaming\nltk_data...<br/>
[nltk_data]   Package stopwords is already up-to-date!<br/>
[('tensorflow', 193), ('data', 102), ('tensor', 99), ('code', 90), ('learning', 81), ('function', 74), ('one', 73), ('use', 65), ('example', 64), ('available', 63)]<br/>
2998<br/>
<br/>
Process finished with exit code 0<br/>

## Task 2.2: Getting Started with tweepy

### Q221 (Twitter_1.py): It is me!!

C:\Users\gabim\AppData\Local\Programs\Python\Python37-32\python.exe C:/Users/gabim/PycharmProjects/Lab2_CC/Twitter_1.py<br/>
Name: Gabriela Martinez<br/>
Location: Medellín, Colombia<br/>
Friends: 12<br/>
Created: 2018-01-13 13:59:37<br/>
Description: <br/>
<br/>
Process finished with exit code 0<br/>

### Q22 (Twitter_2.py): formatting tweets into json and finding friends

#LasMásLeídas | El asesinato cometido para ocultar peligroso descubrimiento matemático ⬇ (Vía @bbcmundo) https://t.co/ajLmfaiIT9<br/>
{<br/>
  "created_at": "Tue Mar 05 08:00:13 +0000 2019",<br/>
  "id": 1102841228457111553,<br/>
  "id_str": "1102841228457111553",<br/>
  "text": "#LasM\u00e1sLe\u00eddas | El asesinato cometido para ocultar peligroso descubrimiento matem\u00e1tico \u2b07 (V\u00eda @bbcmundo) https://t.co/ajLmfaiIT9",<br/>
  "truncated": false,<br/>
  "entities": {<br/>
    "hashtags": [<br/>
      {<br/>
        "text": "LasM\u00e1sLe\u00eddas",<br/>
        "indices": [<br/>
          0,<br/>
          13<br/>
        ]<br/>
      }<br/>
    ],<br/>
    "symbols": [],<br/>
    "user_mentions": [<br/>
      {<br/>
        "screen_name": "bbcmundo",<br/>
        "name": "BBC News Mundo",<br/>
        "id": 10012122,<br/>
        "id_str": "10012122",<br/>
        "indices": [<br/>
          94,<br/>
          103<br/>
        ]<br/>
      }<br/>
    ],<br/>
    "urls": [<br/>
      {<br/>
        "url": "https://t.co/ajLmfaiIT9",<br/>
        "expanded_url": "http://ow.ly/j3cq30nVdU5",<br/>
        "display_url": "ow.ly/j3cq30nVdU5",<br/>
        "indices": [<br/>
          105,<br/>
          128<br/>
        ]<br/>
      }<br/>
    ]<br/>
  },<br/>
  "source": "<a href=\"https://www.hootsuite.com\" rel=\"nofollow\">Hootsuite Inc.</a>",<br/>
  "in_reply_to_status_id": null,<br/>
  "in_reply_to_status_id_str": null,<br/>
  "in_reply_to_user_id": null,<br/>
  "in_reply_to_user_id_str": null,<br/>
  "in_reply_to_screen_name": null,<br/>
  "user": {<br/>
    "id": 9633802,<br/>
    "id_str": "9633802",<br/>
    "name": "EL TIEMPO",<br/>
    "screen_name": "ELTIEMPO",<br/>
    "location": "Bogot\u00e1, Colombia",<br/>
    "description": "Principales noticias de Colombia, el mundo, deportes, econom\u00eda, pol\u00edtica, tecnolog\u00eda, cultura, estilo de vida, tendencias y mucho m\u00e1s. El Tiempo Casa Editorial.",<br/>
    "url": "http://t.co/pXsWZAle5x",<br/>
    "entities": {<br/>
      "url": {<br/>
        "urls": [<br/>
          {<br/>
            "url": "http://t.co/pXsWZAle5x",<br/>
            "expanded_url": "http://www.eltiempo.com",<br/>
            "display_url": "eltiempo.com",<br/>
            "indices": [<br/>
              0,<br/>
              22<br/>
            ]<br/>
          }<br/>
        ]<br/>
      },<br/>
      "description": {<br/>
        "urls": []<br/>
      }<br/>
    },<br/>
    "protected": false,<br/>
    "followers_count": 6563843,<br/>
    "friends_count": 26159,<br/>
    "listed_count": 15584,<br/>
    "created_at": "Tue Oct 23 20:03:24 +0000 2007",<br/>
    "favourites_count": 6519,<br/>
    "utc_offset": null,<br/>
    "time_zone": null,<br/>
    "geo_enabled": true,<br/>
    "verified": true,<br/>
    "statuses_count": 482612,<br/>
    "lang": "es",<br/>
    "contributors_enabled": false,<br/>
    "is_translator": false,<br/>
    "is_translation_enabled": true,<br/>
    "profile_background_color": "06609C",<br/>
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",<br/>
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",<br/>
    "profile_background_tile": true,<br/>
    "profile_image_url": "http://pbs.twimg.com/profile_images/1053511496972541953/Po6LEiC5_normal.jpg",<br/>
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1053511496972541953/Po6LEiC5_normal.jpg",<br/>
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/9633802/1551042126",<br/>
    "profile_link_color": "EB0C2A",<br/>
    "profile_sidebar_border_color": "000000",<br/>
    "profile_sidebar_fill_color": "FFFFFF",<br/>
    "profile_text_color": "000000",<br/>
    "profile_use_background_image": true,<br/>
    "has_extended_profile": true,<br/>
    "default_profile": false,<br/>
    "default_profile_image": false,<br/>
    "following": true,<br/>
    "follow_request_sent": false,<br/>
    "notifications": false,<br/>
    "translator_type": "regular"<br/>
  },<br/>
  "geo": null,<br/>
  "coordinates": null,<br/>
  "place": null,<br/>
  "contributors": null,<br/>
  "is_quote_status": false,<br/>
  "retweet_count": 0,<br/>
  "favorite_count": 0,<br/>
  "favorited": false,<br/>
  "retweeted": false,<br/>
  "possibly_sensitive": false,<br/>
  "possibly_sensitive_appealable": false,<br/>
  "lang": "es"<br/>
}<br/>
{<br/>
  "id": 1115440213,<br/>
  "id_str": "1115440213",<br/>
  "name": "Centro Democr\u00e1tico",<br/>
  "screen_name": "CeDemocratico",<br/>
  "location": "Colombia",<br/>
  "description": "Centro Democr\u00e1tico. Mano Firme, Coraz\u00f3n Grande - Partido Pol\u00edtico.",<br/>
  "url": "https://t.co/O7tiANYpeT",<br/>
  "entities": {<br/>
    "url": {<br/>
      "urls": [<br/>
        {<br/>
          "url": "https://t.co/O7tiANYpeT",<br/>
          "expanded_url": "http://centrodemocratico.com",<br/>
          "display_url": "centrodemocratico.com",<br/>
          "indices": [<br/>
            0,<br/>
            23<br/>
          ]<br/>
        }<br/>
      ]<br/>
    },<br/>
    "description": {<br/>
      "urls": []<br/>
    }<br/>
  },<br/>
  "protected": false,<br/>
  "followers_count": 291609,<br/>
  "friends_count": 314,<br/>
  "listed_count": 517,<br/>
  "created_at": "Wed Jan 23 22:30:02 +0000 2013",<br/>
  "favourites_count": 9915,<br/>
  "utc_offset": null,<br/>
  "time_zone": null,<br/>
  "geo_enabled": true,<br/>
  "verified": true,<br/>
  "statuses_count": 192040,<br/>
  "lang": "es",<br/>
  "status": {<br/>
    "created_at": "Tue Mar 05 01:44:42 +0000 2019",<br/>
    "id": 1102746728820813825,<br/>
    "id_str": "1102746728820813825",<br/>
    "text": "Comenzamos los acercamientos con los candidatos a avales para alcaldes, gobernadores, diputados, concejales y miemb\u2026 https://t.co/Hv7uZML9Xi",<br/>
    "truncated": true,<br/>
    "entities": {<br/>
      "hashtags": [],<br/>
      "symbols": [],<br/>
      "user_mentions": [],<br/>
      "urls": [<br/>
        {<br/>
          "url": "https://t.co/Hv7uZML9Xi",<br/>
          "expanded_url": "https://twitter.com/i/web/status/1102746728820813825",<br/>
          "display_url": "twitter.com/i/web/status/1\u2026",<br/>
          "indices": [<br/>
            117,<br/>
            140<br/>
          ]<br/>
        }<br/>
      ]<br/>
    },<br/>
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",<br/>
    "in_reply_to_status_id": null,<br/>
    "in_reply_to_status_id_str": null,<br/>
    "in_reply_to_user_id": null,<br/>
    "in_reply_to_user_id_str": null,<br/>
    "in_reply_to_screen_name": null,<br/>
    "geo": null,<br/>
    "coordinates": null,<br/>
    "place": null,<br/>
    "contributors": null,<br/>
    "is_quote_status": false,<br/>
    "retweet_count": 119,<br/>
    "favorite_count": 269,<br/>
    "favorited": false,<br/>
    "retweeted": false,<br/>
    "lang": "es"<br/>
  },<br/>
  "contributors_enabled": false,<br/>
  "is_translator": false,<br/>
  "is_translation_enabled": false,<br/>
  "profile_background_color": "C0DEED",<br/>
  "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",<br/>
  "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",<br/>
  "profile_background_tile": false,<br/>
  "profile_image_url": "http://pbs.twimg.com/profile_images/1088570694198312960/hQrOT-j-_normal.jpg",<br/>
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/1088570694198312960/hQrOT-j-_normal.jpg",<br/>
  "profile_banner_url": "https://pbs.twimg.com/profile_banners/1115440213/1549500542",<br/>
  "profile_link_color": "1DA1F2",<br/>
  "profile_sidebar_border_color": "C0DEED",<br/>
  "profile_sidebar_fill_color": "DDEEF6",<br/>
  "profile_text_color": "333333",<br/>
  "profile_use_background_image": true,<br/>
  "has_extended_profile": false,<br/>
  "default_profile": true,<br/>
  "default_profile_image": false,<br/>
  "following": true,<br/>
  "live_following": false,<br/>
  "follow_request_sent": false,<br/>
  "notifications": false,<br/>
  "muting": false,<br/>
  "blocking": false,<br/>
  "blocked_by": false,<br/>
  "translator_type": "none"<br/>
}<br/>

Process finished with exit code 0<br/>

## Task 2.3: Tweet pre-processing

### Q23 (Twitter_3.py):

#### The results we have gotten are:<br/>
['RT', '@', 'JordiTorresBCN', ':', 'just', 'an', 'example', '!', ':', 'D', 'http', ':', '//JordiTorres.Barcelona', '#', 'masterMEI']<br/>
['RT', '@JordiTorresBCN', ':', 'just', 'an', 'example', '!', ':D', 'http://JordiTorres.Barcelona', '#masterMEI']<br/>
<br/>
Process finished with exit code 0<br/>

### Q24<br/>
### How long have you been working on this session?<br/>
* 2 hours and a half in total (including the pre-lab homework)<br/>
### What have been the main difficulties you have faced and how have you solved them?<br/>
* Setting up the Twitter Access environment variables in Unix
