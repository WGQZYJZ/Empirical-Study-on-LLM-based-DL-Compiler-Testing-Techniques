'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
_output_tensor = _input_tensor.chunk(chunks=2, dim=0)
print('input tensor:\n', _input_tensor)
print('output tensor:\n', _output_tensor)