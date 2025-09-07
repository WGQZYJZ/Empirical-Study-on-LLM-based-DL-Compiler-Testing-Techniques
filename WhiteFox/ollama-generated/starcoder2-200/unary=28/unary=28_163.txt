
class Model(torch.nn.Module):
    def __init__(self, min_value=-10., max_value=20.):
        super().__init__()
        self.linear = torch.nn.Linear(3*64*64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=max_value) # The min value is 10 in this example, the max value should be provided as an argument to the clamp function
        v3 = torch.clamp_max(v2, max_value=-5.)  # The max value is -4 in this example, the min value should be provided as an argument to the clamp function
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3*64*64)
