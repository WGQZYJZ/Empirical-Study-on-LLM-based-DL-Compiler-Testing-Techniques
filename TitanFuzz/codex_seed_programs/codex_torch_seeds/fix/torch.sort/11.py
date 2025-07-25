'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('\nPyTorch version: ', torch.__version__)
print('CUDA version: ', torch.version.cuda)
print('cuDNN version: ', torch.backends.cudnn.version())
print('CUDA available: ', torch.cuda.is_available())
print('\nTask 2: Generate input data')
input = torch.rand(10, 3)
print('Input: \n', input)
print('\nTask 3: Call the API torch.sort')
(sorted_input, sorted_indices) = torch.sort(input, dim=1, descending=False)
print('Sorted input: \n', sorted_input)
print('Sorted indices: \n', sorted_indices)
(sorted_input, sorted_indices) = torch.sort(input, dim=0, descending=False)
print('Sorted input: \n', sorted_input)