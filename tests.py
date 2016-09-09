import json
import unittest
from flask import jsonify
from app import app

test_input = (
	"pig",
	"banana",
	"trash",
	"happy",
	"duck",
	"glove",
	"eat",
	"omelet",
	"are",
	"Pigs are awesome!!!",
	"I'm searching ... oh! found it. Let's go to \"zoo\"",
	"Testing for new line \n\t Pig asked : can we can do it?"
);

test_output = (
	"igpay",
	"ananabay",
	"ashtray",
	"appyhay",
	"uckday",
	"oveglay",
	"eatyay",
	"omeletyay",
	"areyay",
	"Igspay areyay awesomeyay!!!",
	"I'myay earchingsay ... ohyay! oundfay ityay. Et'slay ogay otay \"oozay\"",
	"Estingtay orfay ewnay inelay \n\t Igpay askedyay : ancay eway ancay oday ityay?"
);

class PigLatinTest(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		self.app = app.test_client()

	def translate(self, text):
		return self.app.post('/translate', data=dict(
			text=text
		), follow_redirects=True)

	def test_translate(self):
		for i in range(len(test_input)):
			k = test_input[i]
			v = test_output[i]
			response = self.translate(k)
			p_t = json.loads(response.data)['text_piglatin']
			assert p_t == v, \
				"Got %r expecting %r for input %r" % (p_t, v, k)
if __name__ == '__main__':
	unittest.main()
