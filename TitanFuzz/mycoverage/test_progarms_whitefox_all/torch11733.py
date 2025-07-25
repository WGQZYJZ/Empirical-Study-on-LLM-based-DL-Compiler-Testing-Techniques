import torch
from torch import nn

__init__(...):
    super().__init__()
    self.linear = torch.nn.Linear(num_classes, num_classes)
    self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

# Forward function
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = F.relu(v2)
        v4 = v3 + x2
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
