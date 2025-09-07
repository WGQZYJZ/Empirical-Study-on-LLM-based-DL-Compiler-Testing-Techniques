
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.sigmoid(v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32, requires_grad=True)
