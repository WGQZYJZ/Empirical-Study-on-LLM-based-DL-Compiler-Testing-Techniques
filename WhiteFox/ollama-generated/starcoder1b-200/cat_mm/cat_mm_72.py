
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.mm(x1, x1) + 3*x1 + 4*x2


# Initializing the model
m = Model()


