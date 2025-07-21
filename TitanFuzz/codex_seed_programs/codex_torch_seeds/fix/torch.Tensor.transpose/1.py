'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
_input_tensor = torch.rand(3, 4, 5)
print('input tensor: ', _input_tensor)
_transposed_tensor = _input_tensor.transpose(0, 2)
print('transposed tensor: ', _transposed_tensor)