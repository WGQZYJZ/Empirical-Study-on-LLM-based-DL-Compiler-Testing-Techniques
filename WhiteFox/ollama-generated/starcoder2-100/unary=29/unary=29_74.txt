
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.min   = 0
        self.max   = 5
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=self.min)
        v3  = torch.clamp_max(v2, max_value=self.max)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

