

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 160)
    
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1 + 3, min=0, max=None).div(6)
        return v2
