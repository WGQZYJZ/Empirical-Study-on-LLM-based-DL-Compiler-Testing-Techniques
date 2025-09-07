
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.add  = torch.addmm
    
    def forward(self, x1, m1, m2):
         v1  = self.add(x1, m1, m2)
         v2  = torch.cat([v1], dim)
         return v2


# Initializing the model