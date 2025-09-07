
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x2):
        v7  = self.linear(x2) # Apply a linear transformation to the input tensor
        v8  = torch.tanh(v7)  # Apply the hyperbolic tangent function to the output of the linear transformation
        return v8

# Initializing the model
m1  = Model()


# Inputs to the model
x2  = torch.randn(4, 5)
__output__  = m1(x2)
