
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
       v0 = self.linear(x1) # Apply linear transformation to the input tensor 
       v1 = v0 * 0.5  # Multiply the output of the linear transformation by 0.5
       v2 = (v0 ** 3) * 0.7978845608028654 + (v0*v0) * 0.044715 
       v3 = torch.tanh(v2) # Apply the hyperbolic tangent function to the output of the previous operation
       v4 = v3 + 1 # Add 1 to the output of the hyperbolic tangent function
       return v1*v4

# Initializing the model
m = Model()

