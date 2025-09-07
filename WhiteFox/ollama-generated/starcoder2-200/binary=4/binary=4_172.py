
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor
        return v1 + other


# Initializing the model
m  = Model()

# Inputs to the model
x2 = torch.randn(320, 48)
