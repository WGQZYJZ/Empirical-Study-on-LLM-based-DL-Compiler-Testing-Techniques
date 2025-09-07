
class Model(torch.nn.Module):
    def __init__(self, num_features: int = 3, num_classes: int = 2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(num_features, 16, 3)
        self.conv2 = torch.nn.Linear(16 * num_features, num_classes)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = self.conv2(torch.cat([v2, v5], dim=1))
        return v6


# Initializing the model
m = Model()

