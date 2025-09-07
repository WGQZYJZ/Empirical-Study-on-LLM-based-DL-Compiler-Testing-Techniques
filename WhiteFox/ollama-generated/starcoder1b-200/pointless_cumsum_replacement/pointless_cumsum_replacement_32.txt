
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 8, -1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2).cumsum(1).reshape(-1) + 1
        return v3


# Initializing the model
m = Model()

