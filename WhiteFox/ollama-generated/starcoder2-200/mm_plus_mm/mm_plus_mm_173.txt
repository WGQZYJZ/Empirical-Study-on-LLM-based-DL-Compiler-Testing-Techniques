
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(x4, x5)
        v3  = v1 + v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(64, 780) # Generate a random tensor with shape (64, 780) and with values between -1 and 1 for input x1 
x2  = m.mm.weight
x3  = torch.randn(64, 780) # Generate another random tensor of the same shape as x1 using the randomly generated weight matrix. This is input x3.
x4  = torch.randn(1950, 780) # Generate a third random tensor with shape (1950, 780), as it is the number of rows in the input data.
x5  = m.mm.weight[:1950] # Extract the first 1950 columns from this third input tensor using the randomly generated weight matrix. This is input x4.

__output___ = m(x1)

