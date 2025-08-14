#!/usr/bin/env python3
"""
Simple Instructor Dashboard for CSCI 1436 Assignment #1
View autograding results and export grades.
"""

import json
import glob
import os
from datetime import datetime
import csv

def load_all_submissions():
    """Load all student submissions from local files or GitHub API"""
    submissions = []
    
    # Look for local submission files (for testing)
    json_files = glob.glob("assignment1_*.json")
    
    if json_files:
        print(f"📁 Found {len(json_files)} local submission files")
        for json_file in json_files:
            with open(json_file, 'r') as f:
                submission = json.load(f)
                submissions.append({
                    'file': json_file,
                    'data': submission
                })
    else:
        print("ℹ️ No local submissions found. In production, this would fetch from GitHub Classroom API.")
    
    return submissions

def grade_submission(submission_data):
    """Grade a single submission using the autograder logic"""
    from simple_autograder import SimpleGrader
    
    # Temporarily save submission for grader
    temp_file = f"temp_submission_{datetime.now().timestamp()}.json"
    with open(temp_file, 'w') as f:
        json.dump(submission_data, f)
    
    try:
        # Create grader instance and grade
        grader = SimpleGrader()
        grader.submission = submission_data  # Override loaded submission
        results, total_earned, total_possible, overall_percentage = grader.grade_all()
        
        return {
            'results': results,
            'total_earned': total_earned,
            'total_possible': total_possible,
            'overall_percentage': overall_percentage
        }
    finally:
        # Clean up temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)

def display_grade_summary(submissions):
    """Display grade summary for all submissions"""
    if not submissions:
        print("❌ No submissions to display")
        return []
    
    print("🎓 CSCI 1436 Assignment #1 - Grade Summary")
    print("=" * 80)
    
    graded_results = []
    
    for submission in submissions:
        student_name = submission['data']['student']['name']
        student_id = submission['data']['student']['id']
        submitted_at = submission['data']['assignment']['submitted_at']
        
        # Grade the submission
        grading_result = grade_submission(submission['data'])
        
        # Store result
        graded_results.append({
            'student_name': student_name,
            'student_id': student_id,
            'submitted_at': submitted_at,
            'total_earned': grading_result['total_earned'],
            'total_possible': grading_result['total_possible'],
            'percentage': grading_result['overall_percentage'],
            'detailed_results': grading_result['results']
        })
        
        # Display result
        print(f"📚 {student_name} (ID: {student_id})")
        print(f"   Score: {grading_result['total_earned']}/{grading_result['total_possible']} ({grading_result['overall_percentage']:.1f}%)")
        print(f"   Submitted: {datetime.fromisoformat(submitted_at.replace('Z', '+00:00')).strftime('%m/%d/%Y %I:%M %p')}")
        
        # Question breakdown
        for q_id, result in grading_result['results'].items():
            q_num = q_id.split('_')[0].replace('q', 'Q')
            print(f"   {q_num}: {result['earned']}/{result['max_points']} ({result['percentage']:.1f}%)")
        print()
    
    # Class statistics
    if graded_results:
        avg_score = sum(r['percentage'] for r in graded_results) / len(graded_results)
        max_score = max(r['percentage'] for r in graded_results)
        min_score = min(r['percentage'] for r in graded_results)
        
        print("📊 Class Statistics:")
        print(f"   Average: {avg_score:.1f}%")
        print(f"   Highest: {max_score:.1f}%")
        print(f"   Lowest: {min_score:.1f}%")
        print(f"   Total Submissions: {len(graded_results)}")
    
    return graded_results

def export_grades(graded_results, format='csv'):
    """Export grades for LMS import"""
    if not graded_results:
        print("❌ No grades to export")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"csci1436_assignment1_grades_{timestamp}.{format}"
    
    if format == 'csv':
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'Student Name', 'Student ID', 'Submission Date',
                'Q1 Score', 'Q1 Max', 'Q1 Percent',
                'Q2 Score', 'Q2 Max', 'Q2 Percent', 
                'Q3 Score', 'Q3 Max', 'Q3 Percent',
                'Q4 Score', 'Q4 Max', 'Q4 Percent',
                'Q5 Score', 'Q5 Max', 'Q5 Percent',
                'Q6 Score', 'Q6 Max', 'Q6 Percent',
                'Total Score', 'Total Possible', 'Final Percentage'
            ]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for result in graded_results:
                row = {
                    'Student Name': result['student_name'],
                    'Student ID': result['student_id'],
                    'Submission Date': datetime.fromisoformat(result['submitted_at'].replace('Z', '+00:00')).strftime('%m/%d/%Y %I:%M %p'),
                    'Total Score': result['total_earned'],
                    'Total Possible': result['total_possible'],
                    'Final Percentage': f"{result['percentage']:.1f}%"
                }
                
                # Add individual question scores
                for i, (q_id, q_result) in enumerate(result['detailed_results'].items(), 1):
                    row[f'Q{i} Score'] = q_result['earned']
                    row[f'Q{i} Max'] = q_result['max_points']
                    row[f'Q{i} Percent'] = f"{q_result['percentage']:.1f}%"
                
                writer.writerow(row)
    
    print(f"💾 Grades exported to: {filename}")
    return filename

def main():
    print("🎓 CSCI 1436 Assignment #1 - Instructor Dashboard")
    print("=" * 60)
    
    # Load submissions
    submissions = load_all_submissions()
    
    if not submissions:
        print("ℹ️ No submissions found. To test this dashboard:")
        print("   1. Have students run 'python simple_submission.py'")
        print("   2. Or create sample submission files")
        return
    
    # Display grades
    graded_results = display_grade_summary(submissions)
    
    # Export option
    if graded_results:
        print("\n💾 Export Options:")
        export_choice = input("Export grades to CSV? (y/n): ").lower()
        if export_choice == 'y':
            export_grades(graded_results, 'csv')
        
        print("\n✅ Dashboard complete!")
        print("📋 For GitHub Classroom integration:")
        print("   - Students see these scores in their GitHub Actions")
        print("   - Use the CSV export for your LMS gradebook")
        print("   - Word docs in Blackboard are just submission proof")

if __name__ == "__main__":
    main()
