
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = self.conv(x1)
        v2 = torch.mm(v1,inp) + inp
        return v6


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(8000, 3, 64, 64) # A random tensor whose shape is (batch_size, channel, width, height)
x1 = torch.randn(1, 3, 64, 64)
