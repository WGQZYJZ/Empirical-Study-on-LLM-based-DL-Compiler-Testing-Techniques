
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3000, 32).requires_grad_()

__output__   = m(x1).sum().backward() # Summing the output of the model

# We need to call backward on the result of the function that is being modeled, in order for it to work. 
