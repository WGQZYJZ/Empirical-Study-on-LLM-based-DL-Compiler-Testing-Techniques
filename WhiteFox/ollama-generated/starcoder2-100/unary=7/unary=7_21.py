
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l = torch.nn.Linear(3, 4096)
 
    def forward(self, x1):
        v1  = self.l(x1)
        v2  = v1 * clamp(min=0, max=6, l1 + 3) 
        v3  = v2 / 6
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 4096)
__output__  = m(x1)

