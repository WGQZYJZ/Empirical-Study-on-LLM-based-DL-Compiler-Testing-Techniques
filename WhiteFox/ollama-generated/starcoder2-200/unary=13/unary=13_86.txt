
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(12800, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
__input_1__ = torch.randn(784, dtype=torch.float) # Size: [784]

# Inputs to the model
x1 = __input_1__.reshape(-1).view(784, 64)

 # Initializing the model
m2  = Model()
 
 
 x2  = torch.randn(93504)
 
__output__  = m(__input_1__,  )
