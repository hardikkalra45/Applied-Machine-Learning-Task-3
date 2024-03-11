import requests
import time
import unittest
import subprocess

import pickle
from score import *

class TestScoreFunction(unittest.TestCase):

    def test_crash_test(self):
        # Ensure the function does not crash
        model = pickle.load(open('E:/model.pkl','rb'))
        text = "Hello."
        threshold = 0.5
        result = score(text, model, threshold)
        self.assertIsNotNone(result)

    def test_ioformat_test(self):
        # Ensure the input/output formats/types are as expected
        model = pickle.load(open('E:/model.pkl','rb'))

        text = "Hello."
        threshold = 0.5
        prediction, propensity = score(text, model, threshold)
        self.assertIsInstance(prediction, bool)
        self.assertIsInstance(propensity, float)

    def test_prediction_value(self):
        # Ensure prediction value is 0 or 1
        model = pickle.load(open('E:/model.pkl','rb'))
 
        text = "Hello."
        threshold = 0.5
        prediction, _ = score(text, model, threshold)
        self.assertIn(prediction, [0, 1])

    def test_propensity_value(self):
        # Ensure propensity score is between 0 and 1
        model = pickle.load(open('E:/model.pkl','rb'))

        text = "Hello."
        threshold = 0.6
        _, propensity = score(text, model, threshold)
        self.assertGreaterEqual(propensity, 0)
        self.assertLessEqual(propensity, 1)

    def test_threshold_0(self):
        # If the threshold is set to 0, prediction should always be 1
        model = pickle.load(open('E:/model.pkl','rb'))

        text = "Hello."
        threshold = 0
        prediction, _ = score(text, model, threshold)
        self.assertEqual(prediction, 1)

    def test_threshold_1(self):
        # If the threshold is set to 1, prediction should always be 0
        model = pickle.load(open('E:/model.pkl','rb'))

        text = "Hello."
        threshold = 1
        prediction, _ = score(text, model, threshold)
        self.assertEqual(prediction, 0)

    def test_spam_input(self):
        # On a spam input, the prediction should be 1
        model = pickle.load(open('E:/model.pkl','rb'))

        text = "las vegas high rise boom  las vegas is fast becoming a major metropolitan city ! 60 +  new high rise towers are expected to be built on and around the las vegas strip  within the next 3 - 4 years , that ' s 30 , 000 + condominiums !  this boom has just begun ! buy first . . . early phase ,  pre - construction pricing is now available on las vegas high rises including  trump , cosmopolitan , mgm , turnberry , icon , sky , among others .  join the interest list :  http : / / www . verticallv . com  message has been sent to you by realty one highrise . learn more at www . verticallv . comif you  wish to be excluded from future mailings , please reply with the word remove in  the subject line ."
        threshold = 0.5
        prediction, _ = score(text, model, threshold)
     
        self.assertEqual(prediction, True)

    def test_not_spam_input(self):
        # On a non-spam input, the prediction should be 0
        model = pickle.load(open('E:/model.pkl','rb'))

        text = "re : transition to research group - an update - anshuman shrivastava  molly : in order that i may proceed with the visa application for mr .  anshuman shrivastava , i will need from enron ' s h . r . department , the following  information :  a copy of a job offer letter / contract / assignment letter for his us position  with us salary  a job description of the position in the us  a salary range for that position  co # and cost center #  please let me have this at your earliest convenience .  many thanks  margaret  enron north america corp .  from : molly magee 01 / 19 / 2001 06 : 08 pm  to : margaret daffin / hou / ect @ ect  cc : vince j kaminski / hou / ect @ ect  subject : re : transition to research group - an update  once again , margaret , we are in your debt . vince , let ' s get together some  time next week and see where you would like us to go with this . . .  molly  margaret daffin  01 / 19 / 2001 03 : 27 pm  to : molly magee / hou / ect @ ect  cc : vince j kaminski / hou / ect @ ect  subject : re : transition to research group - an update  molly : just to be sure that everyone understands , anshuman cannot work in  the us on a bl visa - he can only come here for business meetings and  training .  we will have to get him the ll visa in order for him to work in the us .  margaret  enron north america corp .  from : molly magee 01 / 19 / 2001 02 : 53 pm  to : vince j kaminski / hou / ect @ ect  cc : margaret daffin / hou / ect @ ect  subject : re : transition to research group - an update  thank you so much for the information , vince . i hope that you have a great  weekend !  molly  vince j kaminski  01 / 19 / 2001 02 : 39 pm  to : molly magee / hou / ect @ ect  cc : vince j kaminski / hou / ect @ ect  subject : re : transition to research group - an update  molly ,  i shall ask sandeep to do it when he comes back from india next week .  i have just learned that anshuman has bl visa and he can start on a project  as a person  delegated by dhabol power company to houston . to be absolutely above the line ,  i would still arrange the ll visa .  vince  enron north america corp .  from : molly magee 01 / 19 / 2001 10 : 44 am  to : vince j kaminski / hou / ect @ ect  cc : margaret daffin / hou / ect @ ect  subject : re : transition to research group - an update  i agree that it makes sense to put the ll in place . there are several things  we will need from you in order to start the visa process . the first is a  fairly detailed job description for anshuman . secondly , we also need to know  whether or not he will be in a managerial position here and / or managing a  project . if there is someone else in your group who can furnish this job  description , just let me know and i will be happy to contact him / her .  as for sandeep , i have been told that he is a u . s . resident so there should  be no problems with him . margaret daffin will be contacting him to be  absolutely sure .  thanks ,  molly  vince j kaminski  01 / 19 / 2001 10 : 21 am  to : molly magee / hou / ect @ ect  cc : vince j kaminski / hou / ect @ ect  subject : re : transition to research group - an update  molly ,  let ' s get ll for anshuman , just in case . i am sure he will stay here for a  while  once he comes . it is quite obvious jeff shankman will have to keep him  longer ,  given the priority of the project .  i assume there are no problems with sandeep .  thanks .  vince  enron north america corp .  from : molly magee 01 / 19 / 2001 09 : 54 am  to : vince j kaminski / hou / ect @ ect  cc : margaret daffin / hou / ect @ ect  subject : re : transition to research group - an update  thank you for the update , vince . i have been working with margaret daffin  with regard to anshuman ' s visa status . we will have to get an ll visa in  place before he can come to the united states , even in a temporary  capacity . do you want to move forward with that effort at this time , or  is the possibility of him coming to the u . s . so remote that it wouldn ' t be  worth the time and money right now ?  molly  vince j kaminski  01 / 19 / 2001 09 : 42 am  to : molly magee / hou / ect @ ect  cc : vince j kaminski / hou / ect @ ect  subject : transition to research group - an update  molly ,  this is an update on anshuman . please , see below . it seems  that his transfer is not an issue for the time being .  we can put it on a back - burner till he gets here .  vince  p . s . the relevant section .  i also spoke about anshuman , and there was resistance to his leaing for such  a long time . however , i have agreement from folks here to send him to  houston for a shorter stint on dpc budget . i will try to finalize that  before i leave . i will call you in the evening to just chat .  - - - - - - - - - - - - - - - - - - - - - - forwarded by vince j kaminski / hou / ect on 01 / 19 / 2001  09 : 45 am - - - - - - - - - - - - - - - - - - - - - - - - - - -  sandeep kohli @ enron _ development  01 / 19 / 2001 04 : 32 am  to : vince j kaminski @ ect  cc :  subject : transition to research group - an update  vince ,  just wanted to let you know that i had a meeting with wade cline ( coo , enron  india ) , neil mcgregor ( president , dpc ) , and mohan gurunath ( cfo , dpc ) today .  though i had already spoken to all of them earlier about my joining your  group , today it became official , and all of them supported the move . i  explained to them what we would be doing , and the results expected from the  henwood study .  dpc would like to pay the costs for the study , and that was mentioned . there  maybe some tax issues etc . that need to be cleared , and other related issues  that i would like to discuss with you , so i will leave them till i get to  houston .  i also spoke about anshuman , and there was resistance to his leaing for such  a long time . however , i have agreement from folks here to send him to  houston for a shorter stint on dpc budget . i will try to finalize that  before i leave . i will call you in the evening to just chat .  i am very thankful to you for giving the opportunity you have . things here  have deteriorated dramatically over the last few weeks . morale is quite down  due to many lay - offs .  i am really looking forward to returning to houston , and the family ! !  regards ,  sandeep ."  
        threshold = 0.5
        prediction, _ = score(text, model, threshold)
     
        self.assertEqual(prediction, False)
        
        
        
class FlaskIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.flask_process = subprocess.Popen(['python', 'E:/app.py'])
        time.sleep(2)

    def tearDown(self):
        shutdown_url = 'http://localhost:5000/shutdown'
        requests.post(shutdown_url)
        self.flask_process.wait()

    def test_flask_endpoint(self):
        url = 'http://localhost:5000/score'
        text_data = {'text': 'Hi.'}
        response = requests.post(url, json=text_data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('prediction', json_response)
        self.assertIn('propensity', json_response)

if __name__ == '__main__':
    unittest.main()

