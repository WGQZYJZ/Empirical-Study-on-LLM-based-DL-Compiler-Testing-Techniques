'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.rand(5, 3)
print('Input:')
print(input)
index = torch.tensor([1, 2])
output = torch.take(input, index)
print('Output:')
print(output)