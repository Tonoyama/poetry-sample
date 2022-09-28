from fastapi import APIRouter
router = APIRouter()


@router.get('/post')
def post():
    return {'users': ['a', 'b', 'c']}
