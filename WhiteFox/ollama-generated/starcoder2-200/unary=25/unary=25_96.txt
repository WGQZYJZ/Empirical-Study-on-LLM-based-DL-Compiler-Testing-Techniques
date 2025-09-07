
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear()
        v2a = (v1 > 0).int()
        v3  = v1 * negative_slope
        v4  = torch.where(v2a, v1, v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10, 50).float() - 0.5
__output__  = m(x1)

