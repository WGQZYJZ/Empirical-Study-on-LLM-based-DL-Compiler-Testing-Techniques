
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v2 = self.linear(x1)
        v3 = v2 + 3
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v7 = v5 / 6
        return v7


# Initializing the model
m  = Model()
 
 # Inputs to the model
 x1  = torch.randn(1, 10)
 
__output__  = m(x1)
