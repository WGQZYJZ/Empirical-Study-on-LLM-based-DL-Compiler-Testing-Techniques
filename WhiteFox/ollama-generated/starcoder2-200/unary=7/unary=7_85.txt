
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        v1 = self.l1(x)
        v2 = torch.clamp(v1 + 3, min=0, max=6)
        v3 = v2 / 6
        return v3


# Initializing the model:
m = Model()

 # Inputs to the model
x = torch.randn(8, 32)

__output__  = m(x)