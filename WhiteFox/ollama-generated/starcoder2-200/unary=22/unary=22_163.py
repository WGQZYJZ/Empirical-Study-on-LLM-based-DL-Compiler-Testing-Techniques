
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 10)
 
    def forward(self, x1): 
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = torch.tanh(v1)#Apply the hyperbolic tangent function to the output of the linear transformation 
        return v2


# Initializing the model 
m = Model(32)
 

# Inputs to the model
x1 = torch.randn(10, 32)
