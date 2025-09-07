
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(4, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, requires_grad=True)
y1 = m(x1)


