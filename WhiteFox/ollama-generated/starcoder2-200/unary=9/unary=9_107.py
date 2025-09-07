
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3            # Add 3 to the output of the convolution 
        v4  = torch.clamp_min(v2, 0)   # Clamp the output of the addition operation to a minimum of `0`
        v5  = torch.clamp_max(v4, 6)   # Clamp the output of the previous operation to a maximum of `6` 
        v3  = v5 / 6              # Divide the output of the previous operation by `6`
        return v3


# Initializing model
m  = Model()


# Inputs for the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
