'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_data = torch.randn(2, 3, 4)
data = torch.randn(3, 2, 4)
torch.Tensor.resize_as_(input_data, data)
print(input_data)
data = torch.randn(3, 2, 4)
torch.Tensor.resize_as_(input_data, data, memory_format=torch.channels_last)
print(input_data)
data = torch.randn(2, 4, 3)
torch.Tensor.resize_as_(input_data, data, memory_format=torch.channels_last)
print(input_data)