
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(8, 1)
 
    def forward(self, x2):
        v7  = self.conv(x2)
        v9  = torch.clamp_min(v7 + 3, 0) 
        v14 = torch.clamp_max(v9 , 6)    
        v8  = (torch.div(v14,  6)).float()       
        return v8

# Initializing the model
m2  = Model()

