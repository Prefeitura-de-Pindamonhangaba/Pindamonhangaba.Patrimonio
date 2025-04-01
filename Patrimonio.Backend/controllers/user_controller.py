from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User, Base
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

user_bp = Blueprint('user', __name__)

# Configuração do banco de dados
DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_NAME = os.getenv('DB_NAME')
DATABASE_USER = os.getenv('DB_USER')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')

# Criar engine e sessão
engine = create_engine(f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@user_bp.route('/users', methods=['GET'])
def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return jsonify([user.to_dict() for user in users])
    finally:
        db.close()

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    db = SessionLocal()
    try:
        user = db.query(User).get(id)
        if not user:
            return jsonify({'message': 'Usuário não encontrado'}), 404
        return jsonify(user.to_dict())
    finally:
        db.close()

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password') or not data.get('name'):
        return jsonify({'message': 'Email, senha e nome são obrigatórios'}), 400
        
    db = SessionLocal()
    try:
        if db.query(User).filter_by(email=data['email']).first():
            return jsonify({'message': 'Email já cadastrado'}), 400
            
        user = User(
            email=data['email'],
            name=data['name'],
            passwordHash=generate_password_hash(data['password']),
            active=data.get('active', True)
        )
        
        db.add(user)
        db.commit()
        
        return jsonify(user.to_dict()), 201
    finally:
        db.close()

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    
    if not data:
        return jsonify({'message': 'Nenhum dado fornecido para atualização'}), 400
        
    db = SessionLocal()
    try:
        user = db.query(User).get(id)
        print(user.email)
        print(data['email'])
        if not user:
            return jsonify({'message': 'Usuário não encontrado'}), 404
            
        if data.get('email') and data['email'] != user.email:
            if db.query(User).filter_by(email=data['email']).first():
                return jsonify({'message': 'Email já cadastrado'}), 400
            user.email = data['email']
            
        if data.get('name'):
            user.name = data['name']
            
        if data.get('password'):
            user.passwordHash = generate_password_hash(data['password'])
            
        if 'active' in data:
            user.active = data['active']
            
        db.commit()
        
        return jsonify(user.to_dict())
    finally:
        db.close()

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    db = SessionLocal()
    try:
        user = db.query(User).get(id)
        if not user:
            return jsonify({'message': 'Usuário não encontrado'}), 404
            
        db.delete(user)
        db.commit()
        
        return jsonify({'message': 'Usuário removido com sucesso'})
    finally:
        db.close() 