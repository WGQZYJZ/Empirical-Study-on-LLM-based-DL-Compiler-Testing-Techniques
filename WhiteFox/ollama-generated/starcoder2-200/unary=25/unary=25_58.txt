
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 1)
 
    def forward(self, x1):
        v0  = self.linear(x1) 
        v3  = torch.where((v0 > 0), v0, -2 * v0) 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
__output__  = m(x1)