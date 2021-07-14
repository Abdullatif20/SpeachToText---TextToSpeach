from ibm_cloud_sdk_core import authenticators
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('ZqyPbF_g_3ggPFZ4wTA6FEbdEfUCe8QJ-ENe_nFxaQVr')

tts = TextToSpeechV1(authenticator = authenticator)
tts.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/c20f7e2b-9125-4d73-a5d8-bfb199848924')

val = input("Enter a Text : ")
with open ('./Speachoutput.mp3', 'wb') as file:
    res = tts.synthesize(val, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    file.write(res.content)
