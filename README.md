# FSRCNN_Waifu
Inspired by Waifu2X which use SRCNN: https://github.com/nagadomi/waifu2x <br/>
Waifu2X web app: http://waifu2x.udp.jp/index.html <br/>
Replicating the FSRCNN model (faster and lighter version of SRCNN) in this paper: http://mmlab.ie.cuhk.edu.hk/projects/FSRCNN.html <br/>
Trained on 1000 high resolution images from https://pixiv.net <br/>
Demo image: https://www.pixiv.net/artworks/79923044 <br/>

Input image: <br/>
![alt text](https://github.com/Onenightcarnival/FSRCNN_Waifu/blob/master/input.png)

Raw output from model: <br/>
![alt text](https://github.com/Onenightcarnival/FSRCNN_Waifu/blob/master/2x%20up%20no%20denoise%20input.png)

Denoise, this is what we want: <br/>
![alt text](https://github.com/Onenightcarnival/FSRCNN_Waifu/blob/master/2x%20up%20input.png)

# Run as Web App
required package: streamlit, tensorflow, cv2, keras, PIL <br>
In terminal, run "streamlit run app.py" <br>
