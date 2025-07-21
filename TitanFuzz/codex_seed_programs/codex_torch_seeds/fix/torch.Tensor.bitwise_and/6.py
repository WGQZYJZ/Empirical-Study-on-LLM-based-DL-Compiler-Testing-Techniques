'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(2, 3), dtype=torch.bool)
print('Input tensor: ', _input_tensor)
_output_tensor = _input_tensor.bitwise_and(_input_tensor)
print('Output tensor: ', _output_tensor)