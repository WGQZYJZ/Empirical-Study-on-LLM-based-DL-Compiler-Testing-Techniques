'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 5)
print('Input: ', input)
dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = dropout(input)
print('Output: ', output)