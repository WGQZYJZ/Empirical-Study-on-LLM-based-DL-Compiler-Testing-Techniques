
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 8)
 
    def forward(self, x1, other=None):
        v0 = None # Dummy output
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
            return (v0, v2)
 
        return v1


# Initializing the model
m  = Model()
 

# Inputs to the model
x1= torch.randn(32,5)
other= torch.randn(8,)
__output__  = m(x1, other=other)

