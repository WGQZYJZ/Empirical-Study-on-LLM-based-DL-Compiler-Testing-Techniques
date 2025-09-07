
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(10, 5, 5)
 
    def forward(self, x1):
        return self.conv(x1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 10, 28, 28)
