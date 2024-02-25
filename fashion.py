import cv2
import numpy as np
import streamlit as st
from insightface.app import FaceAnalysis
import tempfile
import os
from pathlib import Path


st.title("👗Fashion Bot")
base_path = Path('dresses/dresses')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, width=400)
    
    # Convert the uploaded file to bytes, then to a numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Initialize the FaceAnalysis app
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    
    # Perform face analysis
    faces = app.get(img)
    
    if faces:
        # Example to display the bounding box of the first detected face
        gender = faces[0].gender
        if gender == 1:
            central_path = base_path / 'Central India' / 'Boy'
            east_path = base_path / 'East India' / 'Boy'
            north_path = base_path / 'North India' / 'Boy'
            northeast_path = base_path / 'Northeast' / 'Boy'
            south_path = base_path / 'South India' / 'Boy'
            west_path = base_path / 'West India' / 'Boy'
            st.header('Central India')
            for x in central_path.iterdir():
                st.image(f'{x}', width=400)
            
            st.header('East India')
            for x in east_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('North India')
            for x in north_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('Northeast India')
            for x in northeast_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('South India')
            for x in south_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('Weast India')
            for x in west_path.iterdir():
                st.image(f'{x}', width=400)
            
            
        else:
            central_path = base_path / 'Central India' / 'Girl'
            east_path = base_path / 'East India' / 'Girl'
            north_path = base_path / 'North India' / 'Girl'
            northeast_path = base_path / 'Northeast' / 'Girl'
            south_path = base_path / 'South India' / 'Girl'
            west_path = base_path / 'West India' / 'Girl'
            st.header('Central India')
            for x in central_path.iterdir():
                st.image(f'{x}', width=400)
            
            st.header('East India')
            for x in east_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('North India')
            for x in north_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('Northeast India')
            for x in northeast_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('South India')
            for x in south_path.iterdir():
                st.image(f'{x}', width=400)

            st.header('Weast India')
            for x in west_path.iterdir():
                st.image(f'{x}', width=400)       
        # If you want to access gender, ensure your model supports it and you know how to access the information
        # This part of the code might need to be adjusted based on your model and `insightface` version
    else:
        st.write("No faces detected")
