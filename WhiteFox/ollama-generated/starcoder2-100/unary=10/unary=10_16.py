

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(20, 3)
 
    def forward(self, x1):
        v1 = self.l1(x1)
        v2 = v1 + 3
        v3 = F.relu6(v2)
        v4 = torch.clamp_max(v3, 6) # clamp max
        v5 = torch.clamp_min(v4, 0)# clamp min
        return v5 / 6

m = Model()
x1 = torch.randn(3897, 20)
