from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username e password são obrigatórios'}), 400
    
    db = SessionLocal()
    try:
        # Verificar se usuário já existe
        existing_user = db.query(User).filter(User.username == data['username']).first()
        if existing_user:
            return jsonify({'error': 'Usuário já existe'}), 400

        # Criar novo usuário
        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            username=data['username'],
            password_hash=hashed_password,
            name=data.get('name', ''),
            email=data.get('email', ''),
            role=data.get('role', 'user')
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return jsonify({
            'id': new_user.id,
            'username': new_user.username,
            'name': new_user.name,
            'email': new_user.email,
            'role': new_user.role,
            'createdAt': new_user.createdAt.isoformat(),
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username e password são obrigatórios'}), 400
    
    db = SessionLocal()
    try:
        # Buscar usuário
        user = db.query(User).filter(User.username == data['username']).first()
        
        # Verificar se usuário existe e a senha está correta
        if not user or not check_password_hash(user.password_hash, data['password']):
            return jsonify({'error': 'Credenciais inválidas'}), 401
        
        # Criar token JWT
        access_token = create_access_token(
            identity={
                'id': user.id,
                'username': user.username,
                'role': user.role
            },
            expires_delta=timedelta(hours=24)
        )
        
        return jsonify({
            'access_token': access_token,
            'user': {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == current_user['id']).first()
        
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        return jsonify({
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'createdAt': user.createdAt.isoformat(),
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()