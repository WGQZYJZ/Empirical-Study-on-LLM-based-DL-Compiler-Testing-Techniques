
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to input tensor
        v2  = v1 - other_tensor  # Subtract 'other' from the output of the linear transformation
        return v2

# Initializing and running model
m = Model()
x1 = torch.randn(3, 32)
