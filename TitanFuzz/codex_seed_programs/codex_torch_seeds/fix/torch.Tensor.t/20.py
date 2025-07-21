'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
transpose_tensor = input_tensor.t()
print(transpose_tensor)
transpose_tensor = torch.transpose(input_tensor, 0, 1)
print(transpose_tensor)
input_tensor.transpose_(0, 1)
print(input_tensor)