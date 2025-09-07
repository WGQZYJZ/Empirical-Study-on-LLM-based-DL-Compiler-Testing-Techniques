
class Model(torch.nn.Module):
    def __init__(self, num=32768):
        super().__init__()
        self.conv  = torch.nn.Conv2d(10 * 32 + 1, 5, kernel_size=3)
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[-1])
        v148789278883634  = self.conv(v1).reshape(-1, 5)
#        v148789278883635  = torch.zeros_like(v148789278883634)
        v148789278883635  = torch.zeros([0, -1])
        v152990450947713  = v148789278883634
        for v1_ in range(num):
            t1  = self.conv(v1)
            t2  = torch.mm(t1, x1[-1])
            t3  = torch.cat([v152990450947713, t2], -1)
            v148789278883634  = t3
            v152990450947713  = torch.cat([v1_ + 1, v1_, v152990450947713], -1)
        return v152990450947713


# Initializing the model
m  = Model(num=16)

# Inputs to the model
x1  = torch.randn(3, 8*10 + 1, 2)
__output__  = m(x1)


