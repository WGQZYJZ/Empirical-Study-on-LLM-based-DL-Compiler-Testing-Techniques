'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:', _input_tensor)
_output_tensor = _input_tensor.type(torch.float32)
print('Output tensor:', _output_tensor)