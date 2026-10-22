# Verilənlərin Strukturu və Alqoritmlər — Laboratoriya İşi № 2

Bu repozitoriya "Verilənlərin Strukturu və Alqoritmlər" fənni üzrə 2 nömrəli laboratoriya işinin həllərini ehtiva edir. Layihə heç bir hazır kitabxana (STL / collections) istifadə edilmədən, sıfırdan yazılmış xüsusi `Node` strukturları əsasında həyata keçirilmişdir.

## 📁 Repozitoriya Strukturu

Lab02/
├── src/
│   ├── playlist.py          # Tapşırıq 1: Music Playlist (Linked List)
│   ├── history_stack.py     # Tapşırıq 2: Browser History Manager (Stack)
│   └── queue_system.py      # Tapşırıq 3: Airport Check-in Queue System (Queue)
├── include/                 # Başlıq faylları (varsa)
├── screenshots/             # İşləmə görüntüləri və qrafiklər
├── report/
│   └── report.pdf           # Rəsmi laboratoriya hesabatı
├── test_results/            # Eksperiment və performans test nəticələri
├── docs/                    # Əlavə sənədləşmələr
└── README.md                # Layihənin təsvir sənədi

## 🚀 Tapşırıqlar və Xüsusiyyətlər

1. **Music Playlist (Linked List):**
   - Mahnıların əlavə edilməsi, silinməsi, axtarılması və siyahının göstərilməsi.
   - Sətrlərin idarə olunması üçün təkli əlaqəli siyahı (Singly Linked List) arxitekturası.

2. **Browser History Manager (Stack):**
   - LIFO (Last In, First Out) prinsipi ilə işləyən brauzer tarixçəsi və `Undo` (Geri al) mexanizmi.
   - Səhifələrə keçid və son əməliyyatın ləğvi.

3. **Airport Check-in Queue System (Queue):**
   - FIFO (First In, First Out) prinsipi əsasında hava limanı qeydiyyat növbəsi.
   - `front` və `rear` göstəriciləri ilə sərnişinlərin əlavə edilməsi və qeydiyyatdan keçirilməsi.

## 🛠️ Tələblər və İşə Salınma

- **Dil:** Python 3.x
- **Məhdudiyyət:** Hazır STL / kolleksiya strukturlarından istifadə qadağandır.

İstənilən skripti terminalda işə salmaq üçün:
```bash
python src/playlist.py
python src/history_stack.py
python src/queue_system.py
