'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 1, 3, 3)
print('x:', x)
print('x.size():', x.size())
dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
y = dropout(x)
print('y:', y)
print('y.size():', y.size())