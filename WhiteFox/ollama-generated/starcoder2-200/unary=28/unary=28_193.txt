
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -237.888172) # Clamp the output of the linear transformation to a minimum value
        v3 = torch.clamp_max(v2, 4096.582539001465) # Clamp the output of the previous operation to a maximum value
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4096)
__output__  = m(x1)

