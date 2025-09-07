
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1  = torch.clamp_min(x1, -5) # Clamp the output of the linear transformation to a minimum value
         v2  = torch.clamp_max(v1, 5)# Clamp the output of the previous operation to a maximum value
         return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 4) # Initialize an input tensor with shape [3, 4]
__output__  = m(x1)# Compute the outputs of the model using the provided inputs


