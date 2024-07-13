# Myntra WeForShe 2024 Hackathon Phase-2 Submission
## Proposed Idea: Virtual Fashion Styling Assistant
### Team Name: the_simpsons
### Team Members: Ishita Gupta, Monalisa Maity
### University: Delhi Technological University

We will be working on the following 2 themes : -
	1. **Trend Generation** - Use of AI to generate designs and images for upcoming trends
	2. **Engagement on a shopping platform** - Building engagement constructs on a platform which will drive a connect and virality among younger audiences in the country.
     It need not be linked to shopping but needs to be linked to fashion, which will drive users to keep visiting the app on a habitual basis.

**Our Aim**: 
	To create a virtual fashion styling assistant to enhance the shopping experience of Myntra users whilst attracting more users to the app at the same time.
 
 **Description of the Application**
 We have created an application utilizing Python, langchain, GoogleGenerativeAI and streamlit which has two features:
 1. A virtual styling assistant which uses takes input for various parameters like occasion, event_details, personal_style,
    body_type, preferred_colors, climate, cultural_influences, color_palette, preferred_footwear, accessory, silhouette, age_group and gender
    from the users to determine their style preferences and with the help of Google's Gemini 1.5 Pro model, it generates creative and interesting customized styling advice.
 2. A fashion chat bot that can be used by the users to take suggestions for fashion and styling.
    eg: What kinds on clothes will go with a particular type of pair of shoes?
        What kind of earrings will complement my dress?
    
## Instructions to run the code:
1. Create google gemini api key.
2. Download the main.py file and the requirements.txt file which contains the dependencies.
3. Run the following command in terminal:
   ``` streamlit run main.py```
