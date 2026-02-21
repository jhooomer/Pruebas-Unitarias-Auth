class AuthService:
    def __init__(self):
        # Base de datos simulada
        self.users = {"admin": "Cert@2026", "estudiante": "Unibe2026"}
        self.failed_attempts = {}

    def login(self, username, password):
        # Verificar si la cuenta está bloqueada (Contramedida de riesgo)
        if self.failed_attempts.get(username, 0) >= 3:
            return "Account Locked"
        
        if username in self.users and self.users[username] == password:
            self.failed_attempts[username] = 0
            return "Success"
        else:
            # Registrar intento fallido
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            return "Failure"