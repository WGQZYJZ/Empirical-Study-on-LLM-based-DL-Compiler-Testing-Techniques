
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v0  = self.linear(x1)
        v1  = torch.sigmoid(v0) 
        v2  = v1 * v0
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3)
__output__  = m(x1)

