import os
import subprocess
import mysql.connector

# Database connection configuration
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql123',
    'database': 'groceries'
}

# Define users and their roles
users = {
    'dbadmin': {
        'password': 'admin_password',
        'privileges': 'ALL PRIVILEGES'
    },
    'manager': {
        'password': 'manager_password',
        'privileges': 'SELECT, INSERT, UPDATE, DELETE'
    },
    'employee': {
        'password': 'employee_password',
        'privileges': 'SELECT'
    }
}

def create_mysql_users():
    # Connect to MySQL server
    with mysql.connector.connect(**config) as conn:
        cur = conn.cursor()
        
        # Create users and grant privileges
        for user, details in users.items():
            query = f"CREATE USER IF NOT EXISTS '{user}'@'localhost' IDENTIFIED BY '{details['password']}';"
            cur.execute(query)
            query = f"GRANT {details['privileges']} ON groceries.* TO '{user}'@'localhost';"
            cur.execute(query)
            cur.execute("FLUSH PRIVILEGES;")
        
        print("MySQL users and permissions have been set up.")
        cur.close()
        conn.close()

def install_dependencies():
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def run_django_commands():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
    import django
    django.setup()
    from django.core.management import call_command
    call_command('makemigrations')
    call_command('migrate')
    call_command('setup_roles')

def create_django_users():
    from django.contrib.auth.models import User, Group
    from django.conf import settings

    dbadmin_group = Group.objects.get(name='dbadmin')
    manager_group = Group.objects.get(name='manager')
    employee_group = Group.objects.get(name='employee')

    dbadmin_user = User.objects.create_user(username='dbadmin_user', password='password')
    dbadmin_user.groups.add(dbadmin_group)
    dbadmin_user.save()

    manager_user = User.objects.create_user(username='manager_user', password='password')
    manager_user.groups.add(manager_group)
    manager_user.save()

    employee_user = User.objects.create_user(username='employee_user', password='password')
    employee_user.groups.add(employee_group)
    employee_user.save()

    print("Django users have been created and assigned to groups.")

def main():
    print("Installing dependencies...")
    install_dependencies()

    print("Setting up MySQL users and permissions...")
    create_mysql_users()

    print("Running Django migrations and setting up roles...")
    run_django_commands()

    print("Creating Django users...")
    create_django_users()

    print("Setup complete!")

if __name__ == '__main__':
    main()
