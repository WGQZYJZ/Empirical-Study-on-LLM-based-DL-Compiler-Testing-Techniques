'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
print('PyTorch version is: ', torch.__version__)
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data: ', input_data)
output_data = torch.diff(input_data, n=1, dim=(- 1), prepend=None, append=None)
print('Output data: ', output_data)