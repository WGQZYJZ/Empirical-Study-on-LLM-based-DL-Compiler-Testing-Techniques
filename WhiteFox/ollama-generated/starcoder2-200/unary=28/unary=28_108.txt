
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1, min=-5) # Clamp the output of the linear transformation to a minimum value -5
        v3  = torch.clamp_max(v2, max=500) # Clamp the output of the previous operation to a maximum value 500
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 4)
__output__  = m(x1)
