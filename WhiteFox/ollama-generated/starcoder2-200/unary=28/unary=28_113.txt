
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = linear(x1)
        v2  = torch.clamp_min(v1, -4096)
        v3  = torch.clamp_max(v2, 4096)
        return v3


# Initializing the model