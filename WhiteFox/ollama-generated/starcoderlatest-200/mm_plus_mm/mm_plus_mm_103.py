
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 128)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1024, 32)
x2 = torch.randn(1024, 32)
