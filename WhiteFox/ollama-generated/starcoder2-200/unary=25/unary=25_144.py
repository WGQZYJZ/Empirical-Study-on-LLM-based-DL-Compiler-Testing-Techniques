
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 2)
    
    def forward(self, x):
        v1  = self.lin(x) # Apply a linear transformation to the input tensor 
        v2  = (v1 > 0).float() * -2 + v1 # For each element in v1, if it is greater than 0, choose the corresponding element from v1; otherwise, choose the corresponding element of the multiplication by -2 plus v1
        return v2

# Initializing model
m = Model()

# Inputs to model
x = torch.randn(32, 10)

