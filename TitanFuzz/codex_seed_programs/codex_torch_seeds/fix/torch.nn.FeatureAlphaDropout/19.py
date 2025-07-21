'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(5, 3)
feature_alpha_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = feature_alpha_dropout(input_data)
print(output)