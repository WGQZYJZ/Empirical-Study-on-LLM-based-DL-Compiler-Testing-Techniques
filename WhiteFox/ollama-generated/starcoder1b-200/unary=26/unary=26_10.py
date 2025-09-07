
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v2 = self.conv(x2) > 0
        v3 = -v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(3, 8, 64, 64)
