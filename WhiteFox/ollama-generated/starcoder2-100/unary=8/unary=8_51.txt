
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = torch.clamp(v1, min=0, max=6)
        v3  = v2 * v2 
        return v4


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


