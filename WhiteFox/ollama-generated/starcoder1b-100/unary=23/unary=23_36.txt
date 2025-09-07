
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(16, 32, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
