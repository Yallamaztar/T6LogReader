# **T6LogReader 📜**

#### A Python module for reading and searching Black Ops II (Plutonium T6) logs


## 🚀 Features
- **✅ Read the last lines of console.log** 
- **✅ Search for specific commands (e.g., kick, ban, custom commands)**
- **✅ Count the occurrences of a command or keyword**
- **✅ Clear the log file for a fresh start**
- **✅ Works dynamically for any Windows user (not tested on Linux)**
- **✅ Supports custom log file paths**
- **✅ Efficient error handling for robustness**
---

## 📥 Installation

```
pip install T6LogReader
```

---

## 🛠 Usage

### Read Last `number_of_lines: int` Lines
This function allows you to read the last n lines from the log
```python
from t6logreader import T6LogReader

log_reader = T6LogReader()
print(log_reader.read_last_lines(number_of_lines=10))
```

----

### Search for a Specific `command: str`
Searches for commands like "kick", "ban", etc. You can customize the prefix
```python
from t6logreader import T6LogReader

log_reader = T6LogReader()
print(log_reader.search_command(command="kick", prefix="")) # Prefix is normally set as "]" 
```

----

### Read the Last Line
Reads the most recent line from the log file
```python
from t6logreader import T6LogReader

log_reader = T6LogReader()
print(log_reader.read_last_line()) 
```

---

### Clear the Log File
```python
from t6logreader import T6LogReader

log_reader = T6LogReader()
log_reader.clear_log()
```

---

### Count occurrences of a `keyword: str` | `prefix: str`
Counts how many times a keyword (e.g., "kick") appears in the log.
```python
from t6logreader import T6LogReader

log_reader = T6LogReader()
print(log_reader.count_occurences(keyword="kick", prefix="]"))
```

---

## 📂 File Path Handling

#### By default, it reads:
```
C:\Users\YourUser\AppData\Local\Plutonium\console.log
```

#### But you can specify a custom path:
```python
log_reader = T6LogReader(log_path="custom/path/to/console.log")
```

---

# Come Play on Brownies SND (T6) 🍰
### Why Brownies? 🤔
- **Stability:** Brownies delivers a consistent, lag-free experience, making it the perfect choice for players who demand uninterrupted action
- **Community:** The players at Brownies are known for being helpful, competitive, and fun—something Orion can only dream of
- **Events & Features:** Brownies is constantly running unique events and offers more server-side customization options than Orion, ensuring every game feels fresh

---

#### [Brownies Discord](https://discord.gg/FAHB3mwrVF) | [Brownies IW4M](http://152.53.132.41:1624/) | Made With ❤️ By Budiworld