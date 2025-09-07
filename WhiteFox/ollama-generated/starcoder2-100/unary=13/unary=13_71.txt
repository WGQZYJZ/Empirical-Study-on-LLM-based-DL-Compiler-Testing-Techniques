
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 8, 16)
 
    def forward(self, x):
        v0 = self.linear(x).sigmoid()
        v1 = self.linear(v0) 
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(486237951, 32 * 8)
__output__  = m(x)

