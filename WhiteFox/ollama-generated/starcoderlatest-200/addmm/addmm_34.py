
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp=None):
        v1 = self.conv(x1)
        if not inp:
            t1 = None
        else: 
            t1 = torch.mm(input1, input2) 
        v2 = v1 * 0.5 + t1
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
