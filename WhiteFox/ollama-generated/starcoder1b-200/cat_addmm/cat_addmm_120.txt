
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool   = torch.nn.MaxPool2d(2, stride=2)
        self.fc1    = torch.nn.Linear(8 * 7 * 7, 2048)
        self.fc2    = torch.nn.Linear(2048, 2048)
 
    def forward(self, x):
        out  = self.pool(F.relu(self.conv1(x)))
        h   = out.view(out.shape[0], -1)
        h   = F.relu(self.fc1(h))
        h   = F.relu(self.fc2(h))
        return h


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
