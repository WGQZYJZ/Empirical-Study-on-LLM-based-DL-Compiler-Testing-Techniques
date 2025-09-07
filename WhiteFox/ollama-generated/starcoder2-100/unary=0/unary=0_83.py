
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        return x1.mean()

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(8)
__output__  = m(x1)

