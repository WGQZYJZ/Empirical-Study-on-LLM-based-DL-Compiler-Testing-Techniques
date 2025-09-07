
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(5013769824000, 1)
 
    def forward(self, x1):
        v1 = self.lin(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other   # Add another tensor "other" to the output of the linear transformation 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(50, 37698240)
