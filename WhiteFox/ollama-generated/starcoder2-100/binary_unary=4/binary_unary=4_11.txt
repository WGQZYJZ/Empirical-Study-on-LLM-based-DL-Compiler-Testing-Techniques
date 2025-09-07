
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(32* 16* 10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model and passing a tensor as keyword argument to `Model()` constructor
m  = Model(other=torch.randn(32* 16* 10))
 
# Inputs to the model
x1 = torch.randn(32, 8)
__output__  = m(x1)

