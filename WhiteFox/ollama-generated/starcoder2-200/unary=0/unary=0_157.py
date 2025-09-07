
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 ** 2
        v4  = v3 * v1 
        v6  = v4 * 0.044715
        v8  = v1 + v6
        v9  = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v2 * v10
        return v11


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)