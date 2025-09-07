
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v2  = self.linear(x1)
        v3  = v2 + 3
        v4  = torch.clamp_min(v3, 0)
        v6  = torch.clamp_max(v4, 5)
        v7  = v6 / 6
 
        return v7


# Initializing the model