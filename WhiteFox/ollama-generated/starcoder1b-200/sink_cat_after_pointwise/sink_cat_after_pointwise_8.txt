
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model (x_1 and x_2 should be different from each other).
x_1 = torch.randn(3, 3)
x_2 = torch.randn(3, 3)
