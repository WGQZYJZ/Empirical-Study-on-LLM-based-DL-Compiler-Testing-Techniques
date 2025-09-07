
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 14, 6)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = v1 > 0
        v3  = -v1 * (1 - v2).float()
        v4  = torch.where(v2 == True, v1, v3)    
        return v4

m  = Model()

