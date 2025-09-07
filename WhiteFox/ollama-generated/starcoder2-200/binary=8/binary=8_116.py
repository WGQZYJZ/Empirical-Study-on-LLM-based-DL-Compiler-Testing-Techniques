
class Model(torch.nn.Module):
    def __init__(self, m1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
#        print(v1.shape)
#        print(m1.shape)
#        print(other.shape)
#        print('m1', m1[0][0])
        return v1 + other


m  = Model(m1=torch.randn(3,4))

__output__  = m(x1)

