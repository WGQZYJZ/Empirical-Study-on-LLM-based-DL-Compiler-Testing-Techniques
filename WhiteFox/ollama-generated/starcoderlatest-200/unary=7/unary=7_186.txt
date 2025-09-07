
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) * clamp(min=0, max=6, l1 + 3) # Multiply the output of the linear transformation by the clamped output of the linear transformation added with 3
        v2 = v1 / 6  # Divide the output of the multiplication by 6
        return v2


# Initializing the model
m2 = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
