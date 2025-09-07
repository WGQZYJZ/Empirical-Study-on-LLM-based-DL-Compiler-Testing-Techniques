
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.sigm  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = self.sigm(v1)
        v3  = v1 * v2 # 