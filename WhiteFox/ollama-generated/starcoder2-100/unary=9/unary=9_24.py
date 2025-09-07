
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 5
        v2 = torch.clamp_min(v1, -6).clamp_max(0, 9).div(4.)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1,3,8,7)
__output__  = m(x1)

