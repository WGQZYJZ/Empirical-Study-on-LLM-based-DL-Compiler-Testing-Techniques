
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = F.relu(v1)
        return v2

m  = Model()
__output__  = m(torch.randn(3, 8, 64, 64))

