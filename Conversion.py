import asyncio
import Languages 
from googletrans import Translator

async def encode_translate(msg):
    trans = Translator()
    lang_list = list(Languages.LANGUAGES.keys())
    
    detected_obj = await trans.detect(msg)
    lang_code = detected_obj.lang
    lang_ind = lang_list.index(lang_code)
    
    translated_obj = await trans.translate(msg, dest='en')
    english_text = translated_obj.text

    return lang_ind, english_text

async def decode_translate(msg, lang):
    trans = Translator()
    
    lang_list = list(Languages.LANGUAGES.items())
    # lang_code = lang_list[lang_ind]
    
    for key, val in lang_list:
        if val == lang:
            translated_obj = await trans.translate(msg, dest=key)
            final_text = translated_obj.text
            return final_text