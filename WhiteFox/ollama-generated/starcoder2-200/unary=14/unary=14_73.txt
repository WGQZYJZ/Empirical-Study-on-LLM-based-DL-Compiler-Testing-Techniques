
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 5, stride=2)
 
    def forward(self, x1): 
        v0  = x1 * 7.6490383E-4
        v1  = torch.sigmoid(v0 + 2.0000000000000005e-4)
        v2  = v1  *  1.9773932E+01 - 6.8940435E-01
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
__output__  = m(x1)