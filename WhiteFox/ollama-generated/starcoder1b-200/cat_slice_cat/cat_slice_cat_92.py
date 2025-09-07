
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)
        v1 = self.conv1(t1)
        v2 = torch.mean(v1, dim=0)
        v3 = self.conv2(v2)
        v4 = v3 * 0.5
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 16, 32, 32)
