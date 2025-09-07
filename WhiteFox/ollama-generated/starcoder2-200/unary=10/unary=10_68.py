
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1  = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        v0 = self.l1(x)
        v1  = v0 + 3
        v2  = torch.clamp_min(v1, 0)
        v4  = torch.clamp_max(v2, 6)
        v5  = v4 / 6

# Initializing the model