
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.fc1   = torch.nn.Linear(16 * 4 * 4, 120)
        self.fc2   = torch.nn.Linear(120, 84)
        self.fc3   = torch.nn.Linear(84, 10)

    def forward(self, x1):
        h1 = F.relu(self.conv1(x1))
        h1 = F.max_pool2d(h1, kernel_size=2)

        h2 = F.relu(self.conv2(h1))
        h2 = F.max_pool2d(h2, kernel_size=2)

        h3 = h2.view(-1, 16 * 4 * 4)
        h3 = F.relu(self.fc1(h3))
        h3 = F.dropout(F.relu(self.fc2(h3)))
        return self.fc3(h3)


# Initializing the model
m = Model()


