
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) 
        v2  = v1 > 0 # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v3  = v1 * negative_slope  
        v4  = torch.where(v2, v1, v3) 
        return v4

# Initializing the model
m = Model()
negative_slope = -0.7071067811865476 # The value of negative slope to be used in the leaky ReLU function


# Inputs to the model
x1  = torch.randn(3, 2)
__output__  = m(x1)