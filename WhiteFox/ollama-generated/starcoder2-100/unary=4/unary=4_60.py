
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear()(x1) # Apply pointwise linear transformation to the input tensor
        
        v2  = v1 * 0.5 
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1 # Add 1 to the output of the error function
        v6  = v2 * v5  # Multiply the output of the linear transformation by the output of the error function
        
        return v6
        
# Initializing the model
m = Model()

# Inputs to the model