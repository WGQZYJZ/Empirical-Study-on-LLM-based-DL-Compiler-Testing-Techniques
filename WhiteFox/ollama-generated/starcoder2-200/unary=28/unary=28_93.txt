
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(32* 64 * 64 + 8, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.) # 1
        v3 = torch.clamp_max(v2, max=1.) # 5
        return v3
