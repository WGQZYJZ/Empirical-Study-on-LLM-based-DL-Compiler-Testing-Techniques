
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * -1e-2
        v4 = torch.where(v2, v1, v3) # Alternative version: v4 = torch.max(torch.zeros_like(v1), v1 + 1e-2)
        return v4


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(1, 20)
__output__  = m(x1)
