
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x) * 0.5
        v2 = self.conv2(v1) * 0.7071067811865476
        return v2


# Initializing the model
m = Model()


