'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
x = Variable(torch.randn(1, 1, 5, 5))
model = nn.Sequential(nn.Conv2d(1, 6, 3), nn.ReLU(), nn.Conv2d(6, 16, 3), nn.ReLU())
y = model(x)
print(y)