
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1)
        self.fc = torch.nn.Linear(4, 4)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.nn.functional.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.tanh(v3)
        v5 = torch.sigmoid(self.fc(v4))
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
