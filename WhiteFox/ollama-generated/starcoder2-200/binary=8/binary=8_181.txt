
class Model(torch.nn.Module):
    def __init__(self, k, m):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, k=None):
        v1 = self.conv(x1)
        v2 = v1 + k 
        return v2


# Initializing the model
m = Model(0.5, torch.randn((64)))


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
k   = x1.clone() # clone the tensor passed as a keyword argument
