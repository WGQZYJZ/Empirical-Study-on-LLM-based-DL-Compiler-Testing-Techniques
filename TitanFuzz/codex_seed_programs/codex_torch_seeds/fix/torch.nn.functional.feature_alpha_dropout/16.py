'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import feature_alpha_dropout
input = torch.randn(2, 3)
print(input)
output = feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
print(output)