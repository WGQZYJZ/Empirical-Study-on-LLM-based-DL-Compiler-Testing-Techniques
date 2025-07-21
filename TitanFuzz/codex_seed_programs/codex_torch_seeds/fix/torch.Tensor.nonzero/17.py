'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print('input_tensor:\n', input_tensor)
nonzero_tensor = input_tensor.nonzero()
print('nonzero_tensor:\n', nonzero_tensor)
nonzero_tuple = input_tensor.nonzero(as_tuple=True)
print('nonzero_tuple:\n', nonzero_tuple)