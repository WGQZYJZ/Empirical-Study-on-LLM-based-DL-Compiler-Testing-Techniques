
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(32)
x1 = torch.randn(5, 800) * 9e-4 - 0.75  # Generated input tensor


