
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        t1 = self.conv(x1)
        t2 = torch.cat([t1, t1, t1, ..., t1], dim=-1)
        return t2


# Initializing the model
m = Model()

