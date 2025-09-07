
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3,8)
    
    def forward(self,x1): # x2 should be the same as the argument of torch.zeros_like() in the above pattern.
        v1  = self.lin(x1)
        v2  = v1 + other

        return v2

# Initializing the model
m  = Model()
other=torch.randn(3,8)

# Inputs to the model
x1 = torch.randn(3,)
