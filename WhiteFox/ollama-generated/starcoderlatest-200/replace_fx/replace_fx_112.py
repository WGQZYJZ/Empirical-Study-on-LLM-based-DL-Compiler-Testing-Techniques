
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.25, True)
        v2 = torch.rand_like(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 64, 32, dtype=torch.float)
