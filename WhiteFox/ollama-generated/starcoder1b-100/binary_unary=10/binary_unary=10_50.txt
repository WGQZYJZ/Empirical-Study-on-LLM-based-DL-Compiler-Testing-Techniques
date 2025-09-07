
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48, 32)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()


