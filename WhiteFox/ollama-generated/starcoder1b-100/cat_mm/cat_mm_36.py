
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.cat([v1, v1, v1], dim=-1)
        return t1


# Inputs to the model
input1 = torch.randn(3, 64, 64)
input2 = torch.randn(8, 64, 64)
