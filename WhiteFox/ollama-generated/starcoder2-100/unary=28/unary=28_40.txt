
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.rand(24) * 3 + 5 
        v1  = torch.clamp_min(v0, min=6.8)
        v2 = torch.clamp_max(v1, max=9.7)
 
        return None


# Initializing the model
m  = Model()
