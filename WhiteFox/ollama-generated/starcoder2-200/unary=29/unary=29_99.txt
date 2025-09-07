
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.act   = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.act(v1)
        return v2

m  = Model()
__output__  = m(x1)

