'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
import torch
_input_tensor = torch.randint(0, 10, (5, 5))
print('Input tensor:\n', _input_tensor)
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=0)
print('Output tensor:\n', _output_tensor)