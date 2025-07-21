'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
input_data = torch.rand(3, 4, 5)
print(input_data.is_contiguous())
input_data = input_data.transpose(1, 2)
print(input_data.is_contiguous())
input_data = input_data.transpose(1, 2)
print(input_data.is_contiguous())