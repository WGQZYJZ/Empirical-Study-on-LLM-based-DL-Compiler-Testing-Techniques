
class Model(torch.nn.Module):
    def __init__(self, minval=-30., maxval=189.):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 4 + 3, 7)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, minval=-30.)
        v3 = torch.clamp_max(v2, maxval=189.)
        return v3

# Initializing the model