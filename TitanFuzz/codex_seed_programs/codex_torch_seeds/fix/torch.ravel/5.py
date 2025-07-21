'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
import torch
input = torch.tensor([[1, 2], [3, 4]])
print('Input: \n', input)
output = torch.ravel(input)
print('Output: \n', output)