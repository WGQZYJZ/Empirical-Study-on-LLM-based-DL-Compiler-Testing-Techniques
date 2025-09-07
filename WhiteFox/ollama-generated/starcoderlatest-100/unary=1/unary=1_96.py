

# Description of requirements
The model should contain the following pattern:


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 64, kernel_size=3)
 
    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = v1 + (v1 * v1 * v1) * 0.044715 # Add the output of the previous operation to the output of the linear transformation cubed multiplied by 0.044715, where:
        if v1 > 0 then multiply by 0.5-0.25, otherwise multiply by 0.044715
        v3 = v2 * 0.7978845608028654 # Multiply the output of the previous operation by 0.7978845608028654
        v4 = torch.tanh(v3) # Apply the hyperbolic tangent function to the output of the previous operation
        v5 = v4 + 1 # Add 1 to the output of the hyperbolic tangent function
        v6 = v2 * v5 # Multiply the output of the linear transformation by the output of the hyperbolic tangent function
