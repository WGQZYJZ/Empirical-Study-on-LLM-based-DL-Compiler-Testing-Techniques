
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -7368)
        v3 = torch.clamp_max(v2, 99980) # The minimum and maximum values are provided as keyword arguments.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5678, 42, 1024) # Keyword argument for minimum value: -7368, Keyword argument for maximum value: 99980
__output__  = m(x1)

