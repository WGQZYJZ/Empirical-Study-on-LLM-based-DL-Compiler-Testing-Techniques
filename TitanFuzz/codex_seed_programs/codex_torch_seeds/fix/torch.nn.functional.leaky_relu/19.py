'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(3, 3)
print('input: ', input)
output = F.leaky_relu(input, negative_slope=0.01, inplace=False)
print('output: ', output)
output = F.relu(input, inplace=False)
print('output: ', output)
output = F.relu6(input, inplace=False)
print('output: ', output)
output = F.elu(input, alpha=1.0, inplace=False)
print