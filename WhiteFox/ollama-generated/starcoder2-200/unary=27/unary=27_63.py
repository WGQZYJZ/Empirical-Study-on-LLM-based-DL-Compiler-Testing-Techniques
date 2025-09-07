
class Model(torch.nn.Module):
    def __init__(self, minv=0.5, maxv=1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5) 
        v3  = torch.clamp_max(v2, max=1) # Add code here
        return v3


# Initializing the model with customized values for the minimum and maximum values
m  = Model(minv=2, maxv=4)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

