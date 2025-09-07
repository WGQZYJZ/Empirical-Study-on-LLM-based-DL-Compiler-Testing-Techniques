
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3, 8, 4)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(32, 8, 4, 4)
__output__  = m(x1)
 
