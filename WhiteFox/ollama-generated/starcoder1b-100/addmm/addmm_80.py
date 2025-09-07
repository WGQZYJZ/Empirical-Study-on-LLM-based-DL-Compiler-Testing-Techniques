
class Model(torch.nn.Module):
    def __init__(self, inp=200):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
        self.dropout1 = torch.nn.Dropout2d()
        self.relu = torch.nn.ReLU()
        self.fc1   = torch.nn.Linear(4 * inp, 32)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v1 = self.dropout1(v1)
        v1 = self.relu(v1)
        v1 = self.conv2(v1)
        v1 = self.dropout1(v1)
        v2  = torch.mm(v1, x) + inp
        v2 = self.fc1(v2)
        return v2


# Initializing the model
m = Model()


