<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>MsgsaveMailAutoReg
</h1>
<h3> Automated Msgsave email registration using Selenium. To use it, you need to get the 2captcha api key </h3>
<h3> Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<p>Selenium</p>
<p>Faker</p>
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/BeataStultica/MsgsaveMailAutoReg?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/BeataStultica/MsgsaveMailAutoReg?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/BeataStultica/MsgsaveMailAutoReg?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/BeataStultica/MsgsaveMailAutoReg?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)

---


## 📍 Overview

This codebase is a Python script that automates the registration process on the msgsafe.io website. It uses web scraping with Selenium to navigate through the registration steps and also includes features like proxy rotation and integration with 2Captcha API for solving captchas. The core functionality is allows you to quickly create a large number of email accounts from which you can send emails that won't be considered spam.

---

## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                             |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                 |
| [email_generator.py](https://github.com/BeataStultica/MsgsaveMailAutoReg/blob/main/email_generator.py) | This code is a Python script that automates the creation of accounts on the msgsafe.io website. It uses web scraping techniques with Selenium to navigate through the website's registration process. The script also incorporates proxy rotation and 2Captcha API integration for captcha solving. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Get 2captcha api key`
> - `ℹ️ install github`
> - `ℹ️ install Python 3.8+ version`

### 📦 Installation

1. Clone the MsgsaveMailAutoReg repository:
```sh
git clone https://github.com/BeataStultica/MsgsaveMailAutoReg
```

2. Change to the project directory:
```sh
cd MsgsaveMailAutoReg
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

4. Set api key in main.py:
```sh
API_2_CAPTCHA = 'your api key'
```
### 🎮 Using MsgsaveMailAutoReg

```sh
python main.py
```


## 🗺 Roadmap

> - [ ] `ℹ️  train own neural network to solve captcha and replace 2captcha with it`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---



