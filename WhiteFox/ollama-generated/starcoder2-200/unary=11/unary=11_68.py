
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # pointwise transposed convolution
        v2  = v1 + 3 # addition by 3
        v3  = torch.clamp_min(v2, 0) # clamping at a minimum of 0 
        v4  = torch.clamp_max(v3, 6) # clamping at a maximum of 6
        v5  = v4 / 6 # division by 6
        return v5


# Initializing the model
m = Model()


