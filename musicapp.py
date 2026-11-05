import webbrowser
import random
import yt_dlp


class Song:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None


class SmartSpotify:

    def __init__(self):
        self.head = None
        self.current = None
        self.recent = []
        self.favorites = []
        self.loop = False


    def add_song(self, name):

        new_song = Song(name)

        if self.head is None:
            self.head = new_song
            self.current = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_song
            new_song.prev = temp

        print("🎵 Song added to playlist:", name)


    def show_playlist(self):

        if self.head is None:
            print("Playlist empty")
            return

        print("\n🎶 Playlist\n")

        temp = self.head
        i = 1

        while temp:
            print(i, ".", temp.name)
            temp = temp.next
            i += 1


    def search_song_online(self, song):

        print("🔍 Searching online...")

        ydl_opts = {
            'quiet': True,
            'extract_flat': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            result = ydl.extract_info(f"ytsearch:{song}", download=False)

            if 'entries' in result and len(result['entries']) > 0:

                video = result['entries'][0]

                url = "https://www.youtube.com/watch?v=" + video['id']

                print("▶ Playing:", video['title'])

                webbrowser.open(url)

            else:
                print("Song not found")


    def play_current(self):

        if self.current:
            self.search_song_online(self.current.name)
            self.recent.append(self.current.name)
        else:
            print("No song in playlist")


    def next_song(self):

        if self.current and self.current.next:
            self.current = self.current.next

        elif self.loop:
            self.current = self.head

        else:
            print("End of playlist")
            return

        self.play_current()


    def previous_song(self):

        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_current()
        else:
            print("No previous song")


    def shuffle_playlist(self):

        songs = []
        temp = self.head

        while temp:
            songs.append(temp.name)
            temp = temp.next

        random.shuffle(songs)

        print("\n🔀 Shuffled Playlist\n")

        for s in songs:
            print("•", s)


    def like_song(self):

        if self.current:
            self.favorites.append(self.current.name)
            print("❤️ Liked:", self.current.name)


    def show_favorites(self):

        print("\n❤️ Favorite Songs\n")

        for s in self.favorites:
            print("•", s)


    def recently_played(self):

        print("\n⏱ Recently Played\n")

        for s in self.recent[-5:]:
            print("•", s)


player = SmartSpotify()

username = input("Enter your username: ")
print("\nWelcome to Smart Spotify,", username, "🎧")


while True:

    print("\n========== MENU ==========")

    print("1 Add Song to Playlist")
    print("2 Show Playlist")
    print("3 Play Current Song")
    print("4 Next Song")
    print("5 Previous Song")
    print("6 Search and Play Song Online")
    print("7 Shuffle Playlist")
    print("8 Like Current Song")
    print("9 Show Favorite Songs")
    print("10 Recently Played")
    print("11 Toggle Loop Mode")
    print("0 Exit")

    choice = int(input("\nEnter choice: "))


    if choice == 1:

        name = input("Enter song name: ")
        player.add_song(name)


    elif choice == 2:

        player.show_playlist()


    elif choice == 3:

        player.play_current()


    elif choice == 4:

        player.next_song()


    elif choice == 5:

        player.previous_song()


    elif choice == 6:

        name = input("Enter song to search: ")
        player.search_song_online(name)


    elif choice == 7:

        player.shuffle_playlist()


    elif choice == 8:

        player.like_song()


    elif choice == 9:

        player.show_favorites()


    elif choice == 10:

        player.recently_played()


    elif choice == 11:

        player.loop = not player.loop
        print("🔁 Loop mode:", player.loop)


    elif choice == 0:

        print("Closing Smart Spotify")
        break