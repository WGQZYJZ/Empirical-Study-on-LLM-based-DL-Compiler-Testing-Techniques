
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        t1 = self.conv1(x1) + self.conv1(x1)
        t2 = self.conv2(x2) + self.conv2(x2)
        return torch.cat([t1, t2], dim=0)


# Initializing the model
m = Model()


