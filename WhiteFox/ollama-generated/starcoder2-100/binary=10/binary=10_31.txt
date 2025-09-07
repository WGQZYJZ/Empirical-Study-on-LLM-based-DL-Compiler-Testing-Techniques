
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1 + other) # Apply linear transformation to the input tensor. Also add another tensor as input for this transformation (i.e., the variable "other")
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 3) # Input data of shape 4 x 3
__output__  = m(x1 + other)

