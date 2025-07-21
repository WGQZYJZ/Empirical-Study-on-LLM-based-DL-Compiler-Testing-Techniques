'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(20, 16)
m = nn.Dropout(p=0.2)
output = m(input)
print(output)