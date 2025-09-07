
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x) + 3
        v2  = torch.clamp_min(v1, 0)
        v3  = torch.clamp_max(v2, 6)
        v4  = v3 / 6 
        return v4
 
# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x)

