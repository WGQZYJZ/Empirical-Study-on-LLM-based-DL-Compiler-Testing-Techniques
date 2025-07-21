'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(100, 100)
dropout = nn.Dropout(p=0.5)
dropout(x)