Django Groups & Permissions System










This project demonstrates a simple and clean implementation of role-based access control in Django using Groups and Custom Permissions.

⭐ Features

Custom permissions:
can_view, can_create, can_edit, can_delete

Role groups:

Viewers – view only

Editors – view, create, edit

Admins – full control

Permission checks added to views

Easy to test with multiple users

🔧 How It Works

Custom permissions are defined inside the model’s Meta class.

Groups (Viewers, Editors, Admins) are created in the Django admin.

Each group receives specific permissions.

Views require the correct permission before performing actions.

Users are assigned to groups to control what they can access.

🧪 Testing

Create test users in the admin panel

Assign each to a different group

Log in and try:

Viewing items

Creating items

Editing items

Deleting items

Expected behavior:

Viewer → can only view

Editor → view, create, edit

Admin → everything

📁 Deliverables

models.py → contains custom permissions

views.py → enforces access controls

README.md → explains setup, usage, and testing