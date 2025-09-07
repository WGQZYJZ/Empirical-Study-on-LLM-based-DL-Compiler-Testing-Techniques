
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x):
        v = self.conv(x)
        return torch.sigmoid(v)


# Initializing the model
m = Model()
x = m(torch.randn(2, 8, 64, 64))
