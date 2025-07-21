'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.rand(3, 5)
output = F.dropout(input, p=0.5, training=True)
print('Input: ', input)
print('Output: ', output)