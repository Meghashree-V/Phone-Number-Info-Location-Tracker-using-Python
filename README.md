#  Phone Number Info & Location Tracker using Python

A simple Python project that takes a phone number and returns details like **carrier**, **region/state**, **timezone**, and its **approximate location on a map** using APIs and geolocation libraries.

---

## 🔧 Features

- ✅ Detects **country and state/region**
- ✅ Shows **carrier/network provider**
- ✅ Displays **timezone**
- ✅ Retrieves **latitude & longitude**
- ✅ Renders location on an **interactive map (HTML)**

---

## 🗺️ Output

After running the script:

- You'll see details printed in the terminal
- An HTML map will be saved as:

  ```bash
  mylocation.html
  ```

  Open it in your browser to view the location.

### 🔍 Preview

![Output Screenshot](https://github.com/user-attachments/assets/025612ed-e521-4ce7-8f8e-563d52fe77cb)

---

## 🧠 How It Works

1. **Reads phone number** from `myphone.py`
2. Uses `phonenumbers` to parse and get:
   - Region
   - Carrier
   - Timezone
3. Uses **OpenCage API** to convert region → coordinates
4. Generates a map using `folium` and saves it as HTML

---

## 🧪 Example

If `myphone.py` has:

```python
number = "+919876543210"
```

Running `main.py` will show:

```
Region     : Karnataka, India
Carrier    : Airtel
Time Zones : Asia/Kolkata
Latitude   : 12.9716
Longitude  : 77.5946
```

A map will also open (or be saved as `mylocation.html`).

---

## 🔑 OpenCage API Setup

1. Go to [https://opencagedata.com](https://opencagedata.com)
2. Sign up and get a **free API key**
3. Replace the `key` in `main.py`:

   ```python
   key = 'YOUR_API_KEY'
   ```

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install phonenumbers folium opencage
```

---

## 🚀 Running the Project

```bash
python main.py
```

Output will appear in the terminal, and the map will be saved as `mylocation.html`.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork this repo and enhance the functionality.

---

