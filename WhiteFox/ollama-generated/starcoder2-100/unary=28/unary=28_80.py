

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=-5) # clamped to -5 
        v3  = torch.clamp_max(v2, max=50) # clamped to 50
        return v3

# Initializing the model
m = Model()

