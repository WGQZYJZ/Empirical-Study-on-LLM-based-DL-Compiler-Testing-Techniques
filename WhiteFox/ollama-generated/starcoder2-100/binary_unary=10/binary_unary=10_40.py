
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(10) * 5 + 64
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 8)
__output__   = m(x1)

