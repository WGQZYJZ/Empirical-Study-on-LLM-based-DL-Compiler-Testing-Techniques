
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.m = torch.nn.Linear(3, 2)
 
    def forward(self, x1, x2):
        v1 = self.m(x1)
        v2 = x2 * inp  # Input tensor 'inp' is passed as a keyword argument
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
inp = torch.randn(1, 3, 64, 64)
