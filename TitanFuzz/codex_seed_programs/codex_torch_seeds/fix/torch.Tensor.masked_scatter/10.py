'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
print('Task 1: import PyTorch')
print('torch.__version__ = ', torch.__version__)
print('\nTask 2: Generate input data')
input_tensor = torch.arange(0, 20).view(4, 5)
print('input_tensor = ', input_tensor)
mask = torch.tensor([[True, True, True, True, True], [True, True, True, True, True], [True, True, True, False, False], [False, False, False, False, False]])
print('mask = ', mask)
print('\nTask 3: Call the API torch.Tensor.masked_scatter')
output_tensor = input_tensor.masked_scatter(mask, torch.tensor([0]))
print('output_tensor = ', output_tensor)