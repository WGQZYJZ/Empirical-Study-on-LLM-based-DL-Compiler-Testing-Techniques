

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 12)
 
    def forward(self, x1):
        v0  = self.linear(x1)
        v1  = v0 > 0
        v3  = -v0 * negative_slope # the negative slope is a constant in your scenario with value=0.5 and datatype=float
        v2  = torch.where(v1, v0, v3)
        return v2


# Initializing the model
m  = Model()
negative_slope = float(0.5); 

# Inputs to the model
x1  = torch.randn(1, 8)
__output__  = m(x1)

