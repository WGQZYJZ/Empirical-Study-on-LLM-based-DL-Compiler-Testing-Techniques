
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)

    def forward(self, x1):
        v1 = self.linear(x1) - 1
        return v1


# Initializing the model
m = Model()


