# 🧠 Python DSA Projects

Two Python projects that apply core data structures to real-world problems:

| # | Project | Data Structure | Interface |
|---|---------|----------------|-----------|
| 1 | [Restaurant Booking System](#1--restaurant-booking-system) | Queue (FIFO) | tkinter GUI |
| 2 | [Smart Music Player](#2--smart-music-player) | Doubly Linked List | Console + Streamlit web |

---

## 1. 🍽️ Restaurant Booking System

A simple restaurant booking system built with **Python** and **tkinter**. It manages customer reservations using a **queue** and shows how basic queue operations apply to a real-world problem.

### Features
- Add bookings with customer name, booking time and party size
- Process bookings in **first-come, first-served** order
- Display the current list of bookings in the queue
- Interactive time selection with dropdown menus for hours and minutes

### Data Structure Used
| Operation | Purpose |
|-----------|---------|
| **Enqueue** | Add a new booking to the end of the queue |
| **Dequeue** | Process the booking at the front of the queue |
| **Display** | View all bookings currently waiting |

A queue is the natural fit because the customer who booked first should be served first.

### Run
tkinter ships with Python, so no extra installation is needed.
```bash
python restaurant_booking.py
```
> Replace `restaurant_booking.py` with your file name.

### How to Use
1. Enter the customer name and party size.
2. Choose the booking hour and minute from the dropdowns.
3. Click **Add Booking** to enqueue it.
4. Click **Process Booking** to serve the next customer in line.

---

## 2. 🎧 Smart Music Player

A music player that searches songs on YouTube with **yt-dlp** and manages playlists using a **doubly linked list**. It includes a console version and Streamlit web versions.

### Features
- Add songs to a playlist and view the playlist
- Search for any song online and play it
- Play the current song, move to the **next** or **previous** song
- **Shuffle** the playlist
- Like songs and view **favorites**
- View **recently played** songs
- **Loop mode** to return to the start when the playlist ends

### Data Structure Used (`musicapp.py`)
- **Doubly linked list:** each `Song` node has `prev` and `next` pointers
- **Insertion at the tail** to add songs
- **Traversal** to display the playlist
- **O(1) next/previous navigation** using the pointers
- **Loop mode** that jumps from the last node back to the head
- **Shuffle** using a list and `random.shuffle`


## Sample Output

```
Enter your username: Pravalika

Welcome to Smart Spotify, Pravalika 🎧

========== MENU ==========
1 Add Song to Playlist
2 Show Playlist
3 Play Current Song
4 Next Song
5 Previous Song
6 Search and Play Song Online
7 Shuffle Playlist
8 Like Current Song
9 Show Favorite Songs
10 Recently Played
11 Toggle Loop Mode
0 Exit

Enter choice: 1
Enter song name: Believer
🎵 Song added to playlist: Believer
```

### Install and Run
```bash
pip install streamlit yt-dlp
```
Console version:
```bash
python musicapp.py
```
Web version (opens at `http://localhost:8501`):
```bash
streamlit run Musicc.py
```
If `streamlit` is not recognized, use `python -m streamlit run Musicc.py`.

### Notes
- An internet connection is required for song search.
- If songs stop loading, update the library: `pip install -U yt-dlp`.

---

## 🛠️ Tech Stack
Python 3 · tkinter · Streamlit · yt-dlp

## 📚 What I Learned
- Implementing and applying a **queue** (enqueue, dequeue) and a **doubly linked list**
- Building a GUI with tkinter and quick web apps with Streamlit
- Fetching online data with yt-dlp
- Modelling real-world workflows with data structures

## 🚀 Possible Improvements
- Restaurant: save bookings to a file or database, validate inputs, add cancel booking and table assignment
- Music player: add a tail pointer for O(1) insertion, delete and search songs, save playlists between sessions

## 👤 Author
**Muthoju Pravalika**
