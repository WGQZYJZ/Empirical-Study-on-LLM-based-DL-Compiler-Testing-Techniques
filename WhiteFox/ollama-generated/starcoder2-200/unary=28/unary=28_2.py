
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 1)
 
    def forward(self, x1): 
        v1 = self.linear(x1)    
        v2 = torch.clamp_min(v1, -0.5)  
        return torch.clamp_max(v2, 0.9) 


# Initializing the model