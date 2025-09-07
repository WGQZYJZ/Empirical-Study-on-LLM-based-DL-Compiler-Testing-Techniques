
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v2 = self.linear(x1)
        return v2 + other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 3)


__output__  = m(x1)
