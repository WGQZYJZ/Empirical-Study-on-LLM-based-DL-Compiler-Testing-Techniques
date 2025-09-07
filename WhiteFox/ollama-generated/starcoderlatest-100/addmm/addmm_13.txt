
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
        if inp is None:
            self.inp = torch.randn((4, 8))
        else:
            self.inp = inp
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.mm(v1, self.inp) + self.inp
        return v2

# Initializing the model with a different input tensor
m = Model(torch.randn((8, 4)))

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
