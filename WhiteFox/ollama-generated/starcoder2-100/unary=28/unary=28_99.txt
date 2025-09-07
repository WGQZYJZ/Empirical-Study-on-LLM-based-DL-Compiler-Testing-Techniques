
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(24, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=-3.) # minimum value is -3.
        v3  = torch.clamp_max(v2, max=3.) # maximum value is 3.
        return v3

# Initializing the model