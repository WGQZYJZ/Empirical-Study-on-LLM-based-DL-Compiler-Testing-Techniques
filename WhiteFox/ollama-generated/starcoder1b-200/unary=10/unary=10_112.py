
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8, 10)
 
    def forward(self, x1):
        l1  = self.conv(x1)
        l2  = torch.clamp_min(l1 + 3, 0)
        l3  = torch.clamp_max(l2, 6)
        l4  = (l3 / 6).mul(6)
        return l4


# Initializing the model
m = Model()

