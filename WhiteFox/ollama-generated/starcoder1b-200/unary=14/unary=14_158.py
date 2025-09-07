
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return self.sigmoid(v1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
