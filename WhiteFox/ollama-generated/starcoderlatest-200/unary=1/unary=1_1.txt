
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 + (v1 * v1 * v1) * 0.044715
        v4 = v3 * 0.7978845608028654
        v5 = torch.tanh(v4)
        v6 = v5 + 1
        v7 = v2 * v6
        return v7


# Description of requirements
Please add a constant to the output of linear transformation and multiply that constant by `0.7978845608028654`, then apply the hyperbolic tangent function to this sum, and then add `1` to the result of the hyperbolic tangent function.


# Model 1
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = x1 * (x1  * x1) # Add a constant to the output of linear transformation and multiply that constant by 0.7978845608028654 
        return torch.tanh(v1) + 1
 
# Inputs to the model
x1 = torch.randn(3, 64, 64)
