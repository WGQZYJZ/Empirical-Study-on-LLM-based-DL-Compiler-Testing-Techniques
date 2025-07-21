'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input = torch.rand(5, 3)
repeats = torch.tensor([2, 3, 1, 4, 5])
print('Input: ')
print(input)
print('Repeats: ')
print(repeats)
print('Output: ')
print(torch.repeat_interleave(input, repeats, dim=0))