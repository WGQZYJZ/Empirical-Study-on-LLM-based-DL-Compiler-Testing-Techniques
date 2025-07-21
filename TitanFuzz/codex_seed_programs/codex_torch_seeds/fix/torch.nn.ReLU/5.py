'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
input = torch.randn(1, 3, 3, 3)
relu = torch.nn.ReLU(inplace=False)
output = relu(input)
print('input: ', input)
print('output: ', output)