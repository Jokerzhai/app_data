from ..spawncase import SpawnCase


class Case(SpawnCase):
    def __init__(self):
        super(Case, self).__init__()
        self.enabled = False

    