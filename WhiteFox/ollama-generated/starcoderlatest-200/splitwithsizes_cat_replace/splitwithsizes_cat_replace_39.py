
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        s0, s1, s2, s3 = torch.split(x1, split_sizes=[4, 4, 4, 4], dim=-1)
        c0 = self.conv1(s0)
        c1 = self.conv2(c0)
        return c1
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
