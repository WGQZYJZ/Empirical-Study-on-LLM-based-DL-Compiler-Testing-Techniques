
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, ...)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
