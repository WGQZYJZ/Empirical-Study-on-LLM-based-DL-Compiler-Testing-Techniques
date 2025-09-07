
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 30, 50)
