'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.le(input, other)
print('output = ', output)