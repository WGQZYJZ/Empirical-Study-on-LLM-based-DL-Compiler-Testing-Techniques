
class Model(torch.nn.Module):
    def __init__(self, input_size=1600):
        super().__init__()
        
        self.linear  = torch.nn.Linear(input_size, outputSize)
 
    def forward(self, x1):
        v2  = torch.tanh(self.linear(x1)) # Applying a linear transformation followed by the hyperbolic tangent function
        return v2

# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(batchSize, m.input_size)

