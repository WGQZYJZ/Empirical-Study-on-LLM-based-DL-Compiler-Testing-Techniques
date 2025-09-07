
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat((v1, 0.5*torch.ones_like(x1), 0.7071067811865476*torch.ones_like(x1)), 1)
        return torch.nn.functional.softplus(v2)


# Initializing the model
m = Model()


