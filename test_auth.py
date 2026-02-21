import pytest
from auth import AuthService

def test_login_success():
    """Caso de Uso 1: Validar acceso con credenciales correctas."""
    auth = AuthService()
    assert auth.login("admin", "Cert@2026") == "Success"

def test_login_wrong_password():
    """Caso de Uso 1: Validar rechazo por contraseña incorrecta."""
    auth = AuthService()
    assert auth.login("admin", "ClaveErronea") == "Failure"

def test_account_locking_after_3_attempts():
    """Caso de Uso 2: Validar bloqueo de cuenta tras 3 fallos (Seguridad)."""
    auth = AuthService()
    auth.login("admin", "error1")
    auth.login("admin", "error2")
    auth.login("admin", "error3")
    # El cuarto intento debe resultar en bloqueo, incluso si la clave es correcta
    assert auth.login("admin", "Cert@2026") == "Account Locked"