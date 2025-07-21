'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.randn(5, 10)
torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)
feature_alpha_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
x_out = feature_alpha_dropout(x)
print('x_out: ', x_out)
print('x_out: ', x_out)
print('x_out.shape: ', x_out.shape)
print('x.shape: ', x.shape)