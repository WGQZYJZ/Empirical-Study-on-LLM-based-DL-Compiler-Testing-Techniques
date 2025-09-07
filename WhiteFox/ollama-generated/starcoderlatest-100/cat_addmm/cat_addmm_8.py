
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, self.weight1, self.weight2)
        v2 = torch.cat([t1], dim=0)
        return v2
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
