
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, t1=None):
        v1 = self.conv(x1)
        if not t1:
            t2 = v1 + other_tensor
        else:
            t2 = v1 + t1
        return t2


# Initializing the model
m  = Model()


# Inputs to the model
other_tensor = torch.randn(3, 8, 5)
x1          = torch.randn(1, 3, 64, 64)
__output__  = m(x1, t1=other_tensor)