
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1) 
        v2  = v1 + 3 # Add 3 to the output of the linear transformation
        v3  = torch.clamp_min(v2, 0) # Clamp the output of the previous operation to a minimum of 0
        v4  = torch.clamp_max(v3, 6) # Clamp the output of the previous operation to a maximum of 6
        v5  = v4 / 6 # Divide the output of the previous operation by 6 
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(2, 3)
 
__output__  = m(x1)
 
