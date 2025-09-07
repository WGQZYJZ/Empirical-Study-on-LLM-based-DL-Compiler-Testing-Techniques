
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear()
        v2  = v1(x1)
 
        v3  = v2 * 0.5
        v4  = torch.relu()
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 64)
__output__  = m(x1)