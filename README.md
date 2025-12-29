# iCkernel (Interactive C Kernel) for Jupyter

<div align="right">
  <a href="README_kr.md">🇰🇷 한국어 설명 (Korean)</a>
</div>

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

**A Jupyter Notebook kernel for executing C language code.**

Existing Jupyter C kernels often have issues with standard input (`scanf`).
In particular, standard input functions may not work smoothly on **Windows** environments.

**ic-kernel** improves these compatibility issues, allowing standard input/output to work correctly regardless of the OS.

---

## Key Features

* **Cross-Platform:** Works everywhere, including Windows, macOS, and Linux (Ubuntu).
* **Jupyter Input Support:** When `scanf` or `fgets` is executed, an **input box** appears immediately at the bottom (Same experience as a terminal).
* **Infinite Loop Prevention:** Even if you accidentally run `while(1)`, you can stop it immediately by pressing the **[⏹ Stop]** button in Jupyter.
* **Error Coloring:** Compilation errors are highlighted in **Red/Yellow**, making it easy to identify the cause of the problem.
* **Magic Commands:** You can freely add math libraries or compilation options using `//%cflags -lm`.

---

## Installation Guide

This kernel supports local PC use only.
To use this kernel, you need **Python** and a **C Compiler (GCC)**.

### Step 1: Check Python Installation

1. Open your terminal (CMD) and enter the following command:
    ```bash
    python --version
    ```
2. If the version is `3.8` or higher, you are good to go!
3. If an error occurs, download and install Python from the [Official Python Website](https://www.python.org/downloads/).
    * ⚠️ **Warning:** You **MUST** check the **"Add Python to PATH"** box at the bottom of the installation screen!

### Step 2: Install GCC Compiler (Per OS)

Follow the instructions for your operating system.

#### Windows Users (MinGW-w64)

1. Go to the **[WinLibs Download Link](https://winlibs.com/#download-release)**.
2. Download the latest **Zip archive** (UCRT runtime).
3. Extract the downloaded zip file to the root of your C drive (e.g., `C:\mingw64`).
4. **Set Environment Variables (Required):**
    * Search for **"Edit the system environment variables"** in the Windows search bar and open it.
    * Click the **[Environment Variables...]** button -> Under **[System variables]**, double-click **`Path`**.
    * Click **[New]** -> Enter `C:\mingw64\bin` and press Enter.
    * Click [OK] to close all windows.
5. **Verify:** Open a new CMD window and type `gcc --version`. If the version is displayed, success!

#### macOS Users

Open the terminal and enter the following command to install Xcode Command Line Tools.

```bash
xcode-select --install
```

#### Linux (Ubuntu) Users

Open the terminal and install GCC using the commands below.

```bash
sudo apt update
sudo apt install build-essential
```

### Step 3: Install the Kernel (Final)

Download this repository (folder), open a terminal inside the folder, and enter the following two lines.

```bash
# 1. Install Jupyter and required libraries
pip install .

# 2. Register the kernel (Auto-install script)
install-ic-kernel
```

When you see the message "✅ Interactive C Kernel installed successfully!", you are ready.

---

## Usage

1. Type `jupyter notebook` in your terminal to start it.
2. Click the **[New]** button in the top right and select **Interactive C Kernel**.
3. Write and run(`Shift + Enter`) your C code!

### Try Example Codes

#### 1. Input (`scanf`)

```c
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age: ");
    scanf("%d", &age); // An input box will appear below!
    printf("You are %d years old.\n", age);
    return 0;
}
```

#### 2. Using Math Functions (Magic Commands)

When using headers like `math.h`, add the `//%cflags` option at the very top of your code.

```c
//%cflags -lm
#include <stdio.h>
#include <math.h>

int main() {
    printf("Square root of 2: %f\n", sqrt(2.0));
    return 0;
}
```

#### 3. Check Error Messages

Try making a syntax error intentionally. The error location will be highlighted in **Red**.

```c
#include <stdio.h>
int main() {
    printf("I missed the semicolon") // Error!
    return 0;
}
```