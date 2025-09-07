
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v0  = x
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, -1.)
        v3  = torch.clamp_max(v2,  5.)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 60, 60)
__output__= m(x1).shape