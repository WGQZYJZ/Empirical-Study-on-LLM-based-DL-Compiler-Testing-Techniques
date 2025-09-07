
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v4  = v2 * 0.5
        v5  = v1 - 6.79
        v6  = torch.tanh(v1 / 8)
 
        return v6

m  = Model()


x1  = torch.randn(1, 3, 4, 4)

__output__   = m(x1)

