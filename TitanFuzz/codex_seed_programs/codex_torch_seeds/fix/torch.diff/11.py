'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
print('input_data: ', input_data)
output = torch.diff(input_data)
print('output: ', output)