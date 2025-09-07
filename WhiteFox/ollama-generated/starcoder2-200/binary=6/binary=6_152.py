
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2  = v1 - 47  # <--- Other
        return v2


# Initializing the model and a variable for 'other' value
m = Model()
o = torch.tensor([0]) 

# Inputs to the model
x1 = torch.randn(3)

# Initial call
__output__  = m(x1)

