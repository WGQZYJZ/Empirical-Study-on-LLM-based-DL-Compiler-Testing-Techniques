'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
print('Input data: \n', input)
output = F.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
print('Output data: \n', output)