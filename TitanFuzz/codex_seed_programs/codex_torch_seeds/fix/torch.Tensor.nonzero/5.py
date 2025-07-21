'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.randint(low=0, high=9, size=(4, 4), dtype=torch.int32)
print('Input tensor:')
print(_input_tensor)
_output_tensor = _input_tensor.nonzero()
print('Output tensor:')
print(_output_tensor)
_output_tensor = _input_tensor.nonzero(as_tuple=True)
print('Output tensor:')
print(_output_tensor)