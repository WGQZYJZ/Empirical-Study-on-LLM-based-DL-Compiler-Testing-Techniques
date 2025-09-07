
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x1)
        if inp is not None:
            return v1 + inp
        else:
            return v1
 
 # Initializing the model
m = Model()

 # Inputs to the model and corresponding expected results of the model (optional)
x1  = torch.randn(3, 8, 64, 64)
__inp__  = None
