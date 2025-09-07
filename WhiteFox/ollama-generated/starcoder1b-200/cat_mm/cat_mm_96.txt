
class Model(torch.nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(8, num_classes)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1, ..., v1], dim=-1)
        v3 = self.fc(v2)
        return v3


# Initializing the model
m = Model(4)


