
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v2 ** 3
        v4 = (v3 + 1e-7).pow(-0.5)
        v6 = v4 + 1
        v7 = v2 * v6

        return v7


# Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(1,3,8,8)


