
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear  = torch.nn.Linear(32*64*64, 1)
 
    def forward(self, x1):
        v1 = linear(x1) 
        v2 = sigmoid(v1) # Add another operation that may be in a different position
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(4, 32*64*64)
 
