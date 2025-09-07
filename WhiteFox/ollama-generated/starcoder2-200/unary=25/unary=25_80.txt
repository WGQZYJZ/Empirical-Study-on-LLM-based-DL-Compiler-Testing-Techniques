
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2a  = v1 > 0
        v3  = -v1 * negative_slope
        v4  = torch.where(v2a, v1, v3)
 
        return v4

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(10, 5)
negative_slope = 1e-6
 
__output__  = m(x1)

