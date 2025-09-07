
class Model(torch.nn.Module):
    def __init__(self, max=20, min=-15):
        super().__init__()
        self.linear = torch.nn.Linear(487634, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -0.5)
        v3 = torch.clamp_max(v2, 15)
        return v3


# Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(176984, 487634)
__output__= m(x1)

