'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
_input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
print('Input tensor: \n', _input_tensor)
_output_tensor = _input_tensor.bitwise_xor_(torch.ones(4, 4, dtype=torch.uint8))
print('Output tensor: \n', _output_tensor)