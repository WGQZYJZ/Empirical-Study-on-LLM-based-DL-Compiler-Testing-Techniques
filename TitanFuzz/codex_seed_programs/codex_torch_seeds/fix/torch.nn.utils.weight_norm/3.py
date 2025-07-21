"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
import torch.nn as nn
import torch.nn.utils.weight_norm as weight_norm
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.nn.utils.weight_norm')
linear = nn.Linear(10, 10)
linear = weight_norm(linear)
print(linear.weight_v, linear.weight_g, linear.bias)