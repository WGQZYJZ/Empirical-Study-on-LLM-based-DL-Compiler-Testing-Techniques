'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(3, 5)
print(input)
feature_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = feature_dropout(input)
print(output)