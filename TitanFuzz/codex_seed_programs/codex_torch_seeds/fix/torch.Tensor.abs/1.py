'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.abs\ntorch.Tensor.abs(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([(- 1), (- 2), 3, 4, (- 5), 6])
_output_tensor = torch.Tensor.abs(_input_tensor)
print('Output tensor:', _output_tensor)
'\nTask 4: Call the API torch.abs\ntorch.abs(_input_tensor)\n'
_output_tensor = torch.abs(_input_tensor)
print('Output tensor:', _output_tensor)