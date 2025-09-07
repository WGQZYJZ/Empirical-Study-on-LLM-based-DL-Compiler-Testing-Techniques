
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(32, 8, 1)
 
    def forward(self, x1):
        v0  = self.conv(x1) 
        v4  = torch.sigmoid(v0)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(32, 8, 64, 64)
__output__  = m(x1)


