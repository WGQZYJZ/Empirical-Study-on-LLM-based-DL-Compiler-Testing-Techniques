
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, 8, stride=4)
        self.transpose = torch.nn.ConvTranspose2d(32, 8, 1, stride=1)
 
    def forward(self, x):
        v = self.conv(x)
        return self.transpose(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 32, 64, 64)
