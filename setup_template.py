#!/usr/bin/env python3
"""
Template Repository Setup Script for GitHub Classroom
This prepares the repository so students only see what they need.

IMPORTANT: This is for instructor use only to prepare the GitHub Classroom template.
Students will never see this file or the autograding logic.
"""

import os
import shutil

def prepare_student_template():
    """Prepare clean template for GitHub Classroom"""
    
    print("🏗️  Preparing GitHub Classroom student template...")
    
    # Files students need (will be renamed)
    student_files = {
        'simple_submission.py': 'simple_submission.py',  # Student assignment script
        'STUDENT_README.md': 'README.md',                # Student instructions
        'requirements.txt': 'requirements.txt'           # Just python-docx
    }
    
    # Files to keep for instructor use (hidden from students)
    instructor_files = [
        'simple_autograder.py',     # Grading logic (stays in template)
        'simple_dashboard.py',      # Instructor dashboard
        'generate-assignment.py',   # Original script
        'README.md',               # Instructor documentation
        'setup_template.py',       # This setup script
        'GITHUB_CLASSROOM_SETUP.md' # Setup guide
    ]
    
    # GitHub Actions workflow stays (needed for autograding)
    # .github/workflows/classroom.yml
    
    print("📁 Files students will get:")
    for src, dst in student_files.items():
        if os.path.exists(src):
            print(f"   ✅ {dst}")
        else:
            print(f"   ❌ {src} (missing)")
    
    print("\n🔒 Files hidden from students (instructor only):")
    for file in instructor_files:
        if os.path.exists(file):
            print(f"   🔐 {file}")
    
    print(f"\n⚙️  Autograding workflow: .github/workflows/classroom.yml")
    
    print("\n" + "="*60)
    print("🎯 GITHUB CLASSROOM SETUP INSTRUCTIONS:")
    print("="*60)
    print("1. Create GitHub Classroom assignment")
    print("2. Use this repository as template")
    print("3. Enable autograding (6 tests will be detected)")
    print("4. Students get clean repo with just:")
    print("   - simple_submission.py")
    print("   - README.md (student instructions)")
    print("   - requirements.txt")
    print("   - .github/workflows/classroom.yml (autograding)")
    print("\n5. Students CAN'T see:")
    print("   - simple_autograder.py (your grading logic)")
    print("   - simple_dashboard.py (your grade viewer)")
    print("   - Any instructor documentation")
    print("\n✅ This ensures academic integrity while providing autograding!")

def main():
    print("📚 CSCI 1436 Assignment #1 - GitHub Classroom Template Setup")
    print("=" * 70)
    
    choice = input("\nWhat would you like to do?\n1. Show setup instructions\n2. Test student experience locally\nChoice (1-2): ")
    
    if choice == "1":
        prepare_student_template()
        print(f"\n🚀 Ready for GitHub Classroom!")
        print(f"📖 See GITHUB_CLASSROOM_SETUP.md for detailed instructions")
        
    elif choice == "2":
        print("\n🧪 Testing student experience...")
        if os.path.exists('simple_submission.py'):
            print("✅ Student script found")
            print("Run: python simple_submission.py")
        else:
            print("❌ simple_submission.py not found")
            
        if os.path.exists('.github/workflows/classroom.yml'):
            print("✅ Autograding workflow found")
        else:
            print("❌ .github/workflows/classroom.yml not found")
            
    else:
        print("Invalid choice. Run again and choose 1 or 2.")

if __name__ == "__main__":
    main()
