#Overview
This is microservice(written in python Flask) that translates a given sentence or paragraph to Pig Latin.

###Pig Latin

For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added.
eg. "glove" → "oveglay" , "pig" → "igpay"

For words that begin with vowel sounds or a silent letter, one just adds "yay" to the end.
eg. "eat" → "eatyay", "omelet" → "omeletyay", "are" → "areyay"

The punctuation is preserved. For simplicity we assume that only alpha numeric characters and apostrophe(') are letters of a word, any other characters like whitespaces, newlines, other punctuation marks and special characters are left as it is.

eg. "That's right! Pigs are awesome! hel-ooo..." → "At'sthay ightray! Igspay areyay awesomeyay! elhay-oooyay..."

#Requirements
Python 2.7

pip

virtualenv

#Install
make install

#Start Service
sudo make start

#Stop Service
sudo make stop

#Run Tests
make test

#Api Documentation
method : POST

endpoint : /translate

form data format : (key : text, value : string_to_translate)

```
curl -X POST -F "text=Pigs are cool." http://localhost/translate

{
  "text_piglatin": "Igspay areyay oolcay."
}
```

#Comments for production deployment
This flask service is a minimal application and it will not handle more than one request at a time. It also does not scale well.

Some options to handle this situation :

1. gunicorn with nginx [http://docs.gunicorn.org/en/stable/deploy.html](http://docs.gunicorn.org/en/stable/deploy.html)
2. AWS Elastic Beanstalk which has Apache support

More details : [http://flask.pocoo.org/docs/0.11/deploying/](http://flask.pocoo.org/docs/0.11/deploying/)
