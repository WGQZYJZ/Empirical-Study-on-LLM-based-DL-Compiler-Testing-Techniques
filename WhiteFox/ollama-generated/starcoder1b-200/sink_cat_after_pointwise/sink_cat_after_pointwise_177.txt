
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1, ...):
        v1 = ...  # Some tensor operation
        return torch.cat([v1, ...], dim=...)


# Inputs to the model
x1, x2 = torch.randn(2, 3), torch.randn(3)
