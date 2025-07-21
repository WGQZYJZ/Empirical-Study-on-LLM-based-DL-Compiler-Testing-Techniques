'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
print(_input_tensor)
_result = torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)
print(_result)