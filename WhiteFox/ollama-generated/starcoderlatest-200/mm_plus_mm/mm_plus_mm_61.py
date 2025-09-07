
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, x2)
        v3 = torch.mm(x2, v1)
        return (v1 + v2) + v3


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # tensor input
x2 = torch.randn(1, 3, 64, 64) # tensor input
