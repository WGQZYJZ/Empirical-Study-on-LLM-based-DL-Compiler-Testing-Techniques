
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.upsample = torch.nn.Upsample(scale_factor=2)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return self.upsample(v1) * 0.5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
