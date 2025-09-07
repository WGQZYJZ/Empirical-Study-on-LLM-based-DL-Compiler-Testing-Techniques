
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2 = v1.permute(0, 3, 1, 2)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 4, 5, 2)
__output__  = m(x1)