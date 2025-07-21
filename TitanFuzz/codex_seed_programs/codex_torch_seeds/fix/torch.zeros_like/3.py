'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros_like\ntorch.zeros_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.zeros_like(input)
print('Input: ', input)
print('Output: ', output)