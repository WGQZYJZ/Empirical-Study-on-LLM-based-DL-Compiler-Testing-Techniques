
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 16)
        self.key = torch.nn.Linear(8, 16)
        self.value = torch.nn.Linear(16, 16)

    def forward(self, x):
        qk = torch.matmul(x, self.key.t()).div(1e-6 + self.key.pow(2).sum(dim=1).pow(0.5))
        v = torch.matmul(qk, self.value.t())
        return torch.nn.functional.softmax(v, dim=-1) * x


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(100, 5, 64, 64)
