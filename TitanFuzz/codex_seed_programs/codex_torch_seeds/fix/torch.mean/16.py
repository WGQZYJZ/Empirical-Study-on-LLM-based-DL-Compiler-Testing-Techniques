'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(4, 4)
print('Input data: ', input)
mean = torch.mean(input)
print('\nMean of all elements in input data: ', mean)
mean = torch.mean(input, dim=0)
print('\nMean of each column in input data: ', mean)
mean = torch.mean(input, dim=1)
print('\nMean of each row in input data: ', mean)
mean = torch.mean(input, dim=1, keepdim=True)
print('\nMean of each row in input data with keepdim=True: ', mean)