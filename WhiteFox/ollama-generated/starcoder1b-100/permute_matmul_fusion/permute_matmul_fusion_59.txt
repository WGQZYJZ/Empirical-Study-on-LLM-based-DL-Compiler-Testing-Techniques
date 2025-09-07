
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.abs_(x1)
        v2 = torch.pow(v1, 2.)
        return v2


# Initializing the model
m = Model()


