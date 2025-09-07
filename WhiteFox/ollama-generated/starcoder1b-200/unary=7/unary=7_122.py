
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        l1 = self.linear(x)
        return l3 * clamp(min=0, max=6, l1 + 3)

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 20, 5)
