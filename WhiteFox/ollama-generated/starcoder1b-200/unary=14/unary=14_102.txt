
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.glu = torch.nn.GLU()
 
    def forward(self, x1):
        x2 = self.conv(x1)
        return self.glu(x2 * 0.5 + 1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
