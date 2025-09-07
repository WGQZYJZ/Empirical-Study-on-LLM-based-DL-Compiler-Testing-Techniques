
class Model(torch.nn.Module):
    def __init__(self, inputsize):
        super().__init__()
        self.conv = torch.nn.Linear(inputsize, 8192)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * clamp(min=0, max=6, l1 + 3) 
        v3  = v2 / 6
        return v3


# Initializing the model
m  = Model(inputsize)

 # Inputs to the model
 
x1 = torch.randn(7, inputsize)
__output__  = m(x1)

