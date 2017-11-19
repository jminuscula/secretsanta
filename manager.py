
from .pairs import CircularRandomPairer
from .sender import EmailSender, ConsoleSender


class SecretSantaManager:

    def __init__(self, participants, seed, **kwargs):
        super().__init__(**kwargs)
        self.participants = participants
        self.seed = seed

    def run(self):
        pairs = self.get_pairs(self.participants, self.seed)
        for secret_from, secret_to in pairs:
            message = self.format_message(secret_from, secret_to)
            self.send(secret_from, secret_to, message)


class SecretSantaDefaultManager(SecretSantaManager, CircularRandomPairer, EmailSender):
    pass


class SecretSantaDebugManager(SecretSantaManager, CircularRandomPairer, ConsoleSender):
    pass
