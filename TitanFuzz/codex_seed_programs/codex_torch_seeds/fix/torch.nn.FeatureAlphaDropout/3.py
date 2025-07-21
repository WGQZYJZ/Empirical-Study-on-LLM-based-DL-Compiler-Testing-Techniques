'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(2, 3)
print('Input data: ', input)
feature_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = feature_dropout(input)
print('Output data: ', output)