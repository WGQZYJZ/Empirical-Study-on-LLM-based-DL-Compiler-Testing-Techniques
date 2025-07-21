'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
x = torch.randn(1, 2, 3)
print('Input: ', x)
y = torch.nn.functional.relu_(x)
print('Output: ', y)