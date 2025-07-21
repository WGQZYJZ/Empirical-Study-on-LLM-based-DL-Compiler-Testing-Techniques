'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
_input_tensor = torch.arange(0, 10, dtype=torch.float32)
print(_input_tensor)
_output_tensor = torch.Tensor.float_power(_input_tensor, 2)
print(_output_tensor)