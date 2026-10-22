class SongNode:
    def __init__(self, song_id, song_name, artist, duration):
        self.song_id = song_id
        self.song_name = song_name
        self.artist = artist
        self.duration = duration
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self._count = 0

    def add_song(self, song_id, song_name, artist, duration):
        new_node = SongNode(song_id, song_name, artist, duration)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._count += 1
        print(f"Song added successfully: {song_name} - {artist}")

    def delete_song(self, song_id):
        current = self.head
        prev = None

        if current and current.song_id == song_id:
            self.head = current.next
            self._count -= 1
            print(f"Song with ID {song_id} deleted successfully.")
            return

        while current and current.song_id != song_id:
            prev = current
            current = current.next

        if not current:
            print(f"Song with ID {song_id} not found.")
            return

        prev.next = current.next
        self._count -= 1
        print(f"Song with ID {song_id} deleted successfully.")

    def search_song(self, song_name):
        current = self.head
        found = False
        while current:
            if current.song_name.lower() == song_name.lower():
                print(f"Found: ID: {current.song_id}, Name: {current.song_name}, Artist: {current.artist}, Duration: {current.duration}s")
                found = True
            current = current.next
        if not found:
            print(f"Song '{song_name}' not found in the playlist.")

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        
        current = self.head
        print("\n--- Current Playlist ---")
        while current:
            print(f"ID: {current.song_id} | {current.song_name} - {current.artist} ({current.duration}s) -> ", end="")
            current = current.next
        print("None\n")

    def count_songs(self):
        print(f"Total songs in playlist: {self._count}")
        return self._count

    def play_next_song(self):
        if not self.head:
            print("No songs to play. Playlist is empty.")
            return
        print(f"Now Playing: {self.head.song_name} by {self.head.artist}")
        # Növbəti mahnıya keçmək üçün başlanğıcı irəli çəkirik (istəyə görə silə də bilərik)
        self.head = self.head.next
        self._count -= 1

# --- Menyu Test Bölməsi ---
if __name__ == "__main__":
    my_playlist = Playlist()
    
    while True:
        print("\n--- Smart Music Playlist ---")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Search Song")
        print("4. Display Playlist")
        print("5. Play Next Song")
        print("6. Count Songs")
        print("7. Exit")
        
        choice = input("Seçiminizi daxil edin (1-7): ")
        
        if choice == '1':
            s_id = int(input("Song ID: "))
            s_name = input("Song Name: ")
            artist = input("Artist: ")
            duration = int(input("Duration (sec): "))
            my_playlist.add_song(s_id, s_name, artist, duration)
        elif choice == '2':
            s_id = int(input("Silmək istədiyiniz Song ID: "))
            my_playlist.delete_song(s_id)
        elif choice == '3':
            s_name = input("Axtarılan mahnının adı: ")
            my_playlist.search_song(s_name)
        elif choice == '4':
            my_playlist.display_playlist()
        elif choice == '5':
            my_playlist.play_next_song()
        elif choice == '6':
            my_playlist.count_songs()
        elif choice == '7':
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim! Yenidən cəhd edin.")