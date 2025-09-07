
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.tanh(v1) 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4096, 875, 875)
__output__= m(x1)

