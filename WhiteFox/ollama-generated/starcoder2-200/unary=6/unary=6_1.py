

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = v1 + 3 # 3 is used to create the pattern
        v3 = torch.clamp_min(v2, 0) # Minimum of zero is used for clap operation
        v4 = torch.clamp_max(v3,6)# Maximum of six is used for clamping
        v5 = v1 * v4# Multiplication of output of convolution with output of clamp 
        v6 = v5 / 6# Division of multiplication by constant 6
        return v6

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(2,3,64,64)

