<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VIRTUAL DRIVE - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        code {
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

    <h1>VIRTUAL DRIVE</h1>

    <h2>Project Overview</h2>
    <p><strong>VIRTUAL DRIVE</strong> is a real-time webcam-based color detection system designed to provide hands-free controls for racing games such as <strong>Asphalt 9: Legends</strong>. By detecting hand movements and specific color markers, the program translates real-world motions into in-game actions like steering and activating nitro boosts.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Real-time color detection</strong> using OpenCV.</li>
        <li><strong>Virtual steering</strong> through hand movements.</li>
        <li><strong>Game control automation</strong> via key presses using <code>ctypes</code>.</li>
        <li><strong>Optimized for Asphalt 9: Legends</strong> and similar racing games.</li>
        <li><strong>Simple and intuitive interface</strong> with HSV trackbars for fine-tuning color detection.</li>
    </ul>

    <h2>Files in the Project</h2>
    
    <h3>1. corrected_color_detection.py</h3>
    <p>This script captures real-time video feed, detects colors using HSV filtering, and allows the user to fine-tune the detection settings.</p>
    
    <h3>2. directkeys.py</h3>
    <p>Handles sending keyboard inputs to simulate key presses required for in-game actions.</p>

    <h3>3. drum.py</h3>
    <p>The main script that integrates color detection with game controls. It:</p>
    <ul>
        <li>Uses OpenCV to process the webcam feed.</li>
        <li>Identifies movement for left, right, and nitro boost.</li>
        <li>Simulates key presses (<code>A</code>, <code>D</code>, and <code>Space</code>) based on detected movements.</li>
    </ul>

    <h2>Installation & Requirements</h2>
    
    <h3>Prerequisites</h3>
    <p>Ensure you have Python installed, along with the following dependencies:</p>
    <pre><code>pip install numpy opencv-python imutils</code></pre>

    <h3>Running the Project</h3>
    <ol>
        <li><strong>Connect a webcam</strong> to your system.</li>
        <li><strong>Run the script:</strong></li>
        <pre><code>python drum.py</code></pre>
        <li>Adjust the HSV values using <code>corrected_color_detection.py</code> if needed.</li>
        <li>Open Asphalt 9 or a similar game and start playing using hand gestures!</li>
    </ol>

    <h2>Controls</h2>
    <ul>
        <li>Move your <strong>hand left</strong> → Steers left (<code>A</code> key press).</li>
        <li>Move your <strong>hand right</strong> → Steers right (<code>D</code> key press).</li>
        <li>Move your <strong>hand down</strong> → Activates nitro (<code>Space</code> key press).</li>
        <li>Press <strong>'q'</strong> → Exit the program.</li>
    </ul>

    <h2>Notes</h2>
    <ul>
        <li>Ensure <strong>good lighting</strong> conditions for better color detection.</li>
        <li>Adjust the <strong>HSV values</strong> in <code>corrected_color_detection.py</code> for optimal performance.</li>
        <li>Designed for <strong>Windows OS</strong> due to keyboard simulation using <code>ctypes</code>.</li>
    </ul>

    <h2>Author</h2>
    <p>This project was developed as part of a <strong>Semester 5 Mini Project</strong> by [Your Name]. Guided by <strong>Dr. P S More</strong>.</p>

    <h2>Acknowledgments</h2>
    <p>Special thanks to:</p>
    <ul>
        <li>OpenCV and NumPy community.</li>
        <li>DKTE College faculty for their support.</li>
    </ul>

    <hr>
    <p>Enjoy the <strong>Virtual Drive</strong> experience and have fun racing hands-free!</p>

</body>
</html>
