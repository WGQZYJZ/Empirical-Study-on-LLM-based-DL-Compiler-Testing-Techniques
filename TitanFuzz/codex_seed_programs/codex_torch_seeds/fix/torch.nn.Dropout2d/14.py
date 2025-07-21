'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
x = torch.randn(1, 1, 3, 3)
print('Input data: \n', x)
dropout = nn.Dropout2d(p=0.5, inplace=False)
y = dropout(x)
print('Output data: \n', y)