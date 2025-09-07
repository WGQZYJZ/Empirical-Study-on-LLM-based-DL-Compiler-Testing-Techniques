
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x): 
        v1 = self.linear(x)
        v2 = (v1 > 0).float()
        v3 = -0.05 * v1 # negative slope is -0.05
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 256)
__output__  = m(x)