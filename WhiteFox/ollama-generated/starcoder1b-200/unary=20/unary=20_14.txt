
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, 4, stride=2, padding=1)
 
    def forward(self, x):
        t1 = self.conv(x)
        t2 = torch.sigmoid(t1)
        return t2


# Initializing the model
m = Model()
x = torch.randn(4, 32, 50, 50)
