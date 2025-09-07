
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.mm(v1, v1.t())
        t2 = torch.cat([t1, t1, ..., t1])  # Here the length of [t1] depends on the input size
        return t2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
