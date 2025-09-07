
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=10):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28 + 3, 45)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, min_value=0) # Clamp the output of the linear transformation to a minimum value
        v3 = torch.clamp_max(v2, max_value=10)# Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model with values for keyword arguments:
min  = 5 # Minimum value
max  = -78 # Maximum value

m  = Model(
    min_value=min, max_value=max)
# Inputs to the model. This tensor will produce an output with the specified clamped values.
x1  = torch.randn(4096, 3) * 57 - 28


__output__  = m(x1)


