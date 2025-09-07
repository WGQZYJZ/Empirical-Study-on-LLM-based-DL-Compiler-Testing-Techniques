
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 64)
    
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, min=5) # Min clamping value set to 5 for the output of the linear transformation
        v3  = torch.clamp_max(v2, max=40) # Max clamping value set to 40 for the output of the previous operation 
        return v3

# Initializing the model