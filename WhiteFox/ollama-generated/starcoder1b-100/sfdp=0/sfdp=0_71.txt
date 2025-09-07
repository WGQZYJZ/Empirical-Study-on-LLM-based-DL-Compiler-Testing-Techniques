
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 2, stride=2, padding=1)
        self.fc1 = torch.nn.Linear(16 * 64 * 64, 3072)
 
    def forward(self, x):
        v = F.relu(self.conv1(x))
        v = F.relu(self.conv2(v))
        v = v.view(-1, 16 * 64 * 64)
        v = self.fc1(v)
        return v

# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
