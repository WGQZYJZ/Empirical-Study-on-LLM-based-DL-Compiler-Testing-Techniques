'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(100, 100)
dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = dropout(input_data)
print(output)
dropout = nn.FeatureAlphaDropout(p=0.5, inplace=True)
output = dropout(input_data)
print(output)