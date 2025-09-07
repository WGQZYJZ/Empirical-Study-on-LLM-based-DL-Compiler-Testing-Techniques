
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(x1, 0.2)
        v2 = torch.nn.functional.dropout(v1, 0.5)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
