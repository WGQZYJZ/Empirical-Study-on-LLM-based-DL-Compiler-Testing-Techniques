
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, [3, 64, 64], dim=-1)
        return v1[0] * 0.5 + v1[1] * 0.7071067811865476 + torch.erf(v1[2]) + 1


# Initializing the model
m = Model()


