
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 10)

    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 * F.clamp(min=0, max=6, input=v1 + 3) / 6
        return v2


# Initializing the model
m = Model()


# Inputs to the model