# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
import subprocess
import time
import os
import platform
# from pywinauto.application import Application
# import win32gui
# import win32con
# import time
# from win32api import GetSystemMetrics

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

# Mac Pages app tools
@mcp.tool()
def open_pages() -> dict:
    """Open Pages app on Mac"""
    print("CALLED: open_pages() -> dict:")
    try:
        if platform.system() != "Darwin":
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="This function only works on macOS."
                    )
                ]
            }
        
        # Open Pages app
        subprocess.Popen(["open", "-a", "Pages"])
        time.sleep(2)  # Wait for Pages to open
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Pages app opened successfully"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Pages: {str(e)}"
                )
            ]
        }

@mcp.tool()
def create_new_pages_document() -> dict:
    """Create a new document in Pages"""
    print("CALLED: create_new_pages_document() -> dict:")
    try:
        if platform.system() != "Darwin":
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="This function only works on macOS."
                    )
                ]
            }
        
        # Use AppleScript to create a new document
        apple_script = '''
        tell application "Pages"
            activate
            make new document
        end tell
        '''
        subprocess.run(["osascript", "-e", apple_script])
        time.sleep(1)  # Wait for document to be created
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="New Pages document created successfully"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error creating new document: {str(e)}"
                )
            ]
        }

@mcp.tool()
def add_text_to_pages(text: str) -> dict:
    """Add text to the current Pages document"""
    print(f"CALLED: add_text_to_pages(text: str) -> dict:")
    try:
        if platform.system() != "Darwin":
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="This function only works on macOS."
                    )
                ]
            }
        
        # Use AppleScript to add text to the current document
        apple_script = f'''
        tell application "Pages"
            activate
            tell document 1
                set body text to body text & "{text}"
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", apple_script])
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text added to Pages document: {text}"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error adding text to Pages: {str(e)}"
                )
            ]
        }

@mcp.tool()
def save_pages_document(file_name: str) -> dict:
    """Save the current Pages document with the given filename"""
    print(f"CALLED: save_pages_document(file_name: str) -> dict:")
    try:
        if platform.system() != "Darwin":
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="This function only works on macOS."
                    )
                ]
            }
        
        # Ensure the filename has the .pages extension
        if not file_name.endswith('.pages'):
            file_name += '.pages'
        
        # Get the user's Documents folder path
        documents_path = os.path.expanduser("~/Documents")
        full_path = os.path.join(documents_path, file_name)
        
        # Use AppleScript to save the document
        apple_script = f'''
        tell application "Pages"
            activate
            tell document 1
                save in "{full_path}"
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", apple_script])
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Document saved as {file_name} in Documents folder"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error saving Pages document: {str(e)}"
                )
            ]
        }

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle in Paint from (x1,y1) to (x2,y2)"""
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Get primary monitor width to adjust coordinates
        primary_width = GetSystemMetrics(0)
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(0.2)
        
        # Click on the Rectangle tool using the correct coordinates for secondary screen
        paint_window.click_input(coords=(530, 82 ))
        time.sleep(0.2)
        
        # Get the canvas area
        canvas = paint_window.child_window(class_name='MSPaintView')
        
        # Draw rectangle - coordinates should already be relative to the Paint window
        # No need to add primary_width since we're clicking within the Paint window
        canvas.press_mouse_input(coords=(x1+2560, y1))
        canvas.move_mouse_input(coords=(x2+2560, y2))
        canvas.release_mouse_input(coords=(x2+2560, y2))
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def add_text_in_paint(text: str) -> dict:
    """Add text in Paint"""
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(0.5)
        
        # Click on the Rectangle tool
        paint_window.click_input(coords=(528, 92))
        time.sleep(0.5)
        
        # Get the canvas area
        canvas = paint_window.child_window(class_name='MSPaintView')
        
        # Select text tool using keyboard shortcuts
        paint_window.type_keys('t')
        time.sleep(0.5)
        paint_window.type_keys('x')
        time.sleep(0.5)
        
        # Click where to start typing
        canvas.click_input(coords=(810, 533))
        time.sleep(0.5)
        
        # Type the text passed from client
        paint_window.type_keys(text)
        time.sleep(0.5)
        
        # Click to exit text mode
        canvas.click_input(coords=(1050, 800))
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text:'{text}' added successfully"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def open_paint() -> dict:
    """Open Microsoft Paint maximized on secondary monitor"""
    global paint_app
    try:
        paint_app = Application().start('mspaint.exe')
        time.sleep(0.2)
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Get primary monitor width
        primary_width = GetSystemMetrics(0)
        
        # First move to secondary monitor without specifying size
        win32gui.SetWindowPos(
            paint_window.handle,
            win32con.HWND_TOP,
            primary_width + 1, 0,  # Position it on secondary monitor
            0, 0,  # Let Windows handle the size
            win32con.SWP_NOSIZE  # Don't change the size
        )
        
        # Now maximize the window
        win32gui.ShowWindow(paint_window.handle, win32con.SW_MAXIMIZE)
        time.sleep(0.2)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Paint opened successfully on secondary monitor and maximized"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Paint: {str(e)}"
                )
            ]
        }
# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

# Gmail tool
@mcp.tool()
def send_email_via_gmail(recipient_email: str, subject: str, message: str) -> dict:
    """Send an email via Gmail"""
    print(f"CALLED: send_email_via_gmail(recipient_email: str, subject: str, message: str) -> dict:")
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        # Get Gmail credentials from environment variables
        sender_email = os.getenv("GMAIL_USERNAME")
        sender_password = os.getenv("GMAIL_APP_PASSWORD")


        

        
        if not sender_email or not sender_password:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Gmail credentials not found. Please set GMAIL_USERNAME and GMAIL_APP_PASSWORD environment variables."
                    )
                ]
            }
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add body
        msg.attach(MIMEText(message, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Email sent successfully to {recipient_email}"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error sending email: {str(e)}"
                )
            ]
        }

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
