class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


m = Model()
x1  = torch.randn(1, 3, 64, 64)
__output__   = m(x1)
