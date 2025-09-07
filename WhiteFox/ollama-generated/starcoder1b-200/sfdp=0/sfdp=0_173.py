
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
        self.fc = torch.nn.Linear(8 * 7 * 7, 8 * 3 * 3)
 
    def forward(self, x):
        h = F.relu(self.conv1(x))
        h = F.max_pool2d(h, 2)

        h = self.conv2(h).view(-1, 8 * 7 * 7)
        h = F.relu(self.fc(h))

        return h


# Initializing the model
m = Model()

