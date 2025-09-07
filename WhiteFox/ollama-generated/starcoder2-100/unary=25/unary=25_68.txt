
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = v1 > 0 # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v3 = negative_slope = x1 * v2 
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()
 
# Input to the model
x1 = torch.randn(10,)
__output__  = m(x1)

