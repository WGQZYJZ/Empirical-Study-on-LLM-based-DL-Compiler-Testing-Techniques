
class Model(torch.nn.Module):
    def __init__(self, minv=1024, maxv=512):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,kernelSize=7)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=1024)
        v3  = torch.clamp_max(v2, max=512)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

