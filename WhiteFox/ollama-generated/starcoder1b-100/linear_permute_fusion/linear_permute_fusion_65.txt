
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 1)
        v2 = torch.nn.functional.linear(v1, 2)
        return v2


# Inputs to the model
x1 = torch.randn(1, 1, 2)
