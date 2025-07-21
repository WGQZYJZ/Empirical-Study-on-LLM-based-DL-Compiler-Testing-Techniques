"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCELoss\ntorch.nn.BCELoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
x = torch.rand(1, 1, requires_grad=True)
y = torch.rand(1, 1, requires_grad=True)
loss = nn.BCELoss()
output = loss(x, y)
print(output)