from app import db

from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Category(db.Model):
    __tablename__='category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name= Column(String(50),nullable=False, unique=True)


class Product(db.Model):

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer , ForeignKey(Category.id), nullable=False)


if __name__=='__main__':
    from app import app
    with app.app_context():
        # c1=Category(name='Mobile')
        # c2=Category(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='Iphone 15', price=30000, category_id=1, image= "https://tcct.aicmscdn.net/tcct-media/23/9/12/iphone-15-pro-max_64ffced304ab9.png" )
        p2 = Product(name='Iphone 15', price=30000, category_id=2, image="https://p2-ofp.static.pub/ShareResource/na/subseries/hero/lenovo-slim-7i-14inch.png")
        p3 = Product(name='Iphone 15', price=30000, category_id=3, image="https://p2-ofp.static.pub/fes/cms/2023/02/22/pkhjbh23c7sjfxf76k6e6usevy3ixi851221.png")
        p4 = Product(name='Iphone 15', price=30000, category_id=4, image="https://shoppingaz.vn/wp-content/uploads/2022/03/loa-bluetooth-harman-kardon-onyx-studio-5.jpg")
        db.session.add_all([p1,p2,p3,p4])
        db.session.commit()

      # db.create_all()

