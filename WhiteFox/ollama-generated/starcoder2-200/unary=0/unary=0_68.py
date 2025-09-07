
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 + v2
        v4 = v3 * v3 
        v5 = v3 - v2 
        v6 = v4 - v5
        v7 = torch.exp(v6 / self.__class__.eps())
        v8 = v7.pow(-0.3)
        v9 = 1 + v8
        v10= v2 * v9
        return v10


# Initializing the model
m  = Model()
__output__  = m(x1)