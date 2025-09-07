
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=2)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 4, 64, 64)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()

