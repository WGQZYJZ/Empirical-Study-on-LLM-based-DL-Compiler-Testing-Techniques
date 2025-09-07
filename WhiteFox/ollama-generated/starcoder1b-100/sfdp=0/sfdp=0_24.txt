
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.scaled_dot_product(x1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        v4 = v3 * v1
        v5 = v4 * v3
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
