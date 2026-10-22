class PassengerNode:
    def __init__(self, passenger_id, name, flight_number):
        self.passenger_id = passenger_id
        self.name = name
        self.flight_number = flight_number
        self.next = None

class AirportQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._count = 0

    def enqueue(self, passenger_id, name, flight_number):
        new_node = PassengerNode(passenger_id, name, flight_number)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._count += 1
        print(f"Sərnişin növbəyə əlavə edildi: {name} (ID: {passenger_id}, Reys: {flight_number})")

    def dequeue(self):
        if self.front is None:
            print("Növbə boşdur. Qeydiyyatdan keçəcək sərnişin yoxdur.")
            return None
        removed_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._count -= 1
        print(f"Qeydiyyatdan keçdi: {removed_node.name} (Reys: {removed_node.flight_number})")
        return removed_node

    def peek(self):
        if self.front is None:
            print("Növbə boşdur.")
            return None
        print(f"Növbədəki növbəti sərnişin -> ID: {self.front.passenger_id}, Ad: {self.front.name}, Reys: {self.front.flight_number}")
        return self.front

    def display_queue(self):
        if self.front is None:
            print("Növbə boşdur.")
            return
        current = self.front
        print("\n--- Hava Limanı Qeydiyyat Növbəsi (FRONT -> REAR) ---")
        while current:
            print(f"  [ID: {current.passenger_id}] {current.name} (Reys: {current.flight_number})", end=" -> ")
            current = current.next
        print("REAR\n")

    def count_passengers(self):
        print(f"Növbədəki ümumi sərnişin sayı: {self._count}")
        return self._count

# --- Menyu Test Bölməsi ---
if __name__ == "__main__":
    checkin_queue = AirportQueue()
    
    while True:
        print("\n--- Airport Check-in Queue System (Queue) ---")
        print("1. Sərnişin əlavə et (Enqueue)")
        print("2. Qeydiyyatdan keçir (Dequeue)")
        print("3. Növbəti sərnişinə bax (Peek)")
        print("4. Növbəni göstər")
        print("5. Sərnişinlərin sayını göstər")
        print("6. Çıxış")
        
        choice = input("Seçiminizi daxil edin (1-6): ")
        
        if choice == '1':
            p_id = int(input("Sərnişin ID: "))
            p_name = input("Sərnişinin Adı: ")
            flight = input("Reys nömrəsi (Flight Number): ")
            checkin_queue.enqueue(p_id, p_name, flight)
        elif choice == '2':
            checkin_queue.dequeue()
        elif choice == '3':
            checkin_queue.peek()
        elif choice == '4':
            checkin_queue.display_queue()
        elif choice == '5':
            checkin_queue.count_passengers()
        elif choice == '6':
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim! Yenidən cəhd edin.")
