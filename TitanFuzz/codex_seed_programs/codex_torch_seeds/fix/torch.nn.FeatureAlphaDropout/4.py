'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 2)
print('Input: ', x)
feature_alpha_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
y = feature_alpha_dropout(x)
print('Output: ', y)