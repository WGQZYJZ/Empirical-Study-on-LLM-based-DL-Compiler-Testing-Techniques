
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        v2 = v0 > 0
        v4 = v0 * negative_slope
        v5 = torch.where(v2, v0, v4)
        return v5


# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(3,)
 
__output__  = m(x1)

