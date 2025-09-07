
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.negative_slope  = -1
 
    def forward(self, x2): 
        v7  = self.linear(x2) 
        v8  = v7 > 0 
        v9  = v7 * negative_slope  
        v10 = torch.where(v8, v7, v9)
        return v10

# Initializing the model
m  = Model()

 # Inputs to the model
x2  = torch.randn(1,3)
 
 __output__  = m(x2)
