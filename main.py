from fastapi import FastAPI
from models import Product
app = FastAPI()


@app.get('/')
def read_root():
    return{'message':'Hello Welcome to the Page'}

products=[
    Product(id=1, name='Laptop', description='A high-performance laptop', price=999.99, quantity=10),
    Product(id=2, name='Smartphone', description='A latest model smartphone', price=499.99, quantity=20),
    Product(id=3, name='Headphones', description='Noise-cancelling headphones', price=199.99, quantity=15),
    Product(id=4, name='Smartwatch', description='A smartwatch with various features', price=299.99, quantity=5),
    Product(id=5, name='Tablet', description='A lightweight tablet for work and play', price=399.99, quantity=8)
]

@app.get('/products')
async def get_all_products():
    return products

@app.get('/products/{id}')
async def get_product_by_id(id: int) -> Product:
    for product in products:
        if product.id == id:
            return product
    
    return {'message': 'Product not found'}

@app.post('/product')
async def add_prodcut(product: Product) -> Product:
    products.append(product)
    return {'message': 'Product added successfully'}

@app.put('/product')
async def update_product(id:int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {'message': 'Product updated successfully'}
    return {'message': 'Product not found'}

@app.delete('/product/{id}')
async def delete_product(id:int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return {'message': 'Product deleted successfully'}
    return {'message': 'Product not found'}
