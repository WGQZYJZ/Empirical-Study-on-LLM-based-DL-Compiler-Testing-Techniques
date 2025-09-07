
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2): 
        v0 = torch.cat([x1] * 5 + [y2])
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 6)
y2  = torch.randn(4, 8)
__output__  = m(x1, y2)
