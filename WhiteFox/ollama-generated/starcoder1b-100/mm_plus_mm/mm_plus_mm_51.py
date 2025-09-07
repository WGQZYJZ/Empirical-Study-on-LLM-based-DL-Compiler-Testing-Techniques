
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)
 
    def forward(self, x1, x2, x3, x4):
        t1 = torch.mm(x1, x2)
        t2 = torch.mm(x3, x4)
        v1 = self.conv(t1) + self.conv(t2)
        return v1


# Initializing the model
m = Model()


