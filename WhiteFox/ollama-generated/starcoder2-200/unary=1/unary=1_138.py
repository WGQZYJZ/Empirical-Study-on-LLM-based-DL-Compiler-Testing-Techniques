
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1  = self.linear(x1)
        v2  = v1 * 0.5 # The output of the linear transformation multiplied by `0.5`
        v3  = v1 + (v1 * v1 * v1) * 0.044715 # The output of the linear transformation added to the cubed output of the linear transformation multiplied by `0.044715`
 
        v4  = torch.tanh(v3)
        v5  = self.linear_2(x1, v4) + 1 # Add 1 to the output of the hyperbolic tangent function
 
        return v2 * v5


# Initializing the model
m  = Model()

# Inputs to the model