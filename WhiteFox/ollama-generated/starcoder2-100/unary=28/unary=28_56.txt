
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(24, 36)
    
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.clamp_min(v1, -500.)
        v3 = torch.clamp_max(v2, 8999.)
        return v3


# Initializing the model and setting the minimum and maximum values for clamping
m = Model()
minval = -500.
maxval = 174.

# Inputs to the model
x1 = torch.randn(1, 24)
__output__  = m(x1)

