
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        return torch.tanh(v1)


m  = Model()
x  = torch.randn(64, 3, 50, 50)
output  = m(x)

# Initializing the model