
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1) * 0.5
        v2 = self.conv2(v1) * 0.7071067811865476
        v3 = torch.mm(v1, v2)
        return v3


# Initializing the model
m = Model()


