
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x):
        v0 = x  # Copy input tensor
        v1  = self.conv(v0)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2,0) # clamp to a minimum of 0
        v4  = torch.clamp_max(v3,6) # Clamp the previous output operation to a maximum of 6
        v5  = v4 / 6 # Divide the previous operation by 6
        return v5


# Initializing the model
m = Model()
 
# Inputs for the model
x1 = torch.randn(1,3,64,64)
__output__  = m(x1)
 
