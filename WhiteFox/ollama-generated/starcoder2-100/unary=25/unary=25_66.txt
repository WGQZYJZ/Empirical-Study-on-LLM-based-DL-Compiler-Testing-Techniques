
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v2  = linear(x1)
        v3  = v2 > 0
        v4  = -v3 * negative_slope 
        v5  = (v2 + v4)*negative_slope
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(64, 784)
__output__  = m(x1)

