
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = self.conv(x1)
        return v1 + inp


# Initializing the model
m = Model()

# Inputs to the model
inp1 = torch.randn(1, 3, 64, 64)
inp2 = torch.randn(1, 8, 64, 64)
