
class Model(torch.nn.Module):
    def __init__(self, maxv=0.5, minv=-1.2547839602450073):
        super().__init__()
        self.lin  = torch.nn.Linear(100, 1)
 
    def forward(self, x):
        v1  = self.lin(x)
        v2  = torch.clamp_min(v1, minv)
        v3  = torch.clamp_max(v2, maxv)
        return v3


# Initializing the model