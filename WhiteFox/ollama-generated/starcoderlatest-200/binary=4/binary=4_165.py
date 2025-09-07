
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other = torch.tensor(0.1, requires_grad=True) # Setting another parameter
x1 = torch.randn(1, 32, 64, 64)
