'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3)
tensor = torch.randn(3, 2)
torch.Tensor.resize_as_(input_tensor, tensor)
print(input_tensor)