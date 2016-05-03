# Scanning Faces at UIUC

*A work in progress*.

## Image Workflow
1. Visit the homepage
2. Click "Start Camera" to take pictures
3. camera.py takes images and saves them to static/photos_orig/
4. Click "View Original Pictures" to view the photos
5. Click "Manipulate Data" to run the photos through facial recognition
6. face.py runs facial detection against each photo in the photos_orig directory
7. face.py saves scanned images to photos_scanned
8. face.py moves original photo to scanned_originals
9. Click "View Detected Pictures" to view photos with faces highlighted
