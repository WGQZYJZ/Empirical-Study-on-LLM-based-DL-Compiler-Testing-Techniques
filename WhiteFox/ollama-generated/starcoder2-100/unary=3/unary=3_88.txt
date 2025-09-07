
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        
        v2 = torch.nn.Conv2d(3, 8, 1)
        v4 = v2(x1) * 0.5
        v7 = v4 + 1

        return v7


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

