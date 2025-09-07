
class LinearTransform(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 5 * 5, 16)
 
    def forward(self, x1):
        return self.linear(x1)


# Initializing the model
l = LinearTransform()

# Inputs to the model
x1 = torch.randn(40000, 32, 5, 5)
