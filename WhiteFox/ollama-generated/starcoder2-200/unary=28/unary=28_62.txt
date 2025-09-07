
class Model(torch.nn.Module):
    def __init__(self, max_value=None, min_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -0.75 if not hasattr(max_value, 'max') else max_value(-0.75)) # Add negative clamp
        v3  = torch.clamp_max(v2, +0.75 if not hasattr(min_value, 'max') else min_value(+0.75))
        return v3
# Initializing the model