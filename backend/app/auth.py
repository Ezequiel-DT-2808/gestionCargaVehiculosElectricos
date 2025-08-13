from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users = {
    "admin": {"username": "admin", "password": "admin123"}
}

def authenticate_user(username: str, password: str):
    print(f"🔐 Intento de login - Usuario: {username}")
    user = fake_users.get(username)
    if not user:
        print(f"❌ Usuario '{username}' no encontrado")
        return False
    if user["password"] != password:
        print(f"❌ Contraseña incorrecta para usuario '{username}'")
        return False
    print(f"✅ Login exitoso para usuario '{username}'")
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido: falta username")
        return username
    except JWTError as e:
        print(f"❌ Error JWT: {e}")
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
