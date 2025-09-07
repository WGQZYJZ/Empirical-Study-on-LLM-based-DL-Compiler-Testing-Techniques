
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 1)
 
    def forward(self, x):
        v0 = self.linear(x) + 4
        v1 = 3 - v0
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(5, 256)
__output__  = m(x)

