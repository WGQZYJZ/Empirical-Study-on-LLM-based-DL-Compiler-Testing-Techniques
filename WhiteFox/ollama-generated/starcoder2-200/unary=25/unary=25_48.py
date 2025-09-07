
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).float() * -3 + \
              (~(v1 > 0)).float() * -7
        v3  = v1 * (-3) + ~(v1 < 4)
        return torch.where(v2 == 1, 8*v3, v2)

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(10, 2).float() + 4 
 
__output__  = m(x1)