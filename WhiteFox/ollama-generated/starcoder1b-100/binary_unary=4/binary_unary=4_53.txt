
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 256)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v3 + other


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 1024)
