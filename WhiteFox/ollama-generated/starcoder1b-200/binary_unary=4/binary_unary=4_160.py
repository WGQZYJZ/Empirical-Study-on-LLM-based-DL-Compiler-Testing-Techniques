
class Model(torch.nn.Module):
    def __init__(self, other: int=0):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32, bias=True)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = x1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
other = torch.randn(32, dtype=torch.float32)
