
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v0  = self.conv(x)
        v4  = F.sigmoid(v0)
        return v0 * v4


m = Model()

__output__  = m(torch.randn(1,3,64,64))