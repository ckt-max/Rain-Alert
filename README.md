# Rain-Alert
Sending an SMS when the weather prediction says that it's about to rain, so that the person can carry an umbrella with them

Steps:

-- The code first accesses the Own Weather Map (OWM) API with it's API key ( you need to register on their website for that)
-- Then check if the information says that it's gonna rain in the next 12 hours
-- If it does then we send an SMS to the user via Twilio API, using their phone number which we get through by registering on their website
-- Twilio also need to install a couple of more stuff which is well documented on their website
-- Twilio uses an Account SID and an authorization token to log in
