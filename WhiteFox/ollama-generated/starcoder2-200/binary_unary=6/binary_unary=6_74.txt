
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, y1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = v1 - other
        v3  = relu(v2) 
        return v3


# Initializing the model
m2 = Model()

# Inputs to the model
x1  = torch.randn(1, 3) # A batch of three input values
y1  = 500.0 # A value that will be subtracted from the first linear transformation output

