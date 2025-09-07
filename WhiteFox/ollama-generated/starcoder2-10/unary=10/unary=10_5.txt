
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(25, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) 
        v4  = torch.clamp_max(v3, 6)  
        v5  = v4 / 6    
        return v5


# Initializing the model
m  = Model()

# Input to the model:
x1  = torch.randn(2500, 25) # a random tensor of shape (N=2500 x H=25). Please set N and H appropriately.
 
__output__  = m(x1)

