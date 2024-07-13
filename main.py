from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


detailed_prompt_template = PromptTemplate(
    input_variables=[
        'occasion', 'event_details', 'personal_style',
        'body_type', 'preferred_colors', 'climate', 'cultural_influences',
        'color_palette', 'preferred_footwear', 'accessory', 'silhouette',
        'age_group', 'gender'
    ],
    template=(
        "I have an exciting event on the horizon—a {occasion}! The details are as follows: {event_details}.\n"
        "I need a standout outfit that will not only suit the occasion but also make a lasting impression. Can you help me craft the perfect look? \n\n"
        "### Outfit Inspiration\n"
        "Consider the following aspects to provide a tailored outfit recommendation:\n"
        "1. **Gender:** I am {gender}.\n"
        "2. **Age Group:** I belong to the {age_group} age group.\n"
        "3. **Personal Style:** I lean towards a {personal_style} style.\n"
        "4. **Body Type:** My body type is {body_type}, and I want to highlight my best features.\n"
        "5. **Preferred Colors:** I love wearing {preferred_colors}.\n"
        "6. **Climate:** The event will take place in a {climate} climate, so please suggest appropriate fabrics and layers.\n"
        "7. **Cultural Influences:** I appreciate styles influenced by {cultural_influences} culture.\n"
        "8. **Color Palette:** I am drawn to a {color_palette} color palette.\n"
        "9. **Preferred Footwear:** I prefer wearing {preferred_footwear}.\n"
        "10. **Accessory:** I like to accentuate my look with a {accessory}.\n"
        "11. **Silhouette:** My favorite silhouette is {silhouette}.\n\n"
        "### Styling Details\n"
        "Based on these details, could you please provide:\n"
        "- A complete outfit suggestion, including specific pieces and styles.\n"
        "- Detailed styling tips, such as suitable fabrics, layering options, and outfit combinations.\n"
        "Additionally, offer advice on:\n"
        "- Color combinations that will enhance the event theme.\n"
        "- Matching accessories that will enhance my overall look.\n"
        "- Footwear recommendations that are both stylish and appropriate for the occasion.\n"
        "- Tips on achieving a cohesive and polished appearance, keeping in mind the silhouette I prefer.\n\n"
        "I am looking forward to your expert advice to help me become the fashion icon of the event!"
    )
)


advice_chain = LLMChain(llm=llm, prompt=detailed_prompt_template)


if "chatbot_chain" not in st.session_state:
    memory = ConversationBufferWindowMemory(k=3)
    st.session_state.chatbot_chain = ConversationChain(
        llm=llm,
        memory=memory
    )


st.sidebar.title("Fashion Advisor")
page = st.sidebar.selectbox("Choose a section", ["Fashion Advice", "Chatbot"])

if page == "Fashion Advice":
    st.title('Get Personalized Fashion Advice 👗')
    
    occasion = st.text_input("Occasion")
    event_details = st.text_area("Event Details")
    personal_style = st.selectbox("Personal Style", ["elegant", "casual", "bohemian", "sporty", "chic"])
    body_type = st.selectbox("Body Type", ["hourglass", "pear", "apple", "rectangle", "inverted triangle"])
    preferred_colors = st.text_input("Preferred Colors")
    climate = st.selectbox("Climate", ["warm", "cold", "temperate"])
    cultural_influences = st.text_input("Cultural Influences")
    color_palette = st.text_input("Color Palette")
    preferred_footwear = st.text_input("Preferred Footwear")
    accessory = st.text_input("Accessory")
    silhouette = st.text_input("Silhouette")
    age_group = st.selectbox("Age Group", ["0-10", "10-20", "20-35", "35 to 50", "50 and above"])
    gender = st.selectbox("Gender", ["female", "male", "non-binary"])

    if st.button("Get Fashion Advice"):
        response = advice_chain.invoke({
            "occasion": occasion,
            "event_details": event_details,
            "personal_style": personal_style,
            "body_type": body_type,
            "preferred_colors": preferred_colors,
            "climate": climate,
            "cultural_influences": cultural_influences,
            "color_palette": color_palette,
            "preferred_footwear": preferred_footwear,
            "accessory": accessory,
            "silhouette": silhouette,
            "age_group": age_group,
            "gender": gender
        })
        st.write(response["text"])

elif page == "Chatbot":
    st.title("Fashion Chatbot 👠💄👖")
    st.write("Ask me anything about fashion and clothes!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

 
    chat_container = st.container()
    for chat in st.session_state.chat_history:
        with chat_container:
            st.write(f"You: {chat['user']}")
            st.write(f"Bot: {chat['bot']}")

 
    user_input = st.text_input("You: ", key="input")
    if user_input and st.session_state.get("last_user_input") != user_input:
        st.session_state.last_user_input = user_input
        response = st.session_state.chatbot_chain.invoke(user_input)
        st.session_state.chat_history.append({"user": user_input, "bot": response["response"]})
        st.rerun()


    
