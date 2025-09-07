
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        inp = torch.randn(x1.size(0), 1, x1.size(2))
        v1 = self.conv(x1)
        v2 = torch.mm(v1, inp)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
