'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
_input_tensor = torch.randn(4, 5)
_output_tensor = _input_tensor.chunk(3, dim=0)
print(_input_tensor)
print(_output_tensor)