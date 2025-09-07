
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(10, 256)
 
    def forward(self, x):
        v1 = self.linear(x) # Apply linear transformation to the input tensor
        v2 = v1 * clamp(min=0, max=6, v1 + 3) # Multiply the output of the linear transformation by the clamped output (clamped between 0 and 6) of the linear transformation added with `3`
        v3 = v2 / 6 # Divide the output of the multiplication by `6`
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 10)
