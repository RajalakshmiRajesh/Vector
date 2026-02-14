<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Roast My Code] 🎯

## Basic Details

### Team Name: [Vector]

### Team Members
- Member 1: [Rajalakshmi R] - [Jain University]
- Member 2: [Nandana U] - [Jain University]

### Hosted Project Link
[(https://vector-7exv.onrender.com/)]

### Project Description
[An AI-powered "Code Critic" that provides a humorous, multi-perspective intervention on your source code. It transforms boring syntax errors into a sharp, comedic dialogue between three distinct developer archetypes.]

### The Problem statement
[Learning to code is often lonely and dry. Standard compilers give robotic, unhelpful error messages that don't capture the "experience" of a real-world code review or the frustration of messy logic.]

### The Solution
[We built a web application that uses Large Language Models (LLMs) to "roast" user-submitted code. By personifying the feedback through a 13-year-old prodigy, a sarcastic mid-level dev, and an exhausted senior architect, we make code review entertaining and memorable.]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [Python, HTML5, CSS3, JavaScript.]
- Frameworks used: [Flask (Backend).]
- Libraries used: [groq (LLM Integration), python-dotenv (Security), gunicorn (Production Server).]
- Tools used: [VS Code, Git, GitHub, Render (Deployment).]

**For Hardware:**
- Main components: [List main components]
- Specifications: [Technical specifications]
- Tools required: [List tools needed]

---

## Features

List the key features of your project:
- Feature 1: [Multi-Persona Roasting: Generates a conversation between three different developer personalities for a diverse comedic experience]
- Feature 2: [Dynamic UI: Features physics-based floating emojis that respond to the "chaos" of the code review.]
- Feature 3: [Responsive Terminal Output: A styled "Roast Report" container that mimics a professional code audit gone wrong.]
- Feature 4: [Instant LLM Feedback: Powered by Llama 3.3-70B via the Groq Cloud API for near-instant response times.]

---

## Implementation

### For Software:

#### Installation
# Clone the repository
git clone https://github.com/RajalakshmiRajesh/Vector.git

# Install required dependencies
pip install -r requirements.txt

#### Run
# Set your API Key in a .env file first
python app.py

### For Hardware:

#### Components Required
[List all components needed with specifications]

#### Circuit Setup
[Explain how to set up the circuit]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

<img width="1907" height="921" alt="image" src="https://github.com/user-attachments/assets/0bc39945-00af-4da7-bd63-510fb84f2fa0" />

The Landing Page: Featuring the glowing 'Roast My Code' title and questionable code entry area.

<img width="1892" height="908" alt="image" src="https://github.com/user-attachments/assets/f781839a-4b97-42b2-98e5-b8c0e3d0dd47" />

The Roast Report: Showing the AI-generated dialogue between the three developer personas.

<img width="1899" height="904" alt="image" src="https://github.com/user-attachments/assets/4ca538a3-f7b1-416c-bbce-b0b2308235e6" />
Interactive Elements: Floating emojis providing visual feedback on the user's coding 'sins'.

#### Diagrams

**System Architecture:**

The user interacts with the Flask Frontend, which sends code to the Backend. The Backend calls the Groq API (Llama 3.3) and returns the formatted roast to the UI.

**Application Workflow:**

The workflow is a simple request-response cycle optimized for speed using the Groq high-speed inference engine.

---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `(https://vector-7exv.onrender.com/)`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [Submits code for roasting.]
- **Request Body:**
```json
{
  "code": "print('hello world')"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Prompt engineering and persona design.
- System integration and Render deployment troubleshooting.
- UI layout and branding decisions.


*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Rajalakshmi R]: [Frontend design, CSS animations,and UI/UX styling]
- [Nandana U]: [Backend development,Groq API integration, and Render deployment]


---

## License

This project is licensed under the [MIT] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
