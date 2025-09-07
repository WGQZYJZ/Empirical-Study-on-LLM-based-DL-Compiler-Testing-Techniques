
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3*64, 256)
    
    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = (v0 > 0).type_as(v0)
        v2 = v0 * negative_slope
        v3 = torch.where(v1, v0, v2)
        return v3
# Initializing the model
m  = Model()
 
# Inputs to the model 
x1  = torch.randn(8, 3*64)
__output__  = m(x1)

