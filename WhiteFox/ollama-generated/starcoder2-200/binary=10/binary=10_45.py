
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v2 = self.linear(x1) # Apply a linear transformation to an input tensor (specified by the keyword argument "other")
        return v3


# Initializing the model
m  = Model()
 

# Inputs to the model
x1 = torch.randn(1, 500, 500)
