
class Model(torch.nn.Module):
    def __init__(self, min_value=-2., max_value=0.8):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 5)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=min_value) # clamp the value of v1 to a minimum value specified by min_value 
        v3 = torch.clamp_max(v2, max=max_value)# clamp the value of v2 to a maximum value specified by max_value
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 572, 584)

__output__  = m(x1)