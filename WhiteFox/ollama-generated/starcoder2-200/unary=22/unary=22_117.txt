
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v1  = torch.nn.Linear()(x1) # Applying a linear transformation to an input tensor
        v2  = torch.tanh(v1)# The hyperbolic tangent function is applied to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3) # Input to the model 

__output__  = m(x1)
