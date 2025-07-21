'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
_input_tensor = torch.randn(2, 4)
chunk_tensor = _input_tensor.chunk(2, dim=1)
print('The input tensor is:', _input_tensor)
print('The chunk tensor is:', chunk_tensor)