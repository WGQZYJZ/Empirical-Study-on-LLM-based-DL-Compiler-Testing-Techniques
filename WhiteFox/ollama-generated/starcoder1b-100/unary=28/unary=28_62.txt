
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        clamp_min_v2 = torch.clamp_min(v1, min_value)
        clamp_max_v3 = torch.clamp_max(clamp_min_v2, max_value)
        return clamp_max_v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
