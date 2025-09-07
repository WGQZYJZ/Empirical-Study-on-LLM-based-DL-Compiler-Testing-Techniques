
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        v1  = self.lin(x1) # Apply a linear transformation to the input tensor 
        v2  = v1 + other   # Add another tensor to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()
other  = torch.randn(3,)
 
# Inputs to the model
x1  = torch.randn(5, 3)
__output__  = m(x1)

