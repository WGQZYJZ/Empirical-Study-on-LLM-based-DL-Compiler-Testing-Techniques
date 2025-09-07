
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
        negative_slope=0.5
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
       v1 = self.linear(x)
       v2 = v1 > 0
       v3 = v1 * negative_slope
       v4 = torch.where(v2, v1, v3)
       return self.conv(v4)


m = Model()


# Inputs to the model
input = torch.randn(8, 2048)
__output__  = m(input)

