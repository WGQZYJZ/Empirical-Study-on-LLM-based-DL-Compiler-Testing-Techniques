'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input_data = Variable(torch.randn(5, 1, 10, 10))
feature_alpha_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = feature_alpha_dropout(input_data)
print(output)