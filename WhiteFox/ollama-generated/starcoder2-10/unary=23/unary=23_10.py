
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        return torch.tanh(self.conv(x))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4096, 576, 32, 32)
