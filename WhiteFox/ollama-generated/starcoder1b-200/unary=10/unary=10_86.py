
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 2)

    def forward(self, x1):
        v1 = self.linear(x1) + 3
        return torch.clamp_min(v1, 0), torch.clamp_max(v1, 6), v1 / 6


# Initializing the model
m = Model()
x1 = torch.randn(1, 4, dtype=torch.float)
__output__, ___, __output___ = m(x1)


