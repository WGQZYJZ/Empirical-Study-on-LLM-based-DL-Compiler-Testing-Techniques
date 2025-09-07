
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  *  0.5
        v3  = v2 ** 3 
        v4  = torch.sin(v1 / math.pi**0.7659 + -8) + 1
        v5  = torch.erf(torch.sqrt(-2 + x)) + 1
        return t1


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
 
