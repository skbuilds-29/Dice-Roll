import streamlit as st
import time
import random
st.title("Dice Roller! 🎲")
face_num = st.slider("How many dice faces would you like?", 1, 20, 6)
if st.button("Roll the Dice! 🎲"):
    dice_faces=[1]
    for i in range(2, face_num+1,1):
        dice_faces.append(i)
    dice_number = random.choice(dice_faces)
    dice_animation = st.image('https://www.animatedimages.org/data/media/710/animated-dice-image-0005.gif')
    with st.spinner("Rolling the dice..."):
        time.sleep(1.5)
    dice_animation.empty()
    st.write("You rolled a " + str(dice_number) + "! 🎉")
