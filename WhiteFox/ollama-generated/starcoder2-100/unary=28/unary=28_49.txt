
class Model(torch.nn.Module):
    def __init__(self, minval = -50., maxval=20.).
        super().__init__()
        self.linear  = torch.nn.Linear(..., ...)

    def forward(self, x1):
       v1 = self.linear(x1)
       v2 = torch.clamp_min(v1, minval)
       v3 = torch.clamp_max(v2, maxval)
       return v3

# Initializing the model and providing keyword arguments as necessary
m  = Model() # Call the model without providing the keyword arguments
m  = Model(50., 70.) # Provide values for minval and maxval using keyword arguments.

# Inputs to the model with the provided keyword arguments
x1 = torch.randn(1, ...)

