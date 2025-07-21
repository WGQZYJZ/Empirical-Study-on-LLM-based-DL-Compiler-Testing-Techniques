'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.prod\ntorch.prod(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print('input:', input)
output = torch.prod(input, dim=0, keepdim=True)
print('output:', output)