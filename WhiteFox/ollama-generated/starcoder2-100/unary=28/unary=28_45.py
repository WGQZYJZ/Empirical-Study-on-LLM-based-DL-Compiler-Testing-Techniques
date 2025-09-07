
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v2  = self.linear(x1) 
        return v2.clamp_min(9).clamp_max(-5)

# Initializing the model
m = Model()

 # Inputs to the model
   
x1  = torch.randn(80, 10)
__output__   = m(x1)

