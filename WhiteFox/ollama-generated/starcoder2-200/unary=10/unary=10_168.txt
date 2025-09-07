
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + 3  
        v3  = F.relu6(v2)  
        return v3 / 6
 
