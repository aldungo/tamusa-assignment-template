#!/usr/bin/env python3
"""
Simple Autograder for CSCI 1436 Assignment #1
Grades JSON submissions and provides percentage scores to students.
"""

import json
import re
import sys
import glob

class SimpleGrader:
    def __init__(self):
        self.submission = self.load_submission()
    
    def load_submission(self):
        """Load student submission JSON"""
        json_files = glob.glob("assignment1_*.json")
        if not json_files:
            print("❌ ERROR: No submission file found")
            sys.exit(1)
        
        with open(json_files[0], 'r') as f:
            return json.load(f)
    
    def grade_definitions(self):
        """Grade Q1: Definitions (40 points)"""
        answer = self.submission['answers']['q1_definitions']['answer'].lower()
        
        # Key terms and their important concepts
        terms = {
            'repl': ['read', 'eval', 'print', 'loop', 'interactive', 'command'],
            'java api': ['application', 'programming', 'interface', 'library', 'classes', 'methods'],
            'jdk': ['development', 'kit', 'tools', 'compiler', 'runtime', 'java'],
            'variable': ['storage', 'container', 'value', 'memory', 'data', 'holds'],
            'data type': ['type', 'kind', 'category', 'int', 'string', 'boolean', 'specifies'],
            'variable declaration': ['create', 'define', 'specify', 'type', 'name', 'declares'],
            'assignment statement': ['assign', 'value', 'variable', '=', 'store', 'gives'],
            'expression': ['combination', 'evaluate', 'value', 'operation', 'calculate', 'produces'],
            'constant': ['unchanging', 'fixed', 'final', 'immutable', 'same', 'cannot change'],
            'literal': ['value', 'directly', 'written', 'code', 'constant', 'actual']
        }
        
        score = 0
        for term, keywords in terms.items():
            # Check if term is mentioned
            if any(word in answer for word in term.split()):
                # Award points based on keyword coverage
                matches = sum(1 for keyword in keywords if keyword in answer)
                if matches >= 3:
                    score += 4  # Excellent definition
                elif matches >= 2:
                    score += 3  # Good definition
                elif matches >= 1:
                    score += 2  # Basic definition
                else:
                    score += 1  # Term mentioned but poor definition
        
        return min(score, 40)
    
    def grade_languages(self):
        """Grade Q2: High-level vs Low-level (12 points)"""
        answer = self.submission['answers']['q2_languages']['answer'].lower()
        
        key_concepts = [
            'abstract', 'abstraction', 'portable', 'portability', 'readable', 'readability',
            'easier', 'simple', 'understand', 'maintain', 'productive', 'faster',
            'english', 'natural', 'human', 'complex', 'hardware'
        ]
        
        score = 0
        for concept in key_concepts:
            if concept in answer:
                score += 1
        
        # Bonus for substantial answer
        if len(answer.split()) >= 15:
            score += 2
        
        return min(score, 12)
    
    def grade_declarations(self):
        """Grade Q3: Variable declarations (12 points)"""
        answer = self.submission['answers']['q3_declarations']['answer']
        
        # Check for correct declarations (3 points each)
        patterns = [
            r'double\s+length\s*=\s*23\.6',
            r'float\s+width\s*=\s*14\.7[fF]?',
            r'long\s+distance\s*=\s*3172900000[lL]?',
            r'final\s+int\s+speedOfSound\s*=\s*343'
        ]
        
        score = 0
        for pattern in patterns:
            if re.search(pattern, answer, re.IGNORECASE):
                score += 3
        
        return score
    
    def grade_modulo(self):
        """Grade Q4: Modulo operations (12 points)"""
        answer = self.submission['answers']['q4_modulo']['answer']
        
        # Expected answers (3 points each)
        expected = ['6', '0', '23', '6']
        
        score = 0
        for expected_val in expected:
            if expected_val in answer:
                score += 3
        
        return score
    
    def grade_programming(self):
        """Grade Q5: Sphere volume program (12 points)"""
        answer = self.submission['answers']['q5_programming']['answer'].lower()
        
        # Required elements (2 points each)
        elements = [
            ['input', 'scanner', 'readline'],           # Input handling
            ['radius', 'r'],                           # Variable name
            ['volume', 'vol'],                         # Result variable  
            ['4/3', '4.0/3', '(4/3)'],                # Formula constant
            ['pi', 'math.pi', '3.14'],                # Pi constant
            ['*', 'multiply', 'pow', '^', '**']       # Mathematical operations
        ]
        
        score = 0
        for element_group in elements:
            if any(element in answer for element in element_group):
                score += 2
        
        return min(score, 12)
    
    def grade_debugging(self):
        """Grade Q6: Code debugging (12 points)"""
        answer = self.submission['answers']['q6_debugging']['answer'].lower()
        
        # Key issues to identify (4 points each)
        issues = [
            ['division by zero', 'divide by zero', '/0', 'zero division'],
            ['overflow', 'integer overflow', 'exceed', 'too large', 'maximum'],
            ['type mismatch', 'long to int', 'conversion', 'cast', 'incompatible']
        ]
        
        score = 0
        for issue_group in issues:
            if any(issue in answer for issue in issue_group):
                score += 4
        
        return min(score, 12)
    
    def grade_all(self):
        """Grade entire assignment and return results"""
        grading_methods = {
            'q1_definitions': (self.grade_definitions, 40),
            'q2_languages': (self.grade_languages, 12),
            'q3_declarations': (self.grade_declarations, 12),
            'q4_modulo': (self.grade_modulo, 12),
            'q5_programming': (self.grade_programming, 12),
            'q6_debugging': (self.grade_debugging, 12)
        }
        
        results = {}
        total_earned = 0
        total_possible = 0
        
        for question_id, (method, max_points) in grading_methods.items():
            earned = method()
            percentage = (earned / max_points) * 100
            
            results[question_id] = {
                'earned': earned,
                'max_points': max_points,
                'percentage': percentage
            }
            
            total_earned += earned
            total_possible += max_points
        
        overall_percentage = (total_earned / total_possible) * 100
        
        return results, total_earned, total_possible, overall_percentage

def main():
    if len(sys.argv) < 2:
        print("Usage: python simple_autograder.py <question_id|all>")
        sys.exit(1)
    
    grader = SimpleGrader()
    student_name = grader.submission['student']['name']
    
    if sys.argv[1] == 'all':
        # Grade everything and show comprehensive results
        results, total_earned, total_possible, overall_percentage = grader.grade_all()
        
        print(f"🎓 CSCI 1436 Assignment #1 - Autograding Results")
        print(f"📚 Student: {student_name}")
        print(f"📊 Overall Score: {total_earned}/{total_possible} ({overall_percentage:.1f}%)")
        print("=" * 60)
        
        for question_id, result in results.items():
            q_num = question_id.split('_')[0].replace('q', 'Q')
            print(f"{q_num}: {result['earned']}/{result['max_points']} ({result['percentage']:.1f}%)")
        
        print("=" * 60)
        
        # Letter grade estimate
        if overall_percentage >= 90:
            grade = "A"
        elif overall_percentage >= 80:
            grade = "B"
        elif overall_percentage >= 70:
            grade = "C"
        elif overall_percentage >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"🎯 Estimated Grade: {grade}")
        
    else:
        # Grade individual question (for GitHub Classroom)
        question_id = sys.argv[1]
        
        methods = {
            'q1_definitions': grader.grade_definitions,
            'q2_languages': grader.grade_languages,
            'q3_declarations': grader.grade_declarations,
            'q4_modulo': grader.grade_modulo,
            'q5_programming': grader.grade_programming,
            'q6_debugging': grader.grade_debugging
        }
        
        if question_id not in methods:
            print(f"❌ Unknown question: {question_id}")
            sys.exit(1)
        
        score = methods[question_id]()
        max_points = grader.submission['answers'][question_id]['max_points']
        percentage = (score / max_points) * 100
        
        print(f"Score: {score}/{max_points} ({percentage:.1f}%)")
        
        # Exit code for GitHub Classroom
        sys.exit(0 if score > 0 else 1)

if __name__ == "__main__":
    main()
