
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=255.):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.clamp_min = torch.nn.ClampMin(min_value)
        self.clamp_max = torch.nn.ClampMax(max_value)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.clamp_min(v1)
        v3 = self.clamp_max(v2)
        return v3


# Initializing the model
m = Model()


