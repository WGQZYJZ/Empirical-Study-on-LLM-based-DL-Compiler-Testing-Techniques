
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp=None):
        v1 = torch.mm(x1, x2)
        if inp is None:
            v2 = 0.5 * v1 + 1
        else:
            v2 = (v1 + 3) * inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
