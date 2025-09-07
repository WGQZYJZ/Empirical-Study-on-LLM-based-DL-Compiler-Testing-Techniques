
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.pool  = torch.nn.AvgPool2d(2, stride=2)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.relu(v1)
        v3 = self.pool(v2)
        return v3

# Initializing the model
m = Model(n=5)


