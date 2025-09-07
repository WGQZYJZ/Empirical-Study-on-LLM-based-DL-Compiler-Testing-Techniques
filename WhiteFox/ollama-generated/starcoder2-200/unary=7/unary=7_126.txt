
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 256)
    
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = clamped_out  = torch.clamp(v1 + 3, min=0, max=6) # Clamp the output of the linear transformation by 3 and then cast to int
        v3 = v2 / 6 
        return v3

# Initializing model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 64) 
  __output__  = m(x1)

