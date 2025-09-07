
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1  # No need to do an actual computation on this line
        v3 = v2  # No need to perform the operation here
        v4 = v3  # No need to perform the operation on this variable
        v5 = torch.clamp_min(v4, min_value)
        v6 = torch.clamp_max(v5, max_value)
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
