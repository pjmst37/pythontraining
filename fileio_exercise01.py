from translate import Translator

translator = Translator('ja')
translation = translator.translate("Hello world")
print(translation)