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

#LasMásLeídas | El asesinato cometido para ocultar peligroso descubrimiento matemático ⬇ (Vía @bbcmundo) https://t.co/ajLmfaiIT9
{
  "created_at": "Tue Mar 05 08:00:13 +0000 2019",
  "id": 1102841228457111553,
  "id_str": "1102841228457111553",
  "text": "#LasM\u00e1sLe\u00eddas | El asesinato cometido para ocultar peligroso descubrimiento matem\u00e1tico \u2b07 (V\u00eda @bbcmundo) https://t.co/ajLmfaiIT9",
  "truncated": false,
  "entities": {
    "hashtags": [
      {
        "text": "LasM\u00e1sLe\u00eddas",
        "indices": [
          0,
          13
        ]
      }
    ],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "bbcmundo",
        "name": "BBC News Mundo",
        "id": 10012122,
        "id_str": "10012122",
        "indices": [
          94,
          103
        ]
      }
    ],
    "urls": [
      {
        "url": "https://t.co/ajLmfaiIT9",
        "expanded_url": "http://ow.ly/j3cq30nVdU5",
        "display_url": "ow.ly/j3cq30nVdU5",
        "indices": [
          105,
          128
        ]
      }
    ]
  },
  "source": "<a href=\"https://www.hootsuite.com\" rel=\"nofollow\">Hootsuite Inc.</a>",
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "in_reply_to_screen_name": null,
  "user": {
    "id": 9633802,
    "id_str": "9633802",
    "name": "EL TIEMPO",
    "screen_name": "ELTIEMPO",
    "location": "Bogot\u00e1, Colombia",
    "description": "Principales noticias de Colombia, el mundo, deportes, econom\u00eda, pol\u00edtica, tecnolog\u00eda, cultura, estilo de vida, tendencias y mucho m\u00e1s. El Tiempo Casa Editorial.",
    "url": "http://t.co/pXsWZAle5x",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "http://t.co/pXsWZAle5x",
            "expanded_url": "http://www.eltiempo.com",
            "display_url": "eltiempo.com",
            "indices": [
              0,
              22
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 6563843,
    "friends_count": 26159,
    "listed_count": 15584,
    "created_at": "Tue Oct 23 20:03:24 +0000 2007",
    "favourites_count": 6519,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 482612,
    "lang": "es",
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": true,
    "profile_background_color": "06609C",
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
    "profile_background_tile": true,
    "profile_image_url": "http://pbs.twimg.com/profile_images/1053511496972541953/Po6LEiC5_normal.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1053511496972541953/Po6LEiC5_normal.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/9633802/1551042126",
    "profile_link_color": "EB0C2A",
    "profile_sidebar_border_color": "000000",
    "profile_sidebar_fill_color": "FFFFFF",
    "profile_text_color": "000000",
    "profile_use_background_image": true,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": true,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 0,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "es"
}
{
  "id": 1115440213,
  "id_str": "1115440213",
  "name": "Centro Democr\u00e1tico",
  "screen_name": "CeDemocratico",
  "location": "Colombia",
  "description": "Centro Democr\u00e1tico. Mano Firme, Coraz\u00f3n Grande - Partido Pol\u00edtico.",
  "url": "https://t.co/O7tiANYpeT",
  "entities": {
    "url": {
      "urls": [
        {
          "url": "https://t.co/O7tiANYpeT",
          "expanded_url": "http://centrodemocratico.com",
          "display_url": "centrodemocratico.com",
          "indices": [
            0,
            23
          ]
        }
      ]
    },
    "description": {
      "urls": []
    }
  },
  "protected": false,
  "followers_count": 291609,
  "friends_count": 314,
  "listed_count": 517,
  "created_at": "Wed Jan 23 22:30:02 +0000 2013",
  "favourites_count": 9915,
  "utc_offset": null,
  "time_zone": null,
  "geo_enabled": true,
  "verified": true,
  "statuses_count": 192040,
  "lang": "es",
  "status": {
    "created_at": "Tue Mar 05 01:44:42 +0000 2019",
    "id": 1102746728820813825,
    "id_str": "1102746728820813825",
    "text": "Comenzamos los acercamientos con los candidatos a avales para alcaldes, gobernadores, diputados, concejales y miemb\u2026 https://t.co/Hv7uZML9Xi",
    "truncated": true,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https://t.co/Hv7uZML9Xi",
          "expanded_url": "https://twitter.com/i/web/status/1102746728820813825",
          "display_url": "twitter.com/i/web/status/1\u2026",
          "indices": [
            117,
            140
          ]
        }
      ]
    },
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 119,
    "favorite_count": 269,
    "favorited": false,
    "retweeted": false,
    "lang": "es"
  },
  "contributors_enabled": false,
  "is_translator": false,
  "is_translation_enabled": false,
  "profile_background_color": "C0DEED",
  "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
  "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
  "profile_background_tile": false,
  "profile_image_url": "http://pbs.twimg.com/profile_images/1088570694198312960/hQrOT-j-_normal.jpg",
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/1088570694198312960/hQrOT-j-_normal.jpg",
  "profile_banner_url": "https://pbs.twimg.com/profile_banners/1115440213/1549500542",
  "profile_link_color": "1DA1F2",
  "profile_sidebar_border_color": "C0DEED",
  "profile_sidebar_fill_color": "DDEEF6",
  "profile_text_color": "333333",
  "profile_use_background_image": true,
  "has_extended_profile": false,
  "default_profile": true,
  "default_profile_image": false,
  "following": true,
  "live_following": false,
  "follow_request_sent": false,
  "notifications": false,
  "muting": false,
  "blocking": false,
  "blocked_by": false,
  "translator_type": "none"
}

Process finished with exit code 0

## Task 2.3: Tweet pre-processing
