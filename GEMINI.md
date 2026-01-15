# Term 5 Study Hub 🚀

Welcome to your Term 5 central dashboard. This file provides quick access to your courses and notes.

## 📚 Courses

### [Information and Network Security (COMP 7003)](./COMP-7003-Introduction-to-Information-and-Network-Security/inform-network-sec-7003.md)
- **Status:** Week 1 notes available.
- **Resources:** Shrunken PDFs available in `week1/lab1/`.

### [Operating Systems (COMP 7035)](./COMP-7035-Operating-Systems/)
- **Status:** Awaiting notes.

### [Database Design (COMP 7071)](./COMP-7071-Database-Design/Database.md)
- **Status:** Week 1 notes and shrunken slides available.

### [Software Engineering (COMP 7082)](./COMP-7082-Software-Engineering/SWE.md)
- **Status:** Week 1 & 2 slides shrunken and ready for review.

### [Calculus for Computing (MATH 7808)](./MATH-7808-Calculus-%20for-Computing/)
- **Notes:** [Lecture 1](./MATH-7808-Calculus-%20for-Computing/Lecture%201.md), [Lecture 2](./MATH-7808-Calculus-%20for-Computing/Lecture%202.md).

---

## 🛠️ Tools

- **Slide Shrinker (`shrink_slides.py`):** Run `python3 shrink_slides.py` to automatically convert any new `.pdf` or `.pptx` files into lightweight `.md` text files for better context management.
- **Git Sync (`git_sync.sh`):** Use this to keep your notes backed up.

---

## 📝 Recent Activity
- [x] Initialized shrunken markdown versions of all current lecture slides.
- [x] Created `GEMINI.md` dashboard.

## Added by user
- Ignore the misc.md unless needed. It just contains miscellaneous commands text etc. 
- Any `GEMINI-<class name>.md` are instructions for you, these are added by me to help you understand some of the expectations of the class, for the respective class. 
- Any `_old` dirs that are added are not mine, they're old notes from other classmates so take them with a grain of salt. Read these files first before going any deeper.
- Don't read any .docx, .pptx, etc. files to reduce context, there'll be a converted markdown of the file, if not just highlight it and continue.
- Your scope should stay within the provided class, don't read files from other classes unless specified, or ask if you think you'll need context beyond the specific class. 

## ⚙️ Environment Setup & Troubleshooting

### Database Setup (MySQL)
- **Installation:** `sudo apt install mysql-server mysql-workbench`
- **Secure Install:** `sudo mysql_secure_installation` (Enables/disables strict password plugin).
- **Create User:**
  ```sql
  sudo mysql
  CREATE USER 'markus'@'localhost' IDENTIFIED BY 'your_password';
  GRANT ALL PRIVILEGES ON *.* TO 'markus'@'localhost' WITH GRANT OPTION;
  FLUSH PRIVILEGES;
  ```
- **Neovim Connection String:** `mysql://markus:pass%40word@127.0.0.1:3306/db_name`
  - **Note:** `%40` encodes the `@` symbol in passwords.

### Neovim + Dadbod UI
- **Leader Key:** Set to Space (`vim.g.mapleader = " "`) in `init.lua`.
- **Key Mappings:**
  - `<Leader>s` to run query (Shift+S is default).
  - Map in `lua/mappings.lua`: `map("n", "<leader>s", "<cmd>DBUIExecuteQuery<CR>")`
- **Troubleshooting:** If `:echo mapleader` returns nothing, check `vim.g.mapleader` is set **before** plugins load.

### Shell (Fish)
- **Config Path:** `~/.config/fish/config.fish`
- **Add Path:** `fish_add_path /opt/nvim-linux-x86_64/bin`
- **Aliases:**
  ```fish
  alias v='nvim'
  alias vi='nvim'
  ```
- **Reload:** `source ~/.config/fish/config.fish`
