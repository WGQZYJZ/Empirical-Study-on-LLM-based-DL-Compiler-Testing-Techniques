
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 2, 3)
        v2 = v1.permute(0, 2, 1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
__input__ = torch.randn(4, 5, 3)
__output__  = m(__input__)