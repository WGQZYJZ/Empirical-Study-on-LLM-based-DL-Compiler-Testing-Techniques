
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @property
    def config(self):
        return Config(...)  # A configuration object of the model

    def forward(self, x1):
        return ...  # Forward propagation to compute y2


# Initializing the model
m = Model()


