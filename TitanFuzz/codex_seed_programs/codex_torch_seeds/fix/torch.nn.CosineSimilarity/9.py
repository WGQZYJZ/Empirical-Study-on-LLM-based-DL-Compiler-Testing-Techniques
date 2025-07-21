'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
print('Task 3: Call the API torch.nn.CosineSimilarity')
cos = nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos(input1, input2)
print('output: ', output)