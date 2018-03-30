# Copyright 2018 Sergio Oller
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

from mycroft.skills.core import MycroftSkill
from adapt.intent import IntentBuilder
from mycroft.util.log import getLogger

__author__ = 'zeehio'

LOGGER = getLogger(__name__)

class EnclosureTextSkill(MycroftSkill):
    def __init__(self):
        super(EnclosureTextSkill, self).__init__(name="EnclosureTextSkill")

    def initialize(self):
        encl_text_intent = IntentBuilder("EnclosureTextIntent")\
            .require("write").require("text").build()
        self.register_intent(encl_text_intent, self.handle_write_intent)

    def handle_write_intent(self, message):
        utterance = message.data['utterance']
        text = message.data.get("text")
        LOGGER.debug("Text: " + text)
        self.enclosure.mouth_text(text)
        return True


def create_skill():
    return EnclosureTextSkill()

