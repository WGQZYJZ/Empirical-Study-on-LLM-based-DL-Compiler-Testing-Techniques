'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
_input_tensor = torch.randn(5, 3, 2, 2)
print(_input_tensor)
print(torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format))
print('contiguous_format: ', torch.contiguous_format)
_input_tensor = torch.randn(2, 3, 2, 2)
print(_input_tensor)
print(torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format))
print('contiguous_format: ', torch.contiguous_format)
'\nTask 4: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
_input_tensor = torch.randn(5, 3, 2, 2)