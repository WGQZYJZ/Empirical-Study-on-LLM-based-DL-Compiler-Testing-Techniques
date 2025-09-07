
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1 + other)
        return v1


# Initializing the model
m = Model()
other = m.linear.weight

# Inputs to the model
x1 = torch.randn(10, 3)
__output__  = m(x1)

