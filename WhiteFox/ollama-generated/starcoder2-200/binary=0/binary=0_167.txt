
class Model(torch.nn.Module):
    def __init__(self, m1 = None):
        super().__init__()
        self.conv   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1      = self.conv(x1) + m1 # This line causes the error. 
        return v1

m  = Model()
x1   = torch.randn(2,3,64,64)

__output__    = m(x1).to('cpu')

