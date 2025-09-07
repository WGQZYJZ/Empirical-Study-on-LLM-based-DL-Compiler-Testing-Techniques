
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = other + v1  # v2 will contain the addition of other and v1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
