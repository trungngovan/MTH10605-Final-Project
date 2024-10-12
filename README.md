# MTH10605-Final-Project
Do a simple project where we use AWS to create and deploy a real Machine Learning API that can be assessed anywhere in 
the world.

---

## Description
In this project, we will create a simple Machine Learning API that can be accessed from anywhere in the world. 
We will use AWS to create and deploy the API. 

The API will be a simple model that can predict the sentiment of a sentence, and then deploy the model as an 
API that can be accessed via a web interface.

## Team
1. **Ngô Văn Trung** - 21110423
2. **Đỗ Công Tuấn** - 22110250
3. **Nguyễn Văn Anh Vũ** -22110264
4. **Lê Minh Trọng** - 22110239

## Technologies
- Django
- AWS
- Machine Learning
- HTML/CSS
- MySQL

## Installation

1. Clone the repository
```bash
git clone git@github.com:trungngovan/MTH10605-Final-Project.git
```

2. Createe a virtual environment
```bash
python -m venv venv
```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Setup MySQL database (In this project, we use MySQL in a Docker container)
- Pull MySQL image
```bash
docker pull mysql
```

- Run MySQL container
```bash
docker run -d -p 3306:3306 --name mysqldb -e MYSQL_ROOT_PASSWORD=<your-database-password> mysql 
```

- Start MySQL container
```bash
docker start mysqldb
```

- Exec into MySQL container 
```bash
docker exec -it mysqldb mysql -uroot -p # After that, enter your password
```

- Create a database
```sql
CREATE DATABASE <your-database-name>;
```

5. Migrate the database
```bash
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Run the server
```bash
python manage.py runserver
```

## References
- [Django](https://www.djangoproject.com/)
- [AWS](https://aws.amazon.com/)
- [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning)
