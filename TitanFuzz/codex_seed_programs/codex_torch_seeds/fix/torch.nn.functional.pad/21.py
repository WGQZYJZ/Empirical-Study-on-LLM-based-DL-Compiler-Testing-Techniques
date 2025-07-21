"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(input)
pad = (1, 1, 1, 1)
mode = 'constant'
value = 0
print(torch.nn.functional.pad(input, pad, mode, value))