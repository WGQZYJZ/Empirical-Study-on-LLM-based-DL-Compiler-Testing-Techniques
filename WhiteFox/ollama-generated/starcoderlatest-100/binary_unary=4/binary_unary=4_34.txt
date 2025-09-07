
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1, other=None):
        if other is not None:
            t2 = self.linear(x1) + other
        else:
            t2 = self.linear(x1)
        t3 = torch.nn.ReLU()(t2)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
other = torch.randn(1, 4, 64, 64)
