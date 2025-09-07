
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation 
        v3  = v2 * v1 # Multiply the output of the sigmoid function by the output of the linear transformation        
        return v3


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(8, 32)
 
__output__  = m(x1) # The result of the forward pass should be a 3-dimensional tensor, and it should match the dimensionality of the input tensor, which is (8, 32).

