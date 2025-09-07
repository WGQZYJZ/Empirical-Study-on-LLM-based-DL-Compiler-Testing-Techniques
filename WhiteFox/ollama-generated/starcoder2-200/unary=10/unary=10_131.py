
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 2)
 
    def forward(self, x1): 
        v1 = self.linear(x1)        
        v3 = v1 + 3
        v4 = torch.clamp_min(v3,0)
        v5 = torch.clamp_max(v4,6)
        v6 = v5/6
        return v6

m = Model()

