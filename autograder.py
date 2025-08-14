#!/usr/bin/env python3
"""
Autograder for CSCI 1436 Assignment #1
Runs in GitHub Classroom to automatically grade student submissions
"""

import json
import re
import sys
import os
import glob
from typing import Dict, List, Tuple

class AutoGrader:
    def __init__(self):
        self.submission_data = None
        self.load_submission_data()
    
    def load_submission_data(self):
        """Load student submission JSON data"""
        # Find submission JSON file
        json_files = glob.glob("submission_*.json")
        if not json_files:
            print("❌ No submission file found")
            sys.exit(1)
        
        with open(json_files[0], 'r') as f:
            self.submission_data = json.load(f)
        
        # Convert to expected format for compatibility
        if 'responses' in self.submission_data:
            for question_id, response_data in self.submission_data['responses'].items():
                if 'points' not in response_data:
                    # Add point values based on question ID
                    point_map = {
                        'q1_definitions': 40,
                        'q2_high_level': 12, 
                        'q3_declarations': 12,
                        'q4_modulo': 12,
                        'q5_sphere_volume': 12,
                        'q6_debugging': 12
                    }
                    response_data['points'] = point_map.get(question_id, 0)
    
    def grade_q1_definitions(self) -> Tuple[int, str]:
        """Grade Question 1 - Definitions (40 points)"""
        response = self.submission_data['responses']['q1_definitions']['response'].lower()
        
        # Define key terms and their expected concepts
        terms = {
            'repl': ['read', 'eval', 'print', 'loop', 'interactive'],
            'java api': ['application', 'programming', 'interface', 'library', 'classes'],
            'jdk': ['development', 'kit', 'tools', 'compiler', 'runtime'],
            'variable': ['storage', 'container', 'value', 'memory', 'data'],
            'data type': ['type', 'kind', 'category', 'int', 'string', 'boolean'],
            'variable declaration': ['create', 'define', 'specify', 'type', 'name'],
            'assignment statement': ['assign', 'value', 'variable', '=', 'store'],
            'expression': ['combination', 'evaluate', 'value', 'operation', 'calculate'],
            'constant': ['unchanging', 'fixed', 'final', 'immutable', 'same'],
            'literal': ['value', 'directly', 'written', 'code', 'constant']
        }
        
        points = 0
        feedback = []
        
        for term, keywords in terms.items():
            term_found = False
            keyword_count = 0
            
            # Check if term is mentioned
            if term.replace(' ', '') in response.replace(' ', ''):
                term_found = True
                
                # Check for relevant keywords
                for keyword in keywords:
                    if keyword in response:
                        keyword_count += 1
                
                # Award points based on keyword coverage
                if keyword_count >= 2:
                    points += 4  # Full points for well-defined term
                    feedback.append(f"✅ {term.upper()}: Well defined")
                elif keyword_count >= 1:
                    points += 2  # Partial points
                    feedback.append(f"⚠️ {term.upper()}: Partially defined")
                else:
                    points += 1  # Minimal points for mentioning term
                    feedback.append(f"❌ {term.upper()}: Needs better definition")
            else:
                feedback.append(f"❌ {term.upper()}: Not found or poorly defined")
        
        feedback_text = "\n".join(feedback)
        return min(points, 40), feedback_text
    
    def grade_q2_high_level(self) -> Tuple[int, str]:
        """Grade Question 2 - High Level Languages (12 points)"""
        response = self.submission_data['responses']['q2_high_level']['response'].lower()
        
        key_concepts = {
            'abstraction': ['abstract', 'hide', 'complexity', 'simple'],
            'portability': ['portable', 'platform', 'independent', 'cross'],
            'readability': ['readable', 'understand', 'clear', 'human'],
            'productivity': ['faster', 'efficient', 'quick', 'productive'],
            'maintenance': ['maintain', 'modify', 'update', 'change'],
            'syntax': ['syntax', 'english', 'natural', 'easier']
        }
        
        points = 0
        found_concepts = []
        
        for concept, keywords in key_concepts.items():
            for keyword in keywords:
                if keyword in response:
                    if concept not in found_concepts:
                        found_concepts.append(concept)
                        points += 2
                    break
        
        # Bonus points for well-structured answer
        if len(response.split()) >= 20:  # Substantial answer
            points += 2
        
        feedback = f"Found concepts: {', '.join(found_concepts)}"
        return min(points, 12), feedback
    
    def grade_q3_declarations(self) -> Tuple[int, str]:
        """Grade Question 3 - Variable Declarations (12 points)"""
        response = self.submission_data['responses']['q3_declarations']['response']
        
        patterns = [
            (r'double\s+length\s*=\s*23\.6', "double length = 23.6"),
            (r'float\s+width\s*=\s*14\.7[fF]?', "float width = 14.7f"),
            (r'long\s+distance\s*=\s*3172900000[lL]?', "long distance = 3172900000L"),
            (r'final\s+int\s+speedOfSound\s*=\s*343', "final int speedOfSound = 343")
        ]
        
        points = 0
        feedback = []
        
        for pattern, description in patterns:
            if re.search(pattern, response, re.IGNORECASE):
                points += 3
                feedback.append(f"✅ {description}")
            else:
                feedback.append(f"❌ Missing or incorrect: {description}")
        
        feedback_text = "\n".join(feedback)
        return points, feedback_text
    
    def grade_q4_modulo(self) -> Tuple[int, str]:
        """Grade Question 4 - Modulo Operations (12 points)"""
        response = self.submission_data['responses']['q4_modulo']['response']
        
        expected_answers = ["6", "0", "23", "6"]
        expressions = ["40 % 17", "120 % 60", "(65 + 8) % 25", "(97 * 3 + 6) % 25"]
        
        points = 0
        feedback = []
        
        for i, (expr, expected) in enumerate(zip(expressions, expected_answers)):
            if expected in response:
                points += 3
                feedback.append(f"✅ {expr} = {expected}")
            else:
                feedback.append(f"❌ {expr} ≠ {expected}")
        
        feedback_text = "\n".join(feedback)
        return points, feedback_text
    
    def grade_q5_sphere_volume(self) -> Tuple[int, str]:
        """Grade Question 5 - Sphere Volume Program (12 points)"""
        response = self.submission_data['responses']['q5_sphere_volume']['response'].lower()
        
        required_elements = {
            'input': ['input', 'scanner', 'readline', 'nextdouble'],
            'radius': ['radius', 'r'],
            'volume': ['volume', 'vol'],
            'formula': ['4/3', '4.0/3', 'math.pi', 'pi'],
            'power': ['math.pow', 'pow', 'r*r*r', '^3', '**3'],
            'output': ['print', 'system.out', 'println']
        }
        
        points = 0
        found_elements = []
        
        for element, keywords in required_elements.items():
            for keyword in keywords:
                if keyword in response:
                    if element not in found_elements:
                        found_elements.append(element)
                        points += 2
                    break
        
        feedback = f"Program elements found: {', '.join(found_elements)}"
        return min(points, 12), feedback
    
    def grade_q6_debugging(self) -> Tuple[int, str]:
        """Grade Question 6 - Debugging (12 points)"""
        response = self.submission_data['responses']['q6_debugging']['response'].lower()
        
        issues = {
            'division by zero': ['division', 'zero', 'divide', '/'],
            'integer overflow': ['overflow', 'exceed', 'limit', 'max'],
            'type mismatch': ['type', 'mismatch', 'long', 'int', 'conversion']
        }
        
        points = 0
        found_issues = []
        
        for issue, keywords in issues.items():
            keyword_count = sum(1 for keyword in keywords if keyword in response)
            if keyword_count >= 2:
                if issue not in found_issues:
                    found_issues.append(issue)
                    points += 4
        
        feedback = f"Issues identified: {', '.join(found_issues)}"
        return min(points, 12), feedback
    
    def grade_question(self, question_id: str) -> None:
        """Grade a specific question and output results"""
        grading_methods = {
            'q1_definitions': self.grade_q1_definitions,
            'q2_high_level': self.grade_q2_high_level,
            'q3_declarations': self.grade_q3_declarations,
            'q4_modulo': self.grade_q4_modulo,
            'q5_sphere_volume': self.grade_q5_sphere_volume,
            'q6_debugging': self.grade_q6_debugging
        }
        
        if question_id not in grading_methods:
            print(f"❌ Unknown question ID: {question_id}")
            sys.exit(1)
        
        points, feedback = grading_methods[question_id]()
        max_points = self.submission_data['responses'][question_id]['points']
        
        # Output for GitHub Classroom
        print(f"Score: {points}/{max_points}")
        print(f"Feedback: {feedback}")
        
        # Exit with score for GitHub Classroom
        if points == max_points:
            sys.exit(0)  # Perfect score
        else:
            sys.exit(1)  # Partial credit (GitHub Classroom will still award points based on output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python autograder.py <question_id>")
        sys.exit(1)
    
    question_id = sys.argv[1]
    grader = AutoGrader()
    grader.grade_question(question_id)

if __name__ == "__main__":
    main()
