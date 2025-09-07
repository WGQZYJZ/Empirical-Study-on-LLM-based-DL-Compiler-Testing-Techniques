
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(32, 10, 5)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = v1.clamp(min=0).clamp_max(6)
        v3  = v2 / 6
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 32, 80, 94)
