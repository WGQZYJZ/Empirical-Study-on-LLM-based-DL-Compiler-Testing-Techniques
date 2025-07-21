'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose_\ntorch.Tensor.transpose_(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
input_tensor.transpose_(0, 1)
print(input_tensor)
input_tensor.transpose_(0, 1)
print(input_tensor)
input_tensor.transpose_(1, 0)
print(input_tensor)
input_tensor.transpose_(1, 0)
print(input_tensor)