

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = self.linear(x1)  # Applying linear transformation to the input tensor
        v3 = relu(v2 + v1) 
        return v3

# Initializing model
m = Model()


# Inputs to the model
x1, x2  = torch.randn(10, 4), None

# Expected result from the model
