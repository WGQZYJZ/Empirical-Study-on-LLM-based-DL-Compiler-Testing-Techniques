
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(7, 10)
 
    def forward(self, x2):
        v1  = self.linear(x2) 
        v3  = v1 + 3   
        v4  = torch.clamp_min(v3, 0)  
        v5  = torch.clamp_max(v4, 6)    
        v7  = v5 / 6
        return v7


# Initializing the model
m = Model()

 # Inputs to the model
x2 = torch.randn(1, 7)
 
# Output of the model on inputs x2
