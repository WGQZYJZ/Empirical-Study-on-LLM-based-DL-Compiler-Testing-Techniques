
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
        else:
            v2 = v1
        v3 = torch.nn.ReLU()(v2)
        return v3


# Initializing the model
m = Model()
m2 = Model(torch.tensor([1]))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output1__ = m(x1)
__output2__ = m2(x1, other=torch.tensor([1]))

