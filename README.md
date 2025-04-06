# Color Masking & Invisibility Cloak with OpenCV

This is a simple Python script that uses OpenCV to create an "invisibility cloak" effect using color masking in real-time from a webcam feed.

## Features

- Real-time video capture from webcam  
- Dynamic HSV color range adjustment via GUI trackbars  
- Color masking to isolate and replace specific colored areas  
- Combines initial background with live masked feed to create an "invisibility" effect  

## Requirements

- Python 3.x  
- OpenCV  
- NumPy  

Install dependencies using pip:

```bash
pip install opencv-python numpy
```

## Usage

Run the script:

```bash
python invisibility_cloak.py
```

### Controls

- Adjust HSV range using the sliders in the **bars** window to target the specific color to mask.  
- Press **`x`** to exit the application.

## How It Works

1. Captures an initial background frame.  
2. Continuously reads webcam frames and converts them to HSV color space.  
3. Applies a mask based on HSV slider settings.  
4. Combines masked regions from the current frame and background to simulate invisibility.

## Credits

Created by Shashank Singh[@shashankexore](https://github.com/shashankexore)
