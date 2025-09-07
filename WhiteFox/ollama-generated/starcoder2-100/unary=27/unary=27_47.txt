
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x): 
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min_value=-4.)
        v3  = torch.clamp_max(v2, max_value=50.) # clamp the output of the convolution to a maximum value
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
