
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=0)
 
    def forward(self, x):
        v = self.conv(x)
        v = sigmoid(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 3, 64, 64)
