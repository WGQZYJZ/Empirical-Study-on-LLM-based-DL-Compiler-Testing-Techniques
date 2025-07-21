'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(3, 3)
print('Input: ', x)
relu = nn.ReLU()
print('ReLU: ', relu(x))
relu = nn.ReLU(inplace=True)
print('ReLU: ', relu(x))
relu = nn.ReLU(inplace=False)
print('ReLU: ', relu(x))
relu = nn.ReLU(inplace=True)
print('ReLU: ', relu(x))