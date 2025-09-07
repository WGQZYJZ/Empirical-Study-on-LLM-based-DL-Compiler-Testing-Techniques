
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)
 
    def forward(self, x):
        v0 = self.linear(x) > 0
        v1 = self.linear(x) * negative_slope
        v2 = torch.where(v0, v0, v1)
        return v2


# Initializing the model
m = Model()
negative_slope = 1e-3


# Inputs to the model: (for example) [[-1], [1]] and [[]] 
# If inputs are not provided, the default values will be used.

 # 