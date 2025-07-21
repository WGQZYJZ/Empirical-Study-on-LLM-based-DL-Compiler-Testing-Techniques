'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.prod\ntorch.prod(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.prod(input_data, dim=0)
print(output)