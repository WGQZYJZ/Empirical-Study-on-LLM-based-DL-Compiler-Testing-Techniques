
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.conv(x1) * 0.7071067811865476
        v3  = torch.erf(v2) + 1
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)



