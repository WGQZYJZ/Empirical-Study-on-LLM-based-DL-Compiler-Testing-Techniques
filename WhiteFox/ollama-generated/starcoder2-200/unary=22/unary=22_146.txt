
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 20)
 
    def forward(self, x1):
         v1 = self.linear(x1) # Apply the linear transformation to the input tensor 
         v2 = torch.tanh(v1)# Apply the hyperbolic tangent function to the output of the linear transformation
         return v2


# Initializing and feeding data into model
m  = Model()
x1 = torch.randn(1, 784) # Generating an input tensor for the model
__output__  = m(x1)

