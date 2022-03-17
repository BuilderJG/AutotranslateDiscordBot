# Autotranslate Discord Bot by BuilderJG
A Discord Bot made to automatically translate messages in a channel to a different channel using discord.py and deep_translator.
### Requirements:
discord.py\
deep_translator\
json

### Use:
Simply format the `data.json` file like this:\
`{"translatechannels": {"fromchannelid": ["tochannelid", "language"]}}`\
and replace `fromchannelid` and `tochannelid` with the ids of the channels and replace `language` with a language from this list:

`afrikaans, albanian, amharic, arabic, armenian, azerbaijani, basque, belarusian, bengali, bosnian, bulgarian, catalan, cebuano, chichewa, chinese (simplified), chinese (traditional), corsican, croatian, czech, danish, dutch, english, esperanto, estonian, filipino, finnish, french, frisian, galician, georgian, german, greek, gujarati, haitian creole, hausa, hawaiian, hebrew, hindi, hmong, hungarian, icelandic, igbo, indonesian, irish, italian, japanese, javanese, kannada, kazakh, khmer, kinyarwanda, korean, kurdish, kyrgyz, lao, latin, latvian, lithuanian, luxembourgish, macedonian, malagasy, malay, malayalam, maltese, maori, marathi, mongolian, myanmar, nepali, norwegian, odia, pashto, persian, polish, portuguese, punjabi, romanian, russian, samoan, scots gaelic, serbian, sesotho, shona, sindhi, sinhala, slovak, slovenian, somali, spanish, sundanese, swahili, swedish, tajik, tamil, tatar, telugu, thai, turkish, turkmen, ukrainian, urdu, uyghur, uzbek, vietnamese, welsh, xhosa, yiddish, yoruba, zulu`
