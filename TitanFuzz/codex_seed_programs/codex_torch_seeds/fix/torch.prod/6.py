'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.prod\ntorch.prod(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_data = torch.prod(input_data, dim=1)
print(output_data)