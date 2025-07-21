'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_data = torch.cumsum(input_data, dim=0)
print('input_data:', input_data)
print('output_data:', output_data)