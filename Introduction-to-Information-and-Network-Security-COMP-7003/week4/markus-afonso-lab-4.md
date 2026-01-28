# Lab 4: Passwords and Logins

## Step 1: Create a lab user and set a password
**Create the user:**
- Command used: 
```
❯ sudo useradd -m labuser
[sudo] password for markus: 
```

**Set the password:**
- Command used: 
```
❯ sudo passwd labuser
New password: 
Retype new password: 
passwd: password updated successfully
```

**Verify account existence:**
- `getent passwd labuser` output: 
```
❯ getent passwd labuser
labuser:x:1001:1001::/home/labuser:/bin/sh
```
---

## Step 2: Observe /etc/passwd and /etc/shadow
**Deliverable 1:**
- The `labuser` line from `/etc/passwd`: 
```
❯ grep '^labuser:' /etc/passwd
labuser:x:1001:1001::/home/labuser:/bin/sh
```
**Deliverable 2:**
- The `labuser` line from `/etc/shadow` (Redacted):
  - Format: `username:$id$salt$...` (Keep the ID and Salt, replace the rest of the hash with `...`)
  - Line: 
```
❯ sudo grep '^labuser:' /etc/shadow
labuser:$y$j9T$nUetyViZWM42bei0l3jtO/$iyLznu6lMPKOq9isz1ZQQPD8OyU.bDGDD1uVJ7iXtn3:20480:0:99999:7:::
```
> After switching to `SHA512`
```
❯ sudo grep '^labuser:' /etc/shadow
labuser:$6$5AnXfOatz9PMlE/b$vUkU.RTDABLSKjlN3eLS0qrkaaA5wJTZFcp1cQmHzKlBctVPvXACAxV99Chs2GPi0.K3uCFRkZcOoBAxJPMMQ0:20480:0:99999:7:::
```
**Identify the hash scheme:**
- Hash scheme ID found : `$y$`, After switching `$6$`

---

## Step 3: Extract the hash for cracking
**Deliverable 3:**
 Contents of `hash.txt` (Paste the single line here): 
```
❯ cat hash.txt
$y$j9T$nUeFtyViZWM42bei0l3jtO/$iyLznu6lMPKOq9isz1ZQQPD8OyU.bDGDD1uVJ7iXtn3
```

```
❯ cat hash.txt 
$6$5AnXfOatz9PMlE/b$vUkU.RTDABLSKjlN3eLS0qrkaaA5wJTZFcp1cQmHzKlBctVPvXACAxV99Chs2GPi0.K3uCFRkZcOoBAxJPMMQ0
```
---

## Step 4: Dictionary cracking with Hashcat
**Setup:**
- Wordlist used: `https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/Pwdb_top-10000000.txt`
- Hashcat mode selected: 
	- Couldn't find a hashcat mode since the password is hashed using `yescrypt` which hashcat doesn't support.
		- Correction, seems like there is support but set up is quite in depth, beyond what I think is reasonable for this lab, some more info [here](https://github.com/hashcat/hashcat/blob/master/docs/hashcat-python-plugin-quickstart.md)
	- Had to go back and change the hash type for the password
	- Looks like it should be 1800, so going with that
```
❯ hashcat -h | grep "SHA512"
   ...
   7100 | macOS v10.8+ (PBKDF2-SHA512)    | Operating System
   1800 | sha512crypt $6$, SHA512 (Unix)  | Operating System
```
- Full command line used: 
- 

**Results:**:
- Did it crack? 
- Password recovered? 

**Deliverable 4 (Short Paragraph):**
- What does this demonstrate about common-password risk?
- What does it demonstrate about choosing passwords that humans can reproduce?
- **Answer:** 

---

## Step 5: Brute-force mask demo
**Constraints:**
- Search space: Digits only, length 4-6.

**Command used:**
- 

**Deliverable 5 (One Sentence):**
- Compare dictionary cracking vs. brute force.
- **Answer:** 

---

## Step 6: Cleanup
**Lock and Remove Account:**
- Commands used: 

**Deliverable 6 (Evidence):**
- Run `getent passwd labuser`.
- Output (should be empty): 

---

## Submission Checklist
- [ ] /etc/passwd line included?
- [ ] /etc/shadow line redacted correctly?
- [ ] hash.txt content included?
- [ ] Dictionary cracking reflection written?
- [ ] Brute-force comparison sentence written?
- [ ] Cleanup verified?
