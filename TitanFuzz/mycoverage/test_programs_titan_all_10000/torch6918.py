import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 5)
feature_alpha_dropout = torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = feature_alpha_dropout(input_data)