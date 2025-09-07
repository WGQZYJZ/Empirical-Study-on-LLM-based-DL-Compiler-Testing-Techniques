
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x):
        v = self.linear(x) + other
        return v


# Inputs to the model
__input__ = torch.randn(3, 4, 64, 64)
v1 = Model()(__input__)


