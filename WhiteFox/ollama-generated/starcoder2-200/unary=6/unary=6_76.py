
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Add 3 to the output of the convolution
        v3  = torch.clamp_min(v2, min=0) # Clamp the result of addition operation to a minimum value of 0
        v4  = torch.clamp_max(v3, max=6) # Clamp the result of clamping operation to maximum of 6
        v5  = v1 * v4 
        return v5 / 6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
