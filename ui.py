import cv2
import streamlit as st
from PIL import Image
from color_limit import get_limit

st.set_page_config(page_title="Color Detection", layout="wide")
st.title("Real-time Color Detection")

color_options = {
    "Red": (0, 0, 255),
    "Yellow": (0, 255, 255),
    "Green": (0, 255, 0),
    "Blue": (255, 0, 0),
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Orange": (0, 165, 255),
    "Pink": (203, 192, 255),
    "Violet": (255, 0, 143),
    "Indigo": (130, 0, 75),
    "Custom": "custom"
}


selected_color = st.selectbox("Select Color to Detect", list(color_options.keys()))

if selected_color != "Custom":
    color_rgb = color_options[selected_color]
else:
    b = st.slider("Blue (0–255)", 0, 255, 0)
    g = st.slider("Green (0–255)", 0, 255, 0)
    r = st.slider("Red (0–255)", 0, 255, 0)
    color_rgb = (b, g, r)
    st.write(f"Selected BGR Color: `{color_rgb}`")

start = st.button("Start Detection")
if start:
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Unable to access webcam.")
            break

        hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if selected_color == "Red":
            
            lower1 = (0, 120, 70)
            upper1 = (10, 255, 255)
            lower2 = (170, 120, 70)
            upper2 = (180, 255, 255)
            mask1 = cv2.inRange(hsvimage, lower1, upper1)
            mask2 = cv2.inRange(hsvimage, lower2, upper2)
            mask = mask1 | mask2

        elif selected_color == "Black":
            lower_black = (0, 0, 0)
            upper_black = (180, 255, 50)  
            mask = cv2.inRange(hsvimage, lower_black, upper_black)

        elif selected_color == "White":
            lower_white = (0, 0, 200)
            upper_white = (180, 30, 255)  
            mask = cv2.inRange(hsvimage, lower_white, upper_white)

        else:
    
            lower_limit, upper_limit = get_limit(color=color_rgb)
            mask = cv2.inRange(hsvimage, lower_limit, upper_limit)
        
        mask_img = Image.fromarray(mask)
        bbox = mask_img.getbbox()

        if bbox:
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")

    cap.release()
