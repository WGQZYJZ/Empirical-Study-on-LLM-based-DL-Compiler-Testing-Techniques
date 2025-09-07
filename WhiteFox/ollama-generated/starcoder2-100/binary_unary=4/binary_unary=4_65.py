
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(49, 50)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.max_pool2d(v1, [7], stride=[7])
        v3 = self.linear(v2) + other
        return v3
