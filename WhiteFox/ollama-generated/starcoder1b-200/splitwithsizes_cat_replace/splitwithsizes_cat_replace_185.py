
class Model(torch.nn.Module):
    def __init__(self, num_splits=2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.split1 = torch.nn.Split([1], num_splits)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.concat1 = torch.nn.Concat([self.conv1] + self.split1 + [self.conv2])
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = torch.cat([v2] * len(self.split1), dim=1)
        return self.concat1(v6)


# Initializing the model
m = Model()
