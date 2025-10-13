public class Student {
	private String studentName;
	private int studentAge;
	private double studentGPA;

	public Student(String name, int age, double gpa) {
		this.studentName = name;
		this.studentAge = age;
		this.studentGPA = gpa;
	}

    private String calculateGradeLevel() {
		String gradeLevel;

        if (studentAge <= 6) {
			gradeLevel = "Kindergarten";
		} else if (studentAge <= 10) {
			gradeLevel = "Elementary";
		} else if (studentAge <= 13) {
			gradeLevel = "Middle School";
		} else if (studentAge <= 18) {
			gradeLevel = "High School";
		} else {
			gradeLevel = "University";
		}

        return gradeLevel;
    }

    private void printInfo() {
		System.out.println("Student: " + studentName);
		System.out.println("Age: " + studentAge);
		System.out.println("GPA: " + studentGPA);
		System.out.println("Level: " + calculateGradeLevel());
    }

    private void verifyScholarship() {
		if (studentGPA > 3.5 && studentAge >= 18) {
			System.out.println("Eligible for scholarship!");
		} else {
			System.out.println("Not eligible for scholarship.");
		}
    }

	public void processData() {
        printInfo();
        verifyScholarship();
	}
}
