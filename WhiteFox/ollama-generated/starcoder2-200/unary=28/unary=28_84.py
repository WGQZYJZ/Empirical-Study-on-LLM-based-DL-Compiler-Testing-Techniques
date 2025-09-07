
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(in_features=3, out_features=8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -10.)
        v3  = torch.clamp_max(v2,  5.)
        return v3


# Initializing the model