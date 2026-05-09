const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static('./'));

// Persistent data storage (Simulating a database) 
let students = [];

// READ: Get all students
app.get('/api/students', (req, res) => {
    res.status(200).json(students);
});

// CREATE: Add a new student
app.post('/api/students', (req, res) => {
    try {
        const { name, email, course } = req.body;
        
        // Basic validation for UX/UI integrity 
        if (!name || !email) {
            return res.status(400).json({ error: "Name and Email are required" });
        }

        const newStudent = { id: Date.now().toString(), name, email, course };
        students.push(newStudent);
        res.status(201).json({ message: "Student registered successfully", student: newStudent });
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" }); // Robust error-handling [cite: 5]
    }
});

// DELETE: Remove a student (Required for full CRUD) 
app.delete('/api/students/:id', (req, res) => {
    const { id } = req.params;
    const initialLength = students.length;
    students = students.filter(student => student.id !== id);

    if (students.length === initialLength) {
        return res.status(404).json({ error: "Student not found" });
    }
    res.status(200).json({ message: "Student deleted successfully" });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});