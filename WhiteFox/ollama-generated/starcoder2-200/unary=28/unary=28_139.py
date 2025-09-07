
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=512):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.clamp_min(v1, min_value)
        v3  = torch.clamp_max(v2, max_value)
