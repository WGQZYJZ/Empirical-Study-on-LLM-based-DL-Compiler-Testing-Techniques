'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = _input_tensor.type(torch.float32)
print(_input_tensor)
print(_output_tensor)