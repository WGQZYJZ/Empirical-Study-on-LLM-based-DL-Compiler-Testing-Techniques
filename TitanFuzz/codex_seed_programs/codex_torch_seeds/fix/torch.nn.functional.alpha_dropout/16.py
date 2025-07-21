'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 2, 3, 3)
output = F.alpha_dropout(input, p=0.5, training=False, inplace=False)
print(output)
output = F.alpha_dropout(input, p=0.5, training=True, inplace=False)
print(output)