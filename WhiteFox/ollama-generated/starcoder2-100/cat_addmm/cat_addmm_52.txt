
class Model(torch.nn.Module):
    def __init__(self, inplanes = 3, outplanes = 8):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(inplanes, outplanes, 1)
 
    def forward(self, input):
        v1  = torch.addmm(input, mat1, mat2)
        v2  = torch.cat([v1], 3)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, inplanes, 64, 64)
__output__  = m(x1)


