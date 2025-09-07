
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_a = torch.nn.Linear(2, 3)
        self.linear_b = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear_a(v1)
        v3 = self.linear_b(x1)
        return torch.cat([v2, v3], dim=2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
