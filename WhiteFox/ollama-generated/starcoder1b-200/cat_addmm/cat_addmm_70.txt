
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
 
    def forward(self, x1, x2):
        t1 = self.conv1(x1)
        t2 = self.conv2(x2)
        return torch.cat([t1, t2], dim=1)


# Initializing the model
m = Model()

