
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(min=0, max=6, v1 * (v1 + 3)) # Apply the clamped output of the linear transformation added with 3 to the input tensor
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
