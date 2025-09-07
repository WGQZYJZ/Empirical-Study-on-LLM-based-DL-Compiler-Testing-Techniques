
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = torch.cat([t1, t1, t1], dim=-1)
        t3 = torch.cat([t1, t1, t1, t1], dim=0)
        return self.conv2(t2).view(-1, 8 * 64 * 64)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
