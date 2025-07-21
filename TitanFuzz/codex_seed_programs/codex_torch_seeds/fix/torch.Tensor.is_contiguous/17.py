'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('input tensor: ', _input_tensor)
print('is_contiguous: ', _input_tensor.is_contiguous())
_input_tensor = torch.randn(2, 3, 4, 5, 6)
print('input tensor: ', _input_tensor)
print('is_contiguous: ', _input_tensor.is_contiguous())
_input_tensor = torch.randn(2, 3, 4, 5, 6)
_input_tensor = _input_tensor.transpose(1, 4)
print('input tensor: ', _input_tensor)