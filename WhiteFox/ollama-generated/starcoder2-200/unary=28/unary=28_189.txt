
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1, -50.) # Clamp the output of the linear transformation to a minimum value (-50 in this example).
        v3  = torch.clamp_max(v2, +50.) # Clamp the output of the previous operation to a maximum value (+50 in this example).
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3) # 3-dimensional tensor with random values that are drawn from the standard normal distribution

__output__  = m(x1)
