
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(2*8*4+20, 10)
 
    def forward(self, x):
        v1 = F.relu(self.conv1(x))
        v2 = F.relu(self.conv2(v1))
        v3 = F.avg_pool2d(v2, 2, stride=2)
        v4 = v3.view(-1, 8*4*4)
        logits = self.fc(v4)
        return logits


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
