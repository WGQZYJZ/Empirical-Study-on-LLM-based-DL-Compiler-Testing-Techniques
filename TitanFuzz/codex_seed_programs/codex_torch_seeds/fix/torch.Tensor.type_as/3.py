'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.randint(0, 10, (3, 3), dtype=torch.float64)
print('Input tensor:')
print(_input_tensor)
_output_tensor = _input_tensor.type_as(torch.FloatTensor())
print('Output tensor:')
print(_output_tensor)