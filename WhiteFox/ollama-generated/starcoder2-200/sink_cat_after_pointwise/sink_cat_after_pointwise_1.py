
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)
        v = v.view(-1, 3, 5, 7).relu()
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5, 6)
x2 = torch.randn(8, 9)
__output__  = m(x1, x2)