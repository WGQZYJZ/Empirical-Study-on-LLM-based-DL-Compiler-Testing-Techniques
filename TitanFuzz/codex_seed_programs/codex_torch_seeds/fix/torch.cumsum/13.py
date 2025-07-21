'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
cumsum_data = torch.cumsum(input_data, dim=0)
print('Cumulative sum along dim 0: ', cumsum_data)
cumsum_data = torch.cumsum(input_data, dim=1)
print('Cumulative sum along dim 1: ', cumsum_data)