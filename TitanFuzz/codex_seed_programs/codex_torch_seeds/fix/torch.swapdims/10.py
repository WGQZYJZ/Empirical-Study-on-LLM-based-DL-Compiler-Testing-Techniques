'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
input = torch.arange(0, 6)
input = input.view(2, 3)
print('Input:')
print(input)
print('Output:')
print(torch.swapdims(input, 0, 1))