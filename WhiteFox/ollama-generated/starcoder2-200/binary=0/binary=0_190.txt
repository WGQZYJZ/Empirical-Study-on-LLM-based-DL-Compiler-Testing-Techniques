
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, other):
        v1  = self.conv(x1)
        return v1 + other


# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(10, 32, 64, 89)


x1 = torch.randn(10, 3, 64, 64)


__output__  = m(x1, other=other)

