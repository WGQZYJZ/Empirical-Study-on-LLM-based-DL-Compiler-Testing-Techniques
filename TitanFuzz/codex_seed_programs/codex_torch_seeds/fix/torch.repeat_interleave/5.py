'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data: ', input)
repeats = torch.tensor([2, 3])
output = torch.repeat_interleave(input, repeats, dim=0)
print('Output data: ', output)