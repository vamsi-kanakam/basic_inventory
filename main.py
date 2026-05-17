from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

products=[
    Product(id=1, name='Laptop', description='A high-performance laptop', price=999.99, quantity=10),
    Product(id=2, name='Smartphone', description='A latest model smartphone', price=499.99, quantity=20),
    Product(id=3, name='Headphones', description='Noise-cancelling headphones', price=199.99, quantity=15),
    Product(id=4, name='Smartwatch', description='A smartwatch with various features', price=299.99, quantity=5),
    Product(id=5, name='Tablet', description='A lightweight tablet for work and play', price=399.99, quantity=8)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def db_init():
    db = session()
    count=db.query(database_models.Product).count
    
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

db_init() 

@app.get('/products')
async def get_all_products(db:Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get('/products/{id}')
async def get_product_by_id(id: int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return {'message': 'Product not found'}

@app.post('/product')
async def add_prodcut(product: Product, db:Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return {'message': 'Product added successfully'}

@app.put('/product')
async def update_product(id:int, product: Product,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return {'message': 'Product Updated Sucessfully'}
    return {'message': 'Product not found'}

@app.delete('/product/{id}')
async def delete_product(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {'message': 'Product deleted Sucessfully'}
    return {'message': 'Product not found'}
 