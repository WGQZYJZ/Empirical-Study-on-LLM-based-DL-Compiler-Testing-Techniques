
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.pool  = torch.nn.MaxPool2d(3)
        self.fc    = torch.nn.Linear(4000, 6)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.pool(v1)
        v3 = v2.view(-1, 4000)
        v4 = self.fc(v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
