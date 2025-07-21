'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = input_tensor.contiguous()
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)