'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int8)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)
print('Output tensor:')
print(_output_tensor)