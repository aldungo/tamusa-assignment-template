# 📚 GitHub Classroom Setup Guide - Step by Step

This guide walks you through creating a GitHub Classroom assignment with autograding, ensuring students can't see the grading logic.

## 🎯 **Understanding the Setup**

### **Template Repository** (What You Create)
- Contains **autograding infrastructure** (hidden from students)
- Has **clean student files** only
- Students get a **copy** without seeing the grading logic

### **Student Repositories** (What Students Get)
- Only the files they need to complete the assignment
- Autograding happens **behind the scenes**
- No access to grading scripts or answer keys

## 📋 **Step-by-Step Setup Process**

### **Phase 1: Prepare Your Template Repository**

1. **Run the template setup script**:
   ```bash
   python setup_template.py
   ```
   
   This will:
   - ✅ Move instructor files to `instructor_files/` folder
   - ✅ Create clean student-facing files
   - ✅ Set up proper `.gitignore`
   - ✅ Prepare the repository for GitHub Classroom

2. **Commit the template structure**:
   ```bash
   git add .
   git commit -m "Set up GitHub Classroom template"
   git push origin main
   ```

### **Phase 2: Create GitHub Classroom Assignment**

1. **Go to GitHub Classroom**:
   - Visit [classroom.github.com](https://classroom.github.com)
   - Sign in with your GitHub account

2. **Create New Assignment**:
   - Click "New Assignment"
   - Assignment name: `CSCI 1436 Assignment #1`
   - Assignment type: **Individual Assignment**

3. **Configure Repository Template**:
   - ✅ Check "Add a template repository to give students starter code"
   - Select your template repository: `your-username/tamusa-assignment-test`
   - Repository visibility: **Private** (recommended)

4. **Enable Autograding**:
   - ✅ Check "Enable autograding"
   - Select **"Use existing workflow"**
   - The system will detect `.github/workflows/classroom.yml`

5. **Configure Autograding Tests**:
   
   GitHub Classroom will show you 6 tests from your workflow file:
   
   | Test Name | Command | Points | Timeout |
   |-----------|---------|--------|---------|
   | Question 1 - Definitions | `python autograder.py q1_definitions` | 40 | 10s |
   | Question 2 - High Level Languages | `python autograder.py q2_high_level` | 12 | 10s |
   | Question 3 - Variable Declarations | `python autograder.py q3_declarations` | 12 | 10s |
   | Question 4 - Modulo Operations | `python autograder.py q4_modulo` | 12 | 10s |
   | Question 5 - Sphere Volume Program | `python autograder.py q5_sphere_volume` | 12 | 10s |
   | Question 6 - Debugging | `python autograder.py q6_debugging` | 12 | 10s |
   
   ✅ **Accept all these tests** - they're pre-configured correctly!

6. **Assignment Settings**:
   - Deadline: Set your assignment deadline
   - ✅ Enable feedback pull requests (optional but helpful)
   - ✅ Enable autograding (already done above)

7. **Create Assignment**:
   - Click "Create Assignment"
   - 🎉 You'll get an assignment invitation URL!

### **Phase 3: What Students Will See**

When students click your assignment URL:

1. **They get a clean repository with only**:
   ```
   ├── student_submission.py     # Their assignment script
   ├── README.md                 # Student instructions
   ├── requirements.txt          # Python packages they need
   └── .github/workflows/        # Hidden autograding (they can see but not modify)
   ```

2. **They CANNOT see**:
   - `autograder.py` (your grading logic)
   - `instructor_dashboard.py` (your dashboard)
   - Answer keys or solutions
   - Grading rubrics

3. **Their workflow**:
   ```bash
   # 1. Clone their repository
   git clone https://github.com/your-org/assignment-STUDENTNAME
   
   # 2. Complete the assignment
   python student_submission.py
   
   # 3. Submit their work
   git add .
   git commit -m "Complete Assignment #1"
   git push origin main
   
   # 4. Autograding runs automatically!
   ```

### **Phase 4: How Autograding Works**

1. **When students push code**:
   - GitHub Actions triggers automatically
   - Runs your `autograder.py` script (from template, not visible to students)
   - Tests each question independently
   - Reports scores back to GitHub Classroom

2. **Grading Process**:
   ```
   Student pushes → GitHub Actions → Autograder runs → Scores recorded → Student sees results
   ```

3. **Students see their results in**:
   - GitHub Actions tab (pass/fail for each test)
   - GitHub Classroom grade report
   - Pull request feedback (if enabled)

## 🔧 **Advanced Configuration**

### **Hiding the Autograder Completely**

If you want to hide the autograder from students entirely:

1. **Create a separate "solutions" repository**:
   ```bash
   # Create new private repository: csci1436-assignment1-autograder
   # Move autograder.py there
   # Reference it in GitHub Actions via external action
   ```

2. **Use GitHub Actions Secrets**:
   ```yaml
   # In .github/workflows/classroom.yml
   - name: Download Autograder
     run: |
       curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            https://api.github.com/repos/your-org/autograder-repo/contents/autograder.py \
            | jq -r .content | base64 -d > autograder.py
   ```

### **Custom Test Names and Feedback**

You can customize what students see:

```yaml
# In classroom.yml - change test names to be more student-friendly
- name: "Programming Concepts Quiz"
  command: python autograder.py q1_definitions
  
- name: "Language Comparison"  
  command: python autograder.py q2_high_level
```

## 🎓 **For Your Fall 2025 Semester**

### **Recommended Workflow**:

1. **Before Semester**:
   - Set up template repository (done! ✅)
   - Create GitHub Classroom assignment
   - Test with a dummy student account

2. **Assignment Release**:
   - Share GitHub Classroom assignment URL
   - Share Turnitin assignment separately
   - Provide setup instructions

3. **During Assignment**:
   - Students work and submit via GitHub
   - Monitor GitHub Classroom dashboard for submissions
   - Auto-grading provides immediate feedback

4. **After Deadline**:
   - Run `python instructor_dashboard.py` to view all results
   - Cross-reference with Turnitin submissions
   - Export final grades to your LMS

## 🐛 **Troubleshooting Common Issues**

### **"Autograding Failed" in GitHub Classroom**:
- Check that `autograder.py` is in the template repository
- Verify JSON submission file format matches expectations
- Look at GitHub Actions logs for specific errors

### **Students Can't Run the Script**:
- Ensure `requirements.txt` has `python-docx`
- Provide Python installation instructions
- Test the student script yourself

### **Grading Logic Issues**:
- Test your autograder with sample submissions
- Use `python autograder.py q1_definitions` locally to debug
- Check regex patterns and keyword matching

---

## 🚀 **Ready to Deploy?**

1. Run `python setup_template.py` to prepare your repository
2. Follow the GitHub Classroom setup steps above
3. Test with a student account
4. Deploy to your class!

Your students will have a seamless experience while you get powerful autograding! 🎉
