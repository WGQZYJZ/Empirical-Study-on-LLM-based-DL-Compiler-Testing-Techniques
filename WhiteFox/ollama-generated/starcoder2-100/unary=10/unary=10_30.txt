
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v2  = self.conv(x1)
        v4  = v2 + 3 
        v5  = torch.clamp_min(v4, 0 )
        v6  = torch.clamp_max(v5, 6)
        v7  = v6 / 6 
        return v7


# Initializing the model