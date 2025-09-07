
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        negative_slope = torch.full((v1.shape), 0.5) 
        v2 = v1 > 0 # Create a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, and False otherwise
        v3 = v1 * negative_slope # Multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v2, v1, v3) # For each element in v2, if the element is True, choose the corresponding element from v1, otherwise choose the corresponding element from v3
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5, 3) 

