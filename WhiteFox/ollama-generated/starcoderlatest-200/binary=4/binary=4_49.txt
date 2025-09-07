
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()

# Inputs to the model
other_tensor = torch.randn(4, 8)
x1 = torch.randn(5, 3, 64, 64)
