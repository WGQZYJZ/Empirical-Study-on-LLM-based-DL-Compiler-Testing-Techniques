
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)

    def forward(self, x):
        v = self.linear(x) + 3
        return torch.clamp_min(v, 0), torch.clamp_max(v, 6) / 6


# Inputs to the model
__input__ = torch.randn(1, 10)
