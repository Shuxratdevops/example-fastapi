from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # parolni heshlash

def hash(password: str): # parolni heshlaydi
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):# verify 2 ta malumotni tengligini solishtiradi
    return pwd_context.verify(plain_password, hashed_password)

