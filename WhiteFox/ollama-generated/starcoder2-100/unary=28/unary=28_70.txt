
class Model(torch.nn.Module):
    def __init__(self, max_value=10, min_value=-5)
        super().__init__()
        self.linear = torch.nn.Linear()

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_value) 
        v3  = torch.clamp_max(v2, max_value)
        return v3

# Initializing the model with default values for minimum and maximum.
m0 = Model()

