

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([arg1, arg2], 1) # Create a tensor filled with the scalar value 1
        v2 = v1 + 4 # Add 4 to each element of the tensor created in the previous step
        v3 = v2 * 50  # Multiply each element by 50
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
    x1  = torch.randn(arg1, arg2)
    x2  = torch.randn(arg1, arg2)
    
    