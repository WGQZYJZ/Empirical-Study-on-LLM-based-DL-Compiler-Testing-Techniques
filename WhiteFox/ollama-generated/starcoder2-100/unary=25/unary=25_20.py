
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 32 * 3, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).float() - v1
        v3  = v2 * negative_slope
        return torch.where(v2>0., v1, v3)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

__output__  = m(x1)

