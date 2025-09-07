
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_val = min_value # Minimum value of the output tensor for the clamp function
        self.max_val = max_value # Maximum value of the output tensor for the clamp function
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, self.min_val) 
        v3  = torch.clamp_max(v2, self.max_val)
        return v3


# Initializing the model with minimum value -0.5 and maximum value of 4.7938.
m = Model(-0.5, 4.7938)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)