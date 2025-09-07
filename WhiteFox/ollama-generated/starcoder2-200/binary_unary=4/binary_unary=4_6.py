
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2  = v1 + other 
        v3  = torch.relu(v2)
        return v3


# Initializing the model and passing an argument to `other`
m = Model()
other = torch.randn(1, 1) # Some random tensor passed as a keyword argument 
__output__  = m(torch.randn(50, 1), other=other) 
