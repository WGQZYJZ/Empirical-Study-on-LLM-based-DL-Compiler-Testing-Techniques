
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(784, 20)(x1) # Apply a linear transformation to the input tensor
        v2  = (v1 > 0).float() * (-v1 + v1 * v2) # For each element in the output of the linear transformation that is greater than or equal to zero choose the corresponding element, otherwise choose the corresponding negative value of the corresponding element. Then add the resulting tensor with its original value
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(64, 784)
