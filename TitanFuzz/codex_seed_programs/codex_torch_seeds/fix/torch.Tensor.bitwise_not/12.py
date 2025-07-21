'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
_input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.bool)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)
print('Output tensor:')
print(_output_tensor)