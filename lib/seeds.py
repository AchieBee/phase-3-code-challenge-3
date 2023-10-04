from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review  # Import your model classes here

# Create an SQLAlchemy engine and session
engine = create_engine("sqlite:///seeds.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Add data to the session
session.add_all([restaurant1, restaurant2, customer1, customer2])

# Commit the changes to the database
session.commit()

# Close the session to release resources
session.close()
