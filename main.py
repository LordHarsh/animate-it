import cv2
import numpy as np
import random
import argparse

def get_video(video_path):
    """
    Initializes video capture and retrieves video properties.
    
    Parameters:
    - video_path: str, path to the input video file.
    
    Returns:
    - cap: VideoCapture object for the video.
    - width: int, width of the video frames.
    - height: int, height of the video frames.
    - fps: int, frames per second of the video.
    - total_frames: int, total number of frames in the video.
    """
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return cap, width, height, fps, total_frames

def get_text(text, frame, frame_count, width, height, font, font_scale, color, thickness, animation_styles, animation_index):
    """
    Applies the specified text to the frame with an animation style.
    
    Parameters:
    - text: str, the text to be applied.
    - frame: ndarray, the current video frame.
    - frame_count: int, the current frame count.
    - width: int, width of the video frames.
    - height: int, height of the video frames.
    - font: int, font type for the text.
    - font_scale: float, scale factor that is multiplied by the font-specific base size.
    - color: tuple, color of the text in BGR.
    - thickness: int, thickness of the lines used to draw the text.
    - animation_styles: list, list of animation styles.
    - animation_index: int, index to select the animation style.
    
    Returns:
    - frame: ndarray, the modified frame with the text applied.
    """
    # Select animation style
    animation_style = animation_styles[animation_index % len(animation_styles)]
    
    # Calculate current position of text or effect based on animation style
    if animation_style == 'Top to Bottom':
        x = width // 2
        y = int((frame_count % height) * 1.5)  # Move from top to bottom
    elif animation_style == 'Left to Right':
        x = int((frame_count % width) * 1.5)
        y = height // 2  # Move from left to right
    elif animation_style == 'Diagonal':
        x = int((frame_count % width) * 1.5)
        y = int((frame_count % height) * 1.5)  # Move diagonally
    elif animation_style == 'Zoom In':
        font_scale = min(2, 1 + (frame_count % 100) / 50)  # Zoom in effect
        x, y = width // 4, height // 2
    elif animation_style == 'Fade In':
        alpha = (frame_count % 100) / 100
        overlay = frame.copy()
        cv2.putText(overlay, text, (width // 4, height // 2), font, font_scale, color, thickness, cv2.LINE_AA)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        return frame  # For fade in, return the modified frame
    
    # For non-fade animations, add text directly to the frame
    if animation_style != 'Fade In':
        cv2.putText(frame, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
    
    return frame

def write_video(width, height, fps, output_file_name):
    """
    Initializes the video writer.
    
    Parameters:
    - width: int, width of the video frames.
    - height: int, height of the video frames.
    - fps: int, frames per second of the video.
    - output_file_name: str, name of the output video file.
    
    Returns:
    - out: VideoWriter object for the output video.
    """
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file_name, fourcc, fps, (width, height))
    return out

def main(video_path, output_file_name, text):
    """
    Main function to apply text animation to a video.
    
    Parameters:
    - video_path: str, path to the input video file.
    - output_file_name: str, name of the output video file.
    - text: str, text to put on video.
    """
    cap, width, height, fps, total_frames = get_video(video_path)
    out = write_video(width, height, fps, output_file_name)

    fonts = [cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN, cv2.FONT_HERSHEY_DUPLEX,
             cv2.FONT_HERSHEY_COMPLEX, cv2.FONT_HERSHEY_TRIPLEX, cv2.FONT_HERSHEY_COMPLEX_SMALL,
             cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_HERSHEY_SCRIPT_COMPLEX]
    font_index = 0
    font = fonts[font_index]

    font_scale = 1
    thickness = 2
    colors = [(255, 255, 255), (0, 255, 255), (255, 0, 255), (255, 255, 0), 
              (0, 255, 0), (0, 0, 255), (255, 0, 0)]
    color = random.choice(colors)

    animation_styles = ['Top to Bottom', 'Left to Right', 'Diagonal', 'Zoom In', 'Fade In']
    animation_index = 0

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = get_text(text, frame, frame_count, width, height, font, font_scale, color, thickness, animation_styles, animation_index)
        
        out.write(frame)
        
        frame_count += 1
        if frame_count % 100 == 0:  # Change animation style every 100 frames
            animation_index += 1
            color = random.choice(colors)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Applies animated text to a video file.')
    parser.add_argument('video_path', type=str, help='Path to the input video file')
    parser.add_argument('output_file_name', type=str, help='Name of the output video file')
    parser.add_argument('text', type=str, help='Text to overlay on the video')
    
    args = parser.parse_args()

    main(args.video_path, "data/"+args.output_file_name, args.text)
