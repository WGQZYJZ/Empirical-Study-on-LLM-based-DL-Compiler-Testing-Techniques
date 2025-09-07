
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=5.0):
        super().__init__()
        self.linear  = torch.nn.Linear(4 * 64 * 32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1))
        v2  = v1.clamp_min(0.5, max=min_value) # clamp_max is not used here because the minimum value must be specified as an argument to the constructor of the model. This model assumes that min_value will be less than or equal to max_value.
        v3  = torch.clamp(v2, max=50) # Clamp maximum value is a hard-coded constant which would not be possible if it was an input. 
        return v3


# Initializing the model with min and max values as keyword arguments
m  = Model(min_value=-10.78945, max_value=23)
 
# Inputs to the model
x1 = torch.randn(32, 4 * 64 * 32)


