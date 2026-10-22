import time

class ActionNode:
    def __init__(self, action_id, action_name):
        self.action_id = action_id
        self.action_name = action_name
        self.timestamp = time.strftime("%H:%M:%S")
        self.next = None

class UndoStack:
    def __init__(self):
        self.top = None
        self._count = 0

    def push_action(self, action_id, action_name):
        new_node = ActionNode(action_id, action_name)
        new_node.next = self.top
        self.top = new_node
        self._count += 1
        print(f"Əməliyyat yerinə yetirildi: '{action_name}' (ID: {action_id}) - Vaxt: {new_node.timestamp}")

    def undo_action(self):
        if not self.top:
            print("Ləğv ediləcək tarixçə yoxdur. Stack boşdur.")
            return
        removed_node = self.top
        self.top = self.top.next
        self._count -= 1
        print(f"Geri alqoritmi (Undo): '{removed_node.action_name}' (ID: {removed_node.action_id}) tarixçədən silindi.")

    def current_action(self):
        if not self.top:
            print("Aktiv səhifə və ya əməliyyat yoxdur. Stack boşdur.")
            return
        print(f"Cari Səhifə/Əməliyyat -> ID: {self.top.action_id}, Adı: {self.top.action_name}, Vaxt: {self.top.timestamp}")

    def display_history(self):
        if not self.top:
            print("Tarixçə stack-i boşdur.")
            return
        current = self.top
        print("\n--- Brauzer Tarixçəsi (Üstdən Aşağı - TOP to BOTTOM) ---")
        while current:
            print(f"  [ID: {current.action_id}] {current.action_name} ({current.timestamp})")
            current = current.next
        print("-----------------------------------------------------")

    def count_actions(self):
        print(f"Tarixçədəki ümumi əməliyyat sayı: {self._count}")
        return self._count

# --- Menyu Test Bölməsi ---
if __name__ == "__main__":
    history = UndoStack()
    
    while True:
        print("\n--- Brauzer Tarixçəsi Meneceri (Stack) ---")
        print("1. Səhifəyə daxil ol / Əməliyyat yerinə yetir")
        print("2. Geri qayıt / Əməliyyatı ləğv et (Undo)")
        print("3. Cari səhifəni/əməliyyatı göstər")
        print("4. Tam tarixçəni göstər")
        print("5. Əməliyyatların sayını göstər")
        print("6. Çıxış")
        
        choice = input("Seçiminizi daxil edin (1-6): ")
        
        if choice == '1':
            a_id = int(input("Əməliyyat ID: "))
            a_name = input("Əməliyyat və ya Səhifə Adı (URL / təsvir): ")
            history.push_action(a_id, a_name)
        elif choice == '2':
            history.undo_action()
        elif choice == '3':
            history.current_action()
        elif choice == '4':
            history.display_history()
        elif choice == '5':
            history.count_actions()
        elif choice == '6':
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim! Yenidən cəhd edin.")
