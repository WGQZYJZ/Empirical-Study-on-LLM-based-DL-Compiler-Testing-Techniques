
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(3, 8)
 
    def forward(self, x2):
        v7  = self.l1(x2)
        v8  = v7 + 3
        v9  = torch.clamp_min(v8, 0)
        v10 = torch.clamp_max(v9, 6)
        v11 = v10 / 6 
        return v11


# Initializing the model
m2 = Model()


# Inputs to the model
x3 = torch.randn(45, 3)

__output__  = m2(x3)

