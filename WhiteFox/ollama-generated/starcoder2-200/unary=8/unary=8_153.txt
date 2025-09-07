
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 184, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + 3 
        v3 = torch.clamp(v2, min=0, max=6 ) # Clamp the output of the addition operation to a minimum of 0 and a maximum of 6 
        v4 = v1 * v3 # Multiply the output of the transposed convolution by the output of the clamp operation
        v5 = v4 / 6 # Divide the output of the multiplication operation by 6
        return v5

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 32)
__output__  = m(x1)

