'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
import torch
_input_tensor = torch.randint(low=0, high=9, size=(2, 3), dtype=torch.float32)
print('Input tensor: {}'.format(_input_tensor))
_nonzero_indices = torch.Tensor.nonzero(_input_tensor, as_tuple=False)
print('Non-zero indices: {}'.format(_nonzero_indices))