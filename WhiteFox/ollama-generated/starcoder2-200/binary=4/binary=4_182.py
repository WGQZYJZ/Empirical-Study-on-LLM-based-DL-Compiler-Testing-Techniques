class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 8)
    
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 + torch.randn_like(v1) # this is a model example that has the same pattern as the previous one
        return v2
