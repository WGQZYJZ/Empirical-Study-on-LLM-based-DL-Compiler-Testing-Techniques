
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=1)
        return v3


# Initializing the model with arguments as minimum and maximum values of clamping
m = Model(min_value=0, max_value=1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
