
class Model(torch.nn.Module):
    def __init__(self, config={}):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.config = config

    @classmethod
    def config(cls, config=None):
        if not hasattr(cls, '_config'):
            cls._config = config

        return cls._config

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
