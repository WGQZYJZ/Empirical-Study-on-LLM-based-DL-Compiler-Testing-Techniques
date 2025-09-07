
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply a linear transformation to the input tensor
        v2 = v1 - other 
        v3 = torch.nn.functional.relu(v2)  # Apply the ReLU activation function to the result of the linear transformation 
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
other  =  50
x1     = torch.randn(1, 64*9*8) 
 
__output__  = m(x1)

# Final result: 
143