
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=1)
 
    def forward(self, x):
        t1  = self.conv1(x)
        v1  = t1 * 0.5
        t2  = v1 + 1
        t3  = t2 ** 2
        t4  = t3 ** 2
        t5  = torch.erf(t4)
        t6  = t5 * 0.044715
        t7  = t6 + 1
        t8  = v1 + t7
        t9  = self.conv2(t8)
        return t9


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x)

