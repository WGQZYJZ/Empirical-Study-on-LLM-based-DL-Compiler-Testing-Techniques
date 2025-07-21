'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
import torch
input = torch.tensor([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]], [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
result = torch.diff(input, n=1, dim=(- 1), prepend=None, append=None)
print('Input: ', input)
print('Result: ', result)