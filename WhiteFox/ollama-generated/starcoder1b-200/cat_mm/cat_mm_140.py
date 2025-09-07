
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.cat([x1, x1, ..., x1], dim=-1)


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 5, 6, dtype=torch.int64)
