
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0) # clamp the minimum of the output of the addition operation at a minimum of 0
        v4  = torch.clamp_max(v3, 6) # clamp the maximum value of the previous operation to `6`
        v5  = v4 / 6   # divide by `6`
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,3,64,64)

