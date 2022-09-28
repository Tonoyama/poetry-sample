from database import Product, create_session
import sys
sys.path.append("../")


def test_post():
    session = create_session()
    product = session.query(Product).all()
    assert len(product) != 0
