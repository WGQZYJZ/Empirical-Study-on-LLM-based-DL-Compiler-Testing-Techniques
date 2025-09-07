class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
 
        self.inp = torch.ones(n)
 
    def forward(self, x1):
        v1  = torch.mm(x1, x1) 
        v2  = v1 + self.inp 
        return v2
