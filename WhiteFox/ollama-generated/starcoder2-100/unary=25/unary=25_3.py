
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v4 = v1 * negative_slope = 1.5789
        v5 = torch.where(v2, v3, v4)

        return v5

