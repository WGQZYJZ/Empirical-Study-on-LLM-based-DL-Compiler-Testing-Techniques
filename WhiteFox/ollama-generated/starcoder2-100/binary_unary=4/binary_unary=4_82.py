
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32,8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3


# Initializing the model 
m  = Model()

# Inputs to the model
other = torch.randn(8,50,4) # A 5-dimensional tensor used as keyword argument
x1 = torch.randn(6, 32) # A sample input of size [6 x 32]
