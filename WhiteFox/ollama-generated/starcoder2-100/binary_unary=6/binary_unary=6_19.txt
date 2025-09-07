
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3*64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to input tensor
        v2 = v1 - other        # Subtract 'other' from the result of the linear transformation.
        return relu(v2)

# Initializing the model
m = Model()
__output__  = m(torch.randn(8,3*64))

