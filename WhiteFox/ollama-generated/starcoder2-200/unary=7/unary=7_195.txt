
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1 = torch.nn.functional.linear(x1) # Apply linear transformation to the input tensor 
        l2  = clamp(min=0, max=6, l1 + 3) # Multiply the output of the linear transformation by the clamped output of the linear transformation added with 3
        l3  = l2 / 6 # Divide the output of the multiplication by 6
        return l3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 15)
__output__  = m(x1)

