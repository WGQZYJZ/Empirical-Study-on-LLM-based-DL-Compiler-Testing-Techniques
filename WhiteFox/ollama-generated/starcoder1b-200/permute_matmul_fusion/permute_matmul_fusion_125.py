
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear_A(v1)
        v3 = self.linear_B(x2)
        return torch.cat([v2, v3], dim=-1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(2, 2, 4)
