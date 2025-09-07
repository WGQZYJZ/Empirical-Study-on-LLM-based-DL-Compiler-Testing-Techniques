
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1, min=0., max=6.) * (6. - v1) + 3  # Multiply the output of the linear transformation by the clamped output of the linear transformation added with 3
        return v2 / 6  # Divide the output of the multiplication by 6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
