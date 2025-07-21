'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose_\ntorch.Tensor.transpose_(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.rand(3, 4)
torch.Tensor.transpose_(input_tensor, 0, 1)
print(input_tensor)