'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(5, 5)
print('input:', input)
output = F.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
print('output:', output)
'\nTask 4: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=True, inplace=False)\n'
output = F.feature_alpha_dropout(input, p=0.5, training=True, inplace=False)
print('output:', output)