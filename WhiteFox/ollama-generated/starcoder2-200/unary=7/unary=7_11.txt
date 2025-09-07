
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
 
    def forward(self, x1):
        v2 = self.linear(x1) # Apply linear transformation to the input tensor
        v4 = v2 * clamp(min=0, max=6, v2 + 3) # Multiply the output of the linear transformation by the clamped output (clamped between 0 and 6) of the linear transformation added with `3`
        return torch.nn.functional.silu(v4 / 6)


# Initializing the model
m = Model()


# Inputs to the model