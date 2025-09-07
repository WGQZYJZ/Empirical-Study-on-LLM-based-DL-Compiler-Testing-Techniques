class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 3)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v8  = v7 + 3
        v9  = torch.clamp_min(v8, 0) 
        v10 = torch.clamp_max(v9, 6)
        return v10 / 6
