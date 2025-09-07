
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=1000):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1  * 0.5
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (v2 + v5) / 2
        return v6


# Initializing the model
m = Model(max_value=100)


