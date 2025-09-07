
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 + other 
        v3 = torch.relu(v2)
        return v3
 
# Initializing the model
m  = Model()

 # Inputs to the model
other  = torch.randn(8, 64)
x1  = torch.randn(50, 32)
__output__  = m(x1, other=other)
