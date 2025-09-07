
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear(30, 15)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_value) # clamped to a minimum value
        v3  = torch.clamp_max(v2, max_value) 
        return v3
# Initializing the model with custom max and min values
m = Model(-50.0, 75.0)

 # Inputs to the model
 x1  = torch.randn(64, 30)
    __output__  = m(x1)
