'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.rand(3)
end = torch.rand(3)
weight = torch.rand(1)
print('Task 3: Call the API torch.lerp')
output = torch.lerp(input, end, weight)
print('input: ', input)
print('end: ', end)
print('weight: ', weight)
print('output: ', output)