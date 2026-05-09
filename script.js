// Function to register a student via API
async function registerStudent(studentData) {
    try {
        const response = await fetch('/api/students', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(studentData)
        });

        const result = await response.json();

        if (response.ok) {
            console.log("Success:", result.message);
            displayStudents(); // Refresh the list
        } else {
            alert("Error: " + result.error); // Visual UI feedback 
        }
    } catch (error) {
        console.error("System Error:", error); // Systematic error-handling [cite: 5]
    }
}

// Function to delete a student (Live Demonstration feature) [cite: 9]
async function deleteStudent(studentId) {
    const response = await fetch(`/api/students/${studentId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        displayStudents();
    }
}