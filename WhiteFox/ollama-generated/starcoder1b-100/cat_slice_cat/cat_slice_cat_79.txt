
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1[:, 0:size], x2[0:size]], dim=1)
        return self.conv(v1)


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(1, 8)
