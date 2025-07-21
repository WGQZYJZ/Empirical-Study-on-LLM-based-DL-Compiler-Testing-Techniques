'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not\ntorch.Tensor.logical_not(_input_tensor)\n'
import torch
_input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
print('Input tensor: \n', _input_tensor, '\n')
_output_tensor = torch.Tensor.logical_not(_input_tensor)
print('Output tensor: \n', _output_tensor)