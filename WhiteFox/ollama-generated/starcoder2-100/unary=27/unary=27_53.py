
class Model(torch.nn.Module):
    def __init__(self, minval=-10, maxval=10):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, minval=(-10)) 
        v3  = torch.clamp_max(v2, maxval=(10)) # Change max_value to 10 and min_value to -10 for this model example
        return v3


# Initializing the model with default values for minimum and maximum values
m  = Model()

# Inputs to the model using default values (-10, 10)
x1 = torch.randn(256, 3, 48, 48)
