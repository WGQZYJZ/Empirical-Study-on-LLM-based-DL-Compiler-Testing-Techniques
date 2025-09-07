
class Model(torch.nn.Module):
    def __init__(self, min_value=-100.0, max_value=25.0):
        super().__init__()
        self.linear  = torch.nn.Linear(3*64*64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=min_value)
        v3  = torch.clamp_max(v2, max=max_value)
        return v3


# Initializing the model with specific values for min and max clamping bounds
m  = Model(-50.0, 10.0)

# Inputs to the model