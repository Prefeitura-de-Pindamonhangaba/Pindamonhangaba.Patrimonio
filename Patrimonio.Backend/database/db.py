import psycopg2
from flask import current_app

def get_db():
    """Retorna uma conexão com o banco de dados PostgreSQL."""
    if 'db' not in current_app.config:
        try:
            current_app.config['db'] = psycopg2.connect(
                host=current_app.config['DATABASE_HOST'],
                database=current_app.config['DATABASE_NAME'],
                user=current_app.config['DATABASE_USER'],
                password=current_app.config['DATABASE_PASSWORD']
            )
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
    return current_app.config['db']

def close_db(e=None):
    """Fecha a conexão com o banco de dados se existir."""
    db = current_app.config.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """Inicializa a extensão do banco de dados com a aplicação Flask."""
    app.teardown_appcontext(close_db)

def execute_query(query, params=()):
    """Executa uma consulta SQL e retorna os resultados."""
    conn = get_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor
        except psycopg2.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()
    return None

def fetch_one(query, params=()):
    """Executa uma consulta SQL e retorna o primeiro resultado."""
    cursor = execute_query(query, params)
    if cursor:
        return cursor.fetchone()
    return None

def fetch_all(query, params=()):
    """Executa uma consulta SQL e retorna todos os resultados."""
    cursor = execute_query(query, params)
    if cursor:
        return cursor.fetchall()
    return None