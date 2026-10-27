# 🌦️ Real-Time Weather & Air Quality Index (AQI) Dashboard

An end-to-end full-stack web application built with **Python (Flask)** and **Bootstrap 5** that delivers live weather metrics and Air Quality Index (AQI) analysis using the **OpenWeatherMap REST API**.

---

## 📌 Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Directory Structure](#project-directory-structure)
- [How It Works (Data Flow)](#how-it-works-data-flow)
- [API Endpoints Used](#api-endpoints-used)
- [Installation & Local Setup](#installation--local-setup)
- [Environment Configuration](#environment-configuration)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 📖 Overview

The **Weather & AQI Dashboard** allows users to monitor atmospheric conditions and environmental health metrics for any location globally. The application fetches live data from OpenWeatherMap, parses key indicators such as particulate matter ($PM_{2.5}$, $PM_{10}$), temperature, humidity, and atmospheric pressure, and presents them through an interactive, responsive dashboard.

---

## 🏗️ System Architecture

1. **Client Layer:** User enters a city name or triggers browser geolocation via JavaScript.
2. **Server Layer:** Flask receives the request, loads environment variables securely via `python-dotenv`, and queries OpenWeatherMap REST endpoints.
3. **Data Processing:** The backend processes JSON payloads, maps AQI index values to descriptive health advisory levels, and renders the data dynamically using Jinja2 templates.
4. **Presentation Layer:** Responsive layout powered by Bootstrap 5 with dynamic CSS styling based on weather conditions.

---

## ✨ Key Features

- **Real-Time Weather Metrics:** Current temperature, perceived temperature ("feels like"), humidity levels, wind velocity, and atmospheric pressure.
- **Comprehensive AQI Breakdown:** Numerical AQI classification (Good, Fair, Moderate, Poor, Very Poor) along with specific pollutant levels ($PM_{2.5}$, $PM_{10}$, $NO_2$, $SO_2$, $CO$, $O_3$).
- **Browser Geolocation:** One-click location detection using HTML5 Geolocation API.
- **City Search with Validation:** Real-time error handling for invalid city names or network issues.
- **Secure Key Storage:** Keeps sensitive API keys hidden from source code using `.env`.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python 3.x, Flask | Routing, API handling, server-side template rendering |
| **Frontend** | HTML5, CSS3, JavaScript | DOM manipulation, Geolocation API, responsive layouts |
| **UI Framework** | Bootstrap 5 | Mobile-first grid system and UI components |
| **Template Engine** | Jinja2 | Dynamic HTML data binding |
| **Data Source** | OpenWeatherMap API | Live weather and air pollution endpoints |
| **Environment** | python-dotenv | Secure secret and credential management |

---

## 📂 Project Directory Structure

```text
weather-aqi-dashboard/
│
├── app.py                  # Core application entry point and route definitions
├── requirements.txt        # Python package dependencies
├── .env.example            # Environment variable template (safe to commit)
├── .gitignore              # Files and folders ignored by Git (.env, venv/)
├── README.md               # Complete project documentation
│
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles, responsive tweaks, animations
│   └── js/
│       └── main.js         # Geolocation handling and UI interactions
│
└── templates/
    ├── base.html           # Reusable layout and navigation shell
    └── index.html          # Main weather and AQI display view
