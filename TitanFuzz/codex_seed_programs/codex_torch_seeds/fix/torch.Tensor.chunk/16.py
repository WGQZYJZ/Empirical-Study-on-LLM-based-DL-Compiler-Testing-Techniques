'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
import torch
_input_tensor = torch.randn(10, 4)
_output_tensor = _input_tensor.chunk(4, dim=1)
print(_output_tensor)