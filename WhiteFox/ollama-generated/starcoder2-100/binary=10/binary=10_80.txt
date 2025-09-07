
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = torch.nn.functional.linear(x1)
        if not other is None:
            v2  = v1 + other 
        else: 
            v2 = v1
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1, x3  = torch.randn(100, 8), torch.randn(50, 6)
 
