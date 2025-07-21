'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.divide\ntorch.divide(input, other, *, rounding_mode=None, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[2, 2, 2], [2, 2, 2]])
output = torch.divide(input, other)
print(output)