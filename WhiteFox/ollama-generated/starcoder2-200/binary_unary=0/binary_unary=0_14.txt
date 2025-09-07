
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + x2_other
        v4  = torch.relu(v2)
        return v4


# Initializing the model
m  = Model()
m._modules['conv'].weight.data.fill_(0) # make it always zero!
m._modules['conv'].bias.data.fill_(0)   # make it always zero!
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

