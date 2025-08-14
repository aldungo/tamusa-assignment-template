#!/usr/bin/env python3
"""
Instructor Dashboard for CSCI 1436 Assignment #1
View autograded results from GitHub Classroom and track Turnitin submissions
"""

import json
import os
import glob
import pandas as pd
from datetime import datetime
import requests
from typing import Dict, List
import argparse

class InstructorDashboard:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.org_name = "your-github-classroom-org"  # Replace with your org
        self.assignment_name = "csci1436-assignment1"
        
    def fetch_github_classroom_results(self) -> List[Dict]:
        """Fetch autograding results from GitHub Classroom"""
        if not self.github_token:
            print("⚠️ GITHUB_TOKEN not found. Using local files instead.")
            return self.load_local_results()
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        # Get all repositories for the assignment
        url = f"https://api.github.com/orgs/{self.org_name}/repos"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"❌ Failed to fetch repositories: {response.status_code}")
            return []
        
        repos = response.json()
        assignment_repos = [repo for repo in repos if self.assignment_name in repo['name']]
        
        results = []
        for repo in assignment_repos:
            repo_name = repo['name']
            student_name = repo_name.replace(f"{self.assignment_name}-", "")
            
            # Get latest commit autograding results
            commits_url = f"https://api.github.com/repos/{self.org_name}/{repo_name}/commits"
            commits_response = requests.get(commits_url, headers=headers)
            
            if commits_response.status_code == 200:
                commits = commits_response.json()
                if commits:
                    latest_commit = commits[0]
                    
                    # Get check runs for autograding
                    check_runs_url = f"https://api.github.com/repos/{self.org_name}/{repo_name}/commits/{latest_commit['sha']}/check-runs"
                    check_response = requests.get(check_runs_url, headers=headers)
                    
                    if check_response.status_code == 200:
                        check_runs = check_response.json()
                        autograding_results = self.parse_autograding_results(check_runs)
                        
                        results.append({
                            'student_name': student_name,
                            'repo_name': repo_name,
                            'submission_time': latest_commit['commit']['committer']['date'],
                            'autograding_results': autograding_results,
                            'total_score': sum(result['points'] for result in autograding_results),
                            'max_score': sum(result['max_points'] for result in autograding_results)
                        })
        
        return results
    
    def load_local_results(self) -> List[Dict]:
        """Load results from local submission files (for testing)"""
        results = []
        json_files = glob.glob("submission_*.json")
        
        for json_file in json_files:
            with open(json_file, 'r') as f:
                submission_data = json.load(f)
            
            student_info = submission_data['student_info']
            student_name = f"{student_info['first_name']} {student_info['last_name']}"
            
            # Simulate autograding results
            autograding_results = []
            total_score = 0
            
            for question_id, response_data in submission_data['responses'].items():
                # This would normally come from GitHub Classroom
                simulated_score = response_data['points'] * 0.8  # Assume 80% average
                autograding_results.append({
                    'question_id': question_id,
                    'question_num': response_data['question_num'],
                    'points': int(simulated_score),
                    'max_points': response_data['points'],
                    'feedback': "Autograded by GitHub Classroom"
                })
                total_score += int(simulated_score)
            
            results.append({
                'student_name': student_name,
                'student_id': student_info['student_id'],
                'submission_time': submission_data['assignment_info']['submission_timestamp'],
                'autograding_results': autograding_results,
                'total_score': total_score,
                'max_score': submission_data['assignment_info']['total_points'],
                'turnitin_submitted': self.check_turnitin_submission(student_name)
            })
        
        return results
    
    def parse_autograding_results(self, check_runs: Dict) -> List[Dict]:
        """Parse GitHub Classroom autograding results"""
        results = []
        
        for check_run in check_runs.get('check_runs', []):
            if check_run['name'] == 'Autograding':
                # Parse the check run output for individual question scores
                output = check_run.get('output', {}).get('text', '')
                
                # This would need to be customized based on your autograding output format
                # For now, return a placeholder
                results = [
                    {'question_id': 'q1_definitions', 'question_num': 1, 'points': 32, 'max_points': 40, 'feedback': 'Good definitions'},
                    {'question_id': 'q2_high_level', 'question_num': 2, 'points': 10, 'max_points': 12, 'feedback': 'Missing some concepts'},
                    {'question_id': 'q3_declarations', 'question_num': 3, 'points': 12, 'max_points': 12, 'feedback': 'Perfect syntax'},
                    {'question_id': 'q4_modulo', 'question_num': 4, 'points': 9, 'max_points': 12, 'feedback': 'Some calculation errors'},
                    {'question_id': 'q5_sphere_volume', 'question_num': 5, 'points': 10, 'max_points': 12, 'feedback': 'Good program structure'},
                    {'question_id': 'q6_debugging', 'question_num': 6, 'points': 8, 'max_points': 12, 'feedback': 'Identified most issues'}
                ]
                break
        
        return results
    
    def check_turnitin_submission(self, student_name: str) -> bool:
        """Check if student has submitted to Turnitin (placeholder)"""
        # This would integrate with Turnitin API or check a tracking file
        # For now, simulate random submissions
        import random
        return random.choice([True, False])
    
    def generate_grade_report(self, results: List[Dict]) -> pd.DataFrame:
        """Generate a comprehensive grade report"""
        report_data = []
        
        for result in results:
            row = {
                'Student Name': result['student_name'],
                'Student ID': result.get('student_id', 'N/A'),
                'Submission Time': result['submission_time'],
                'Total Score': result['total_score'],
                'Max Score': result['max_score'],
                'Percentage': f"{(result['total_score'] / result['max_score'] * 100):.1f}%",
                'Turnitin Submitted': '✅' if result.get('turnitin_submitted', False) else '❌'
            }
            
            # Add individual question scores
            for q_result in result['autograding_results']:
                q_num = q_result['question_num']
                row[f'Q{q_num} Score'] = f"{q_result['points']}/{q_result['max_points']}"
            
            report_data.append(row)
        
        return pd.DataFrame(report_data)
    
    def generate_detailed_feedback(self, results: List[Dict]) -> None:
        """Generate detailed feedback for each student"""
        os.makedirs('feedback_reports', exist_ok=True)
        
        for result in results:
            student_name = result['student_name']
            filename = f"feedback_reports/{student_name.replace(' ', '_')}_feedback.txt"
            
            with open(filename, 'w') as f:
                f.write(f"CSCI 1436 Programming Fundamentals I - Assignment #1\n")
                f.write(f"Student: {student_name}\n")
                f.write(f"Submission Time: {result['submission_time']}\n")
                f.write(f"Total Score: {result['total_score']}/{result['max_score']} ({(result['total_score'] / result['max_score'] * 100):.1f}%)\n")
                f.write("=" * 60 + "\n\n")
                
                for q_result in result['autograding_results']:
                    f.write(f"Question {q_result['question_num']}: {q_result['points']}/{q_result['max_points']} points\n")
                    f.write(f"Feedback: {q_result['feedback']}\n\n")
                
                f.write("Turnitin Submission: ")
                f.write("✅ Submitted" if result.get('turnitin_submitted', False) else "❌ Not Found")
                f.write("\n\n")
                
                # Add improvement suggestions
                f.write("Suggestions for Improvement:\n")
                f.write("- Review concepts for questions with lower scores\n")
                f.write("- Practice coding syntax and debugging\n")
                f.write("- Ensure complete definitions for terminology questions\n")
    
    def export_to_lms(self, df: pd.DataFrame, format: str = 'csv') -> str:
        """Export grades in LMS-compatible format"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == 'csv':
            filename = f"grades_export_{timestamp}.csv"
            df.to_csv(filename, index=False)
        elif format == 'excel':
            filename = f"grades_export_{timestamp}.xlsx"
            df.to_excel(filename, index=False)
        else:
            raise ValueError("Format must be 'csv' or 'excel'")
        
        return filename
    
    def run_dashboard(self, export_format: str = 'csv'):
        """Main dashboard function"""
        print("🎓 CSCI 1436 Assignment #1 - Instructor Dashboard")
        print("=" * 60)
        
        # Fetch results
        print("📊 Fetching autograding results...")
        results = self.fetch_github_classroom_results()
        
        if not results:
            print("❌ No results found. Make sure students have submitted their assignments.")
            return
        
        print(f"✅ Found {len(results)} submissions")
        
        # Generate reports
        print("📋 Generating grade report...")
        df = self.generate_grade_report(results)
        
        # Display summary
        print("\n📈 Grade Summary:")
        print(f"Total Submissions: {len(results)}")
        print(f"Average Score: {df['Total Score'].mean():.1f}/{df['Max Score'].iloc[0]}")
        print(f"Highest Score: {df['Total Score'].max()}")
        print(f"Lowest Score: {df['Total Score'].min()}")
        
        turnitin_count = sum(1 for result in results if result.get('turnitin_submitted', False))
        print(f"Turnitin Submissions: {turnitin_count}/{len(results)}")
        
        # Display grade table
        print("\n📊 Individual Grades:")
        print(df.to_string(index=False))
        
        # Generate detailed feedback
        print("\n📝 Generating detailed feedback reports...")
        self.generate_detailed_feedback(results)
        
        # Export grades
        export_file = self.export_to_lms(df, export_format)
        print(f"💾 Grades exported to: {export_file}")
        
        print("\n✅ Dashboard complete!")
        print("📁 Check the 'feedback_reports' folder for individual student feedback")

def main():
    parser = argparse.ArgumentParser(description='Instructor Dashboard for CSCI 1436 Assignment #1')
    parser.add_argument('--format', choices=['csv', 'excel'], default='csv',
                       help='Export format for grades (default: csv)')
    
    args = parser.parse_args()
    
    dashboard = InstructorDashboard()
    dashboard.run_dashboard(args.format)

if __name__ == "__main__":
    main()
