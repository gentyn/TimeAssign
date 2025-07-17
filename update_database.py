#!/usr/bin/env python3
"""
Database Update Script for TimeAssign
This script updates the database with professional demonstration data.
"""

import os
import sys
import django
from datetime import time

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timeassign.settings')
django.setup()

from ta_app.models import myUser, Course, Break

def clear_existing_data():
    """Clear all existing data from the database."""
    print("Clearing existing data...")
    myUser.objects.all().delete()
    Course.objects.all().delete()
    Break.objects.all().delete()
    print("✓ Existing data cleared")

def create_users():
    """Create professional user accounts for demonstration."""
    print("\nCreating users...")
    
    users_data = [
        # Department Chair
        {
            'username': 'dr_smith',
            'password': 'chair2024',
            'name': 'Dr. Sarah Smith',
            'usertype': 'chair',
            'email': 'smith@uwm.edu'
        },
        # Instructors
        {
            'username': 'prof_johnson',
            'password': 'instructor2024',
            'name': 'Prof. Michael Johnson',
            'usertype': 'instructor',
            'email': 'johnson@uwm.edu'
        },
        {
            'username': 'prof_williams',
            'password': 'instructor2024',
            'name': 'Prof. Emily Williams',
            'usertype': 'instructor',
            'email': 'williams@uwm.edu'
        },
        {
            'username': 'prof_brown',
            'password': 'instructor2024',
            'name': 'Prof. David Brown',
            'usertype': 'instructor',
            'email': 'brown@uwm.edu'
        },
        # Teaching Assistants
        {
            'username': 'ta_chen',
            'password': 'ta2024',
            'name': 'Alex Chen',
            'usertype': 'ta',
            'email': 'chen@uwm.edu',
            'assignedInstructor': 2  # Prof. Johnson
        },
        {
            'username': 'ta_garcia',
            'password': 'ta2024',
            'name': 'Maria Garcia',
            'usertype': 'ta',
            'email': 'garcia@uwm.edu',
            'assignedInstructor': 2  # Prof. Johnson
        },
        {
            'username': 'ta_patel',
            'password': 'ta2024',
            'name': 'Raj Patel',
            'usertype': 'ta',
            'email': 'patel@uwm.edu',
            'assignedInstructor': 3  # Prof. Williams
        },
        {
            'username': 'ta_kim',
            'password': 'ta2024',
            'name': 'Jennifer Kim',
            'usertype': 'ta',
            'email': 'kim@uwm.edu',
            'assignedInstructor': 4  # Prof. Brown
        },
        {
            'username': 'ta_rodriguez',
            'password': 'ta2024',
            'name': 'Carlos Rodriguez',
            'usertype': 'ta',
            'email': 'rodriguez@uwm.edu',
            'assignedInstructor': 3  # Prof. Williams
        }
    ]
    
    created_users = {}
    for user_data in users_data:
        user = myUser.objects.create(**user_data)
        created_users[user_data['username']] = user
        print(f"✓ Created {user.usertype}: {user.name}")
    
    return created_users

def create_courses(users):
    """Create professional course offerings with proper scheduling."""
    print("\nCreating courses...")
    
    courses_data = [
        # CS 101 - Introduction to Computer Science
        {
            'course_name': 'CS 101 - Introduction to Computer Science',
            'start_time': time(9, 0),  # 9:00 AM
            'end_time': time(10, 15),  # 10:15 AM
            'mon_flag': True,
            'wed_flag': True,
            'fri_flag': True,
            'coursetype': 'LEC',
            'instructor': users['prof_johnson'].id,
            'ta1': users['ta_chen'].id,
            'ta2': users['ta_garcia'].id
        },
        {
            'course_name': 'CS 101 Lab A',
            'start_time': time(10, 30),  # 10:30 AM
            'end_time': time(12, 30),  # 12:30 PM
            'mon_flag': True,
            'coursetype': 'LAB',
            'lectureid': 1,  # Will be set after course creation
            'ta1': users['ta_chen'].id
        },
        {
            'course_name': 'CS 101 Lab B',
            'start_time': time(14, 0),  # 2:00 PM
            'end_time': time(16, 0),  # 4:00 PM
            'wed_flag': True,
            'coursetype': 'LAB',
            'lectureid': 1,  # Will be set after course creation
            'ta1': users['ta_garcia'].id
        },
        
        # CS 201 - Data Structures
        {
            'course_name': 'CS 201 - Data Structures',
            'start_time': time(11, 0),  # 11:00 AM
            'end_time': time(12, 15),  # 12:15 PM
            'tues_flag': True,
            'thurs_flag': True,
            'coursetype': 'LEC',
            'instructor': users['prof_williams'].id,
            'ta1': users['ta_patel'].id,
            'ta2': users['ta_rodriguez'].id
        },
        {
            'course_name': 'CS 201 Lab A',
            'start_time': time(13, 0),  # 1:00 PM
            'end_time': time(15, 0),  # 3:00 PM
            'tues_flag': True,
            'coursetype': 'LAB',
            'lectureid': 4,  # Will be set after course creation
            'ta1': users['ta_patel'].id
        },
        {
            'course_name': 'CS 201 Lab B',
            'start_time': time(15, 30),  # 3:30 PM
            'end_time': time(17, 30),  # 5:30 PM
            'thurs_flag': True,
            'coursetype': 'LAB',
            'lectureid': 4,  # Will be set after course creation
            'ta1': users['ta_rodriguez'].id
        },
        
        # CS 301 - Algorithms
        {
            'course_name': 'CS 301 - Algorithms',
            'start_time': time(13, 0),  # 1:00 PM
            'end_time': time(14, 15),  # 2:15 PM
            'mon_flag': True,
            'wed_flag': True,
            'fri_flag': True,
            'coursetype': 'LEC',
            'instructor': users['prof_brown'].id,
            'ta1': users['ta_kim'].id
        },
        {
            'course_name': 'CS 301 Lab',
            'start_time': time(14, 30),  # 2:30 PM
            'end_time': time(16, 30),  # 4:30 PM
            'wed_flag': True,
            'coursetype': 'LAB',
            'lectureid': 7,  # Will be set after course creation
            'ta1': users['ta_kim'].id
        },
        
        # Online Course
        {
            'course_name': 'CS 401 - Software Engineering',
            'start_time': time(16, 0),  # 4:00 PM
            'end_time': time(17, 15),  # 5:15 PM
            'tues_flag': True,
            'thurs_flag': True,
            'coursetype': 'ON',
            'instructor': users['prof_johnson'].id,
            'ta1': users['ta_chen'].id
        },
        
        # Grading Assignment
        {
            'course_name': 'CS 101 Grading',
            'start_time': time(9, 0),  # 9:00 AM
            'end_time': time(11, 0),  # 11:00 AM
            'fri_flag': True,
            'coursetype': 'GRD',
            'ta1': users['ta_garcia'].id
        }
    ]
    
    created_courses = []
    for course_data in courses_data:
        course = Course.objects.create(**course_data)
        created_courses.append(course)
        print(f"✓ Created {course.coursetype}: {course.course_name}")
    
    # Update lecture IDs for labs
    cs101_lecture = Course.objects.filter(course_name__contains='CS 101', coursetype='LEC').first()
    cs201_lecture = Course.objects.filter(course_name__contains='CS 201', coursetype='LEC').first()
    cs301_lecture = Course.objects.filter(course_name__contains='CS 301', coursetype='LEC').first()
    
    # Update lab lecture IDs
    Course.objects.filter(course_name__contains='CS 101 Lab').update(lectureid=cs101_lecture.id)
    Course.objects.filter(course_name__contains='CS 201 Lab').update(lectureid=cs201_lecture.id)
    Course.objects.filter(course_name__contains='CS 301 Lab').update(lectureid=cs301_lecture.id)
    
    return created_courses

def create_breaks(users):
    """Create professional break schedules for TAs."""
    print("\nCreating breaks...")
    
    breaks_data = [
        # Lunch breaks
        {
            'break_name': 'Lunch Break',
            'start_time': time(12, 0),  # 12:00 PM
            'end_time': time(13, 0),  # 1:00 PM
            'mon_flag': True,
            'tues_flag': True,
            'wed_flag': True,
            'thurs_flag': True,
            'fri_flag': True,
            'userid': users['ta_chen'].id
        },
        {
            'break_name': 'Lunch Break',
            'start_time': time(12, 30),  # 12:30 PM
            'end_time': time(13, 30),  # 1:30 PM
            'mon_flag': True,
            'tues_flag': True,
            'wed_flag': True,
            'thurs_flag': True,
            'fri_flag': True,
            'userid': users['ta_garcia'].id
        },
        {
            'break_name': 'Lunch Break',
            'start_time': time(12, 0),  # 12:00 PM
            'end_time': time(13, 0),  # 1:00 PM
            'mon_flag': True,
            'tues_flag': True,
            'wed_flag': True,
            'thurs_flag': True,
            'fri_flag': True,
            'userid': users['ta_patel'].id
        },
        {
            'break_name': 'Lunch Break',
            'start_time': time(12, 0),  # 12:00 PM
            'end_time': time(13, 0),  # 1:00 PM
            'mon_flag': True,
            'tues_flag': True,
            'wed_flag': True,
            'thurs_flag': True,
            'fri_flag': True,
            'userid': users['ta_kim'].id
        },
        {
            'break_name': 'Lunch Break',
            'start_time': time(12, 0),  # 12:00 PM
            'end_time': time(13, 0),  # 1:00 PM
            'mon_flag': True,
            'tues_flag': True,
            'wed_flag': True,
            'thurs_flag': True,
            'fri_flag': True,
            'userid': users['ta_rodriguez'].id
        },
        
        # Office hours and study breaks
        {
            'break_name': 'Office Hours',
            'start_time': time(15, 0),  # 3:00 PM
            'end_time': time(16, 0),  # 4:00 PM
            'tues_flag': True,
            'thurs_flag': True,
            'userid': users['ta_chen'].id
        },
        {
            'break_name': 'Study Time',
            'start_time': time(16, 0),  # 4:00 PM
            'end_time': time(17, 0),  # 5:00 PM
            'mon_flag': True,
            'wed_flag': True,
            'fri_flag': True,
            'userid': users['ta_garcia'].id
        },
        {
            'break_name': 'Office Hours',
            'start_time': time(14, 0),  # 2:00 PM
            'end_time': time(15, 0),  # 3:00 PM
            'mon_flag': True,
            'wed_flag': True,
            'userid': users['ta_patel'].id
        }
    ]
    
    for break_data in breaks_data:
        break_obj = Break.objects.create(**break_data)
        user = myUser.objects.get(id=break_data['userid'])
        print(f"✓ Created break for {user.name}: {break_obj.break_name}")
    
    return Break.objects.all()

def main():
    """Main function to update the database."""
    print("🔄 Updating TimeAssign Database with Professional Demo Data")
    print("=" * 60)
    
    try:
        # Clear existing data
        clear_existing_data()
        
        # Create new data
        users = create_users()
        courses = create_courses(users)
        breaks = create_breaks(users)
        
        print("\n" + "=" * 60)
        print("✅ Database update completed successfully!")
        print("\n📊 Summary:")
        print(f"   • {len(users)} users created")
        print(f"   • {len(courses)} courses created")
        print(f"   • {len(breaks)} breaks created")
        
        print("\n🔑 Demo Login Credentials:")
        print("   Chair: dr_smith / chair2024")
        print("   Instructor: prof_johnson / instructor2024")
        print("   TA: ta_chen / ta2024")
        
        print("\n🌐 Access the application at: http://127.0.0.1:8000/")
        
    except Exception as e:
        print(f"\n❌ Error updating database: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 