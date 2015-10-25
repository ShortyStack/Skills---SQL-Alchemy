"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
1. Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
2. Model.query.filter_by(name = 'Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
3. Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
4. Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
5. Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
6. Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands with that are either discontinued or founded before 1950.
7. Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued == None)).all()

# Get any model whose brand_name is not Chevrolet.
    Model.query.filter(Model.brand_name.isnot('Chevrolet')).all()

   

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    # Fill in get_model_info so that it takes a year as input, and prints each 
    # model’s name, brand_name and brand headquarters for each car model from that year.
    vehicles = Model.query.filter_by(year=year)
    for vehicle in vehicles:
        print vehicle.name, vehicle.brand_name, vehicle.brand_relationship.headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    print"Querying database"
    brands_query = Model.query.all()

    brands_list = []
    for brand in brands_query:
        brands_list.append(brand.brand_name)
    unique_brands_list = set(brands_list)

    for brand in unique_brands_list:
        print "Brand: {}".format(brand.encode('utf-8')
        for model in brands_query:
            if model.brand_name == brand:
                print "    Model: {} ({})".format(model.name,
                                                      model.year)


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# My Answer = 
# >>> answer = Brand.query.filter_by(name='Ford')
# >>> type(answer)
# <class 'flask_sqlalchemy.BaseQuery'>

#My Answer = Returned Value: This will return all vehicles that are the brand name Ford

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# My Answer: 
# An association table is one that links one table to another. There is no new 
# data presented in that table.
# It is just a way for one to reach through from one table to another. 
# An association table manages foreign keys 


