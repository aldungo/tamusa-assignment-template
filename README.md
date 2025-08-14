# CSCI 1436 Assignment #1 - Simple Auto-Grading System

This repository contains a **simplified** assignment submission and auto-grading system for CSCI 1436 Programming Fundamentals I.

## 🎯 **Simple System Overview**

**What it does:**
1. **Students**: Answer questions → Get JSON auto-graded → Upload Word doc to Blackboard
2. **Instructor**: View percentage scores → Export grades → Done!

**What it doesn't do:**
- ❌ Manual Word doc review (Turnitin handles plagiarism automatically)
- ❌ Complex instructor dashboards
- ❌ Complicated setup processes

## 📁 **Simple File Structure**

```
├── simple_submission.py       # Student script (clean & simple)
├── simple_autograder.py       # Autograding logic (percentage-based)
├── simple_dashboard.py        # Basic instructor grade viewer
├── .github/workflows/
│   └── classroom.yml          # GitHub Actions autograding
└── README.md                  # This file
```

## 🚀 **Quick Setup**

### **For Students:**
1. Accept GitHub Classroom assignment link
2. Run: `python simple_submission.py`
3. Push to GitHub (auto-graded immediately!)
4. Upload Word doc to Blackboard (submission proof)

### **For Instructor:**
1. Create GitHub Classroom assignment with this as template
2. Enable autograding (pre-configured!)
3. Students submit → You see percentage scores
4. Run `python simple_dashboard.py` to export grades

## 🎓 **Student Experience**

```bash
# 1. Complete assignment
python simple_submission.py
# Answers questions interactively
# Creates: assignment1_FirstName_LastName.json (autograded)
# Creates: Assignment1_FirstName_LastName.docx (Blackboard proof)
# Auto-saves work to Git (local backup)

# 2. Submit to GitHub (CRITICAL!)
git push
# ⚠️ WARNING: Work can be lost if students skip this step!

# 3. See instant results in GitHub Actions tab!
# Results show: Q1: 32/40 (80%), Q2: 10/12 (83%), etc.

# 4. Upload Word doc to Blackboard (just proof of submission)
```

## 🛡️ **Critical: Preventing Student Work Loss**

**The Risk**: Students can lose ALL work if they close Codespace without pushing!

**Safeguards Added**:
- ✅ **Auto-commit**: Script automatically saves work to Git (local backup)
- ✅ **Clear warnings**: Multiple reminders to push before closing
- ✅ **Auto-save files**: VS Code saves files every 1 second  
- ✅ **Prominent instructions**: Student README emphasizes `git push`

**Student Safety Workflow**:
1. Run `python simple_submission.py` → Auto-saves locally ✅
2. **MUST run `git push`** → Submits for grading ✅  
3. Safe to close Codespace ✅

**If student forgets to push**: Work may be lost when Codespace times out!

## 📊 **Auto-Grading Details**

Each question gets a **percentage score**:

- **Q1 (40 pts)**: Programming term definitions
- **Q2 (12 pts)**: High-level vs low-level languages  
- **Q3 (12 pts)**: Java variable declarations
- **Q4 (12 pts)**: Modulo operation calculations
- **Q5 (12 pts)**: Sphere volume program logic
- **Q6 (12 pts)**: Code debugging skills

**Students see**: `Score: 85/100 (85%)` in GitHub Actions

## 🎯 **Your Fall 2025 Workflow**

### **Setup (Once):**
1. Create GitHub Classroom assignment using this repo as template
2. Set up parallel Blackboard assignment for Word doc submission
3. Configure Turnitin for automatic plagiarism detection

### **During Assignment:**
1. Students submit via GitHub → **Auto-graded instantly**
2. Students upload Word docs to Blackboard → **Turnitin scans automatically**
3. You monitor GitHub Classroom dashboard for completion

### **After Deadline:**
```bash
# View all grades and export
python simple_dashboard.py
# Exports: csci1436_assignment1_grades_TIMESTAMP.csv
# Import to your LMS gradebook
```

## 💡 **Why This Is Better**

### **For Students:**
- ✅ **Instant feedback** (see scores immediately)
- ✅ **Clear percentage scores** (no guessing)
- ✅ **Simple process** (one script, two submissions)

### **For You:**
- ✅ **Zero manual grading** (JSON is auto-graded)
- ✅ **No Word doc review needed** (Turnitin handles plagiarism)
- ✅ **Quick grade export** (CSV ready for LMS import)
- ✅ **Scalable** (works for 20 or 200 students)

## 🔧 **GitHub Classroom Tests**

When you create the assignment, GitHub Classroom will show these 6 tests:

| Test Name | Command | Points |
|-----------|---------|--------|
| Question 1 - Programming Definitions | `python simple_autograder.py q1_definitions` | 40 |
| Question 2 - Programming Languages | `python simple_autograder.py q2_languages` | 12 |
| Question 3 - Variable Declarations | `python simple_autograder.py q3_declarations` | 12 |
| Question 4 - Mathematical Operations | `python simple_autograder.py q4_modulo` | 12 |
| Question 5 - Programming Logic | `python simple_autograder.py q5_programming` | 12 |
| Question 6 - Code Debugging | `python simple_autograder.py q6_debugging` | 12 |

**✅ Accept all these tests** - they're pre-configured!

## 🔒 **Academic Integrity**

- **JSON autograding** = consistent scoring
- **GitHub commit history** = submission timeline proof
- **Turnitin Word docs** = plagiarism detection
- **Immediate scoring** = reduces grade disputes

---

## ❓ **"Do I Need to Run Setup Scripts First?"**

### **NO! This is ready immediately:**

✅ **When you create the GitHub Classroom assignment using this repo as template:**
- Students get working code instantly
- Autograding is pre-configured  
- GitHub Codespaces launches in 30 seconds
- No instructor setup required

✅ **Students immediately can:**
- Open assignment in Codespaces (zero setup)
- Run `python simple_submission.py` 
- Get auto-graded results
- See percentage scores

✅ **You immediately get:**
- Autograding dashboard in GitHub Classroom
- Percentage scores for each student
- CSV export capabilities

### **The Magic:**
- `.devcontainer/devcontainer.json` → Codespaces auto-setup
- `.github/workflows/classroom.yml` → Pre-configured autograding  
- `simple_autograder.py` → Hidden from students but runs automatically
- `requirements.txt` → Auto-installs dependencies

**Result: Students click "Create codespace" → 30 seconds later they're coding!**

---

## 📚 **Step-by-Step GitHub Classroom Setup**

### **Phase 1: Use This Repository (No Setup Required!)**

1. **This repository is READY to use as a GitHub Classroom template**:
   - ✅ All autograding is pre-configured
   - ✅ GitHub Codespaces support included
   - ✅ Students get instant setup (zero configuration)
   - ✅ No instructor setup scripts to run

2. **What students get immediately**:
   ```
   student-repo/
   ├── simple_submission.py      # Ready to run assignment script
   ├── requirements.txt          # python-docx dependency  
   ├── README.md                 # Student instructions with Codespaces guide
   ├── .devcontainer/            # Codespaces auto-configuration
   │   └── devcontainer.json
   └── .github/workflows/        # Pre-configured autograding
       └── classroom.yml
   ```

3. **Test locally (optional)**:
   ```bash
   # Test the student experience
   python simple_submission.py
   
   # Test the autograder  
   python simple_autograder.py all
   ```

### **Phase 2: Create GitHub Classroom Assignment**

1. **Go to GitHub Classroom**:
   - Visit [classroom.github.com](https://classroom.github.com)
   - Sign in with your GitHub account

2. **Create New Assignment**:
   - Click **"New Assignment"**
   - Assignment name: **"CSCI 1436 Assignment #1"**
   - Assignment type: **Individual Assignment**

3. **Add Template Repository**:
   - ✅ Check **"Add a template repository to give students starter code"**
   - Select: **"aldungo/tamusa-assignment-test"** (or your forked version)
   - Repository visibility: **Private** (recommended)

4. **Enable Autograding**:
   - ✅ Check **"Enable autograding"**
   - Click **"Add test"** or **"Import from template"**
   - GitHub will detect the existing `.github/workflows/classroom.yml`
   - You should see 6 tests automatically imported

5. **Verify the Autograding Tests**:
   
   GitHub Classroom should show these tests:
   
   | Test Name | Command | Points | Timeout |
   |-----------|---------|---------|---------|
   | Question 1 - Programming Definitions | `python simple_autograder.py q1_definitions` | 40 | 10s |
   | Question 2 - Programming Languages | `python simple_autograder.py q2_languages` | 12 | 10s |
   | Question 3 - Variable Declarations | `python simple_autograder.py q3_declarations` | 12 | 10s |
   | Question 4 - Mathematical Operations | `python simple_autograder.py q4_modulo` | 12 | 10s |
   | Question 5 - Programming Logic | `python simple_autograder.py q5_programming` | 12 | 10s |
   | Question 6 - Code Debugging | `python simple_autograder.py q6_debugging` | 12 | 10s |
   
   ✅ **Accept all these tests** - they're already configured correctly!

6. **Assignment Settings**:
   - **Deadline**: Set your assignment deadline
   - **Admin access**: Choose if TAs can access
   - **Feedback**: ✅ Enable feedback pull requests (optional)

7. **Create Assignment**:
   - Click **"Create Assignment"**
   - 🎉 **You'll get an assignment invitation URL to share with students!**

### **Phase 3: What Students Will See**

When students click your assignment URL, they get a **clean repository** with only:

```
student-repo/
├── simple_submission.py      # Their assignment script
├── requirements.txt          # Just: python-docx==0.8.11
├── README.md                 # Student instructions only
└── .github/workflows/        # Autograding (they can see but not modify)
    └── classroom.yml
```

**Students will NOT see**:
- `simple_autograder.py` (your grading logic)
- `simple_dashboard.py` (your grade viewer)
- Any answer keys or grading rubrics

### **Phase 4: Student Workflow (Zero Setup!)**

**Students click assignment link → Immediate access:**

1. **GitHub Codespaces (Recommended)**:
   - Click green **"<> Code"** button → **"Codespaces"** → **"Create codespace"**
   - Wait 30 seconds (Python + dependencies auto-installed)
   - Run: `python simple_submission.py`
   - Commit & push → Auto-graded instantly!

2. **Or Local Development**:
   - Clone repo → `pip install -r requirements.txt` → Run script

3. **Results**: See percentage scores in GitHub Actions tab immediately

### **Phase 5: Your Instructor Workflow**

1. **Monitor submissions** via GitHub Classroom dashboard
2. **View detailed grades** (if needed):
   ```bash
   # Clone a student's repo to see their submission
   git clone https://github.com/your-org/assignment-STUDENT-NAME
   cd assignment-STUDENT-NAME
   
   # Run your dashboard on their submission
   python simple_autograder.py all
   ```
3. **Export final grades** using GitHub Classroom's built-in export

---

## 🎯 **Key Benefits of This Setup**

✅ **Students see**: Clean assignment, instant feedback, clear instructions  
✅ **You manage**: All grading logic stays hidden, automatic scoring, easy grade export  
✅ **Secure**: Students can't see or modify grading criteria  
✅ **Scalable**: Works for any class size  
✅ **Simple**: No complex setup or maintenance required  

**Bottom Line:** Students get instant feedback, you get automatic grading, Turnitin handles plagiarism. Simple and effective! 🎉
