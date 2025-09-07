
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v6


# Initializing the model
m = Model()


