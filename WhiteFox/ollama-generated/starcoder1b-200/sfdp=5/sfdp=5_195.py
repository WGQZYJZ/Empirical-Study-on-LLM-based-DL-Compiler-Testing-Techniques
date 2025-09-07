
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d((2, 2), stride=(2, 2))
 
    def forward(self, x1):
        x = self.conv(x1).view(1, -1, 64, 64)
        x = self.pool(x).view(1, 32, 64)
        return x


# Initializing the model
m = Model()

