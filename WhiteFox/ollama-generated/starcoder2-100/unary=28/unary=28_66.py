

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1): 
        v2 = self.linear(x1).clamp_min(-0.5, min=None).clamp_max(.7, max=None)  
        return v2


# Initializing the model