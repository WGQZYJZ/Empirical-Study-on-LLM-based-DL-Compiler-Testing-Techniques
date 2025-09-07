
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc = torch.nn.Linear(5000, num_classes)
 
    def forward(self, x):
        v  = self.conv(x)
        v  = v.view(v.size(0), -1)
        v  = F.relu(self.fc(v))
        return v


# Initializing the model
m = Model()


