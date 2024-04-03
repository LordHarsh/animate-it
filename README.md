# AnimateIt: Animated Text Overlay for Videos

This Python project adds customizable animated text overlays to your videos. It utilizes OpenCV (cv2) for video processing and provides flexibility in text styling and animation.

## Features

* **Multiple Text Overlays:** Add several different animated text elements to your videos.
* **Customization:** Control the following for each text element:
    * Font (using OpenCV font faces)
    * Font size
    * Color (BGR values)
    * Line thickness
    * Start and end positions
    * Animation duration (in frames)

## Prerequisites

* **Python 3** ([https://www.python.org/](https://www.python.org/))
* **OpenCV**  (`pip install opencv-python`)

**Project Structure**

* `main.py`: The main Python script containing the animation logic.
* `data/`: 
    * `vid.mp4`: A sample input video file.
    * `output_vid.mp4`: An example output video with text overlay (if already generated).

## How to Run the Project

1. **Clone/Download:** Get a copy of this project.
2. **Install OpenCV:** If you haven't already, install OpenCV using `pip install opencv-python`.
3. **Adjust Paths (Optional):** If necessary, modify the video input ('video_path') and output paths in the `animated_text_overlay.py` script.
4. **Customize Text Animations:** Edit the `texts` list within `animated_text_overlay.py` to create and configure your desired text overlays.
5. **Execute:** Run the script from your terminal: `python animated_text_overlay.py`

Your output video with the animated text will be saved as 'output_video.mp4'.

## Example Usage

Below is a sample configuration for the `texts` list:

```python
texts = [
    {
        'text': "Exciting Overlay!", 
        'font_face': cv2.FONT_HERSHEY_TRIPLEX,
        'font_scale': 1.5, 
        'color': (0, 128, 255),  # Orange
        'thickness': 3,
        'start_pos': (20, height - 50),
        'end_pos': (width // 2, 50),  # Moves to the center-top
        'num_frames': 120
    },
]
```

## Further Development

* Experiment with different animation trajectories!
* Explore more advanced text effects provided by OpenCV. 
