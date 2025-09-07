
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.mm(v1, v1)
        v3 = v2 + 0.5 * torch.mm(v1, x1)
        return v3
 
