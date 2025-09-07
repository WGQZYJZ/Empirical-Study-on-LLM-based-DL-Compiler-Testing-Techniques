
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d((2, 2), (2, 2))
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = F.relu(self.conv2(x))
        return x


# Initializing the model
m = Model()


