# facescanner database
summary of DB content

example.py gives examples for creating and interacting with the databse

## Tables and rows
- STUDENTS
    - Represents students
    - id
    - first name
    - last name
    - netID
- CLASSES
    - Represents individual classes/sections
    - id
    - class number
    - title (if applicable)
    - lecture vs lab
    - date
    - day of week
- ATTENDANCE
    - Represents attendance taken, answers "was a student at this class?"
    - id
    - student.id
    - date
    - attended? bool
- IMAGECAPTURES
    - References image captures from attendance camera, stores file path
    - id
    - path/to/image
    - date-taken
- FACECACHE (?)
    - If opencv does this, we could store the area of an image where a face was detected. Would be useful for troubleshooting and possibly teaching the algorithm. This could also be where we keep a seed image
    - id
    - student.id
    - path/to/image