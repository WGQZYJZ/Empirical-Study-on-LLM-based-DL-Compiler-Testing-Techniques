
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
__x1__  = torch.randn(4096,3,7,7)
__output__  = m(__x1__)

