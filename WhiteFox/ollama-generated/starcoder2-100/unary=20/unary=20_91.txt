
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(8, 3, kernel_size=7)
 
    def forward(self, x0):
        v0  = self.conv1(x0)
        v1  = torch.sigmoid(v0)
        return v1

# Initializing the model
m  = Model()
 
# Inputs to the model
x0  = torch.randn(32, 8, 64, 64)
__output__  = m(x0)

