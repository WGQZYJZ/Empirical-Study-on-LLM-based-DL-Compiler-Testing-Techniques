'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(2, 3, 4), dtype=torch.long)
print('Input Tensor:')
print(_input_tensor)
print('\n')
_nonzero_indices_tensor = _input_tensor.nonzero()
print('Nonzero indices of the input tensor:')
print(_nonzero_indices_tensor)
print('\n')
_nonzero_indices_tuple = _input_tensor.nonzero(as_tuple=True)
print('Nonzero indices of the input tensor as tuple:')
print(_nonzero_indices_tuple)
print('\n')