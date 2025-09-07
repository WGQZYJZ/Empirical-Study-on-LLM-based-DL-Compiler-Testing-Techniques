
class Model(torch.nn.Module):
    def __init__(self, c):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.c = c
 
    def forward(self, x):
        v0 = self.conv(x)
        v2 = v0 - self.c
        return v2

# Initializing the model
m = Model(torch.randn(1, 3))


# Inputs to the model
__input__  = torch.randn(1, 3, 64, 64)
 
 # Output of the model
