
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, min_) # clamp the minimum value in v1 to a given threshold
        v3  = torch.clamp_max(v2, max_) # clamp the maximum value of v2 to another given threshold 
        return v3

# Initializing the model with minimum and maximum value 0.5 as keyword arguments
m  = Model(min_=0.5, max_=0.8)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
