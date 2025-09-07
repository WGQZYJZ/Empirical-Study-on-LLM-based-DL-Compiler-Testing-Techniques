
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v0 = self.linear(x1) + 3
        v1 = torch.clamp_min(v0, 0)
        v2 = torch.clamp_max(v1, 6)
        v3 = v2 / 6
 
        return v3

# Initializing the model