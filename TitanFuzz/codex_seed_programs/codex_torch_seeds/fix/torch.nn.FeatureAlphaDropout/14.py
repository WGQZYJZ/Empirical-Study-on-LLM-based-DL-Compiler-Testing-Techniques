'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.nn import FeatureAlphaDropout
input_data = torch.randn(10, 5)
feature_dropout = FeatureAlphaDropout(p=0.5, inplace=False)
output = feature_dropout(input_data)
print(output)