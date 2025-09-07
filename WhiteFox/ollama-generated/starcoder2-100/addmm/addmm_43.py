

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        return self.conv(x)

# Initializing the model
m = Model()

# Inputs to the model
inp  = torch.randn([547965])
x   = torch.rand([3,28,28])
__output__  = m(x, inp=inp)

