

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 8, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply linear transformation to the input tensor
        v2 = torch.clamp(min=-0.5 * torch.abs(v1), max=6, source=torch.add(source=v1, scalar=3))  # Apply clamping
        v3 = v2 / 6  # Divide the output of the linear transformation by 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(409, 64)


