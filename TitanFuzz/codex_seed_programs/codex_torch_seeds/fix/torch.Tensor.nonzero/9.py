'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor: \n', input_tensor)
nonzero_indices = input_tensor.nonzero()
print('nonzero_indices: \n', nonzero_indices)
nonzero_indices = input_tensor.nonzero(as_tuple=True)
print('nonzero_indices: \n', nonzero_indices)