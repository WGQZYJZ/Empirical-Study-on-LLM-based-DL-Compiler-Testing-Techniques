
class Model(torch.nn.Module):
    def __init__(self, n1, n2=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1): 
        v1 = self.conv(x1) + self.other
        return v1


# Initializing the model
m = Model(None)
other = torch.randn() # We have set this to a random float tensor; it can be anything but 0.
__output__  = m(torch.randn(1,3,64,64), other=other)

