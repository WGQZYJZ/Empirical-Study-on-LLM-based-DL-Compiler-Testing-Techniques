
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v2 = v2 * 0.5
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v1 * v4
        return v5


# Initializing the model
m = Model()


