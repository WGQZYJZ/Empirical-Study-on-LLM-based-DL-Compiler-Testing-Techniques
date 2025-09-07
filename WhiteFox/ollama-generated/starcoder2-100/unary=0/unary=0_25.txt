
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = (v1*v1)*v1 
        v4  = torch.tanh((v1+0.7978845608028654)*(v3*0.044715+v2))
        return v4 + 1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

