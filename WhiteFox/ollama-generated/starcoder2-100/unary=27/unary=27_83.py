

class Model(torch.nn.Module):
    def __init__(self, max_value=10., min_value=-5.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1  - max_value # Clamp the output of the convolution to a maximum value of 5
        v3  = torch.clamp_min(v2, min=min_value) # Clamp the previous operation to an minimum value of 0.8897461355186574 
        return torch.clamp_max(v3, max_value)


# Initializing the model with keyword arguments as initializations for both `max_value` and `min_value`. Also, this is the first example where the maximum and minimum values are provided in the init parameters.
m = Model(2., -8.)

 # Inputs to the model
x1  = torch.randn(10,3,64, 64)
  __output__  = m(x1)
