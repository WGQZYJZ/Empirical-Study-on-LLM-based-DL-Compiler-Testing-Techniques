
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3*64*64, 50) # input dimension: (N x C*H*W), output dim: (N x H*W x W*50)
        self.linear2 = torch.nn.Linear(50, 3)
 
    def forward(self, x):
        v1 = self.linear1(x) # Apply linear transformation to the input tensor
        v2 = v1 * 0.5 # Multiply the output of the previous operation by 0.5
        v3 = v1 + (v1 * v1 * v1) * 0.044715 # Add the output of the previous operation to the cubed linear transformation multiplied by 0.044715
        v4 = v3 * 0.7978845608028654 # Multiply the output of the previous operation by 0.7978845608028654
        v5 = torch.tanh(v4) # Apply the hyperbolic tangent function to the output of the previous operation
        v6 = v5 + 1 # Add 1 to the output of the hyperbolic tangent function
        v7 = v2 * v6 # Multiply the output of the linear transformation by the output of the hyperbolic tangent function
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3*64*64)
