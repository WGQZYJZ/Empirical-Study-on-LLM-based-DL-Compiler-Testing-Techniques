
class Model(torch.nn.Module):
    def __init__(self, min_value=100., max_value=-256.):
        super().__init__()
        self.linear  = torch.nn.Linear(37, 48)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=100.)
        v3  = torch.clamp_max(v2, max=-256.)
        return v3
