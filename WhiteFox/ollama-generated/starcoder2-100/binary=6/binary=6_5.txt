
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply linear transformation to input tensor
        v2 = v1 - other # Subtract 'other' from the output of linear transformation
        return v2

# Initializing model
m  = Model()


Inputs to model:
x1 = torch.randn(5, 3).requires_grad_(True)
other = torch.randn(4).requires_grad_(True)
