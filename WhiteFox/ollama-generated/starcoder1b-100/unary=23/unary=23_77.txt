
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4)
 
    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = torch.tanh(t1)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
