'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
transposed_tensor = torch.Tensor.transpose(input_tensor, 0, 1)
print(transposed_tensor)
transposed_tensor = torch.Tensor.transpose(input_tensor, 1, 0)
print(transposed_tensor)
transposed_tensor = torch.Tensor.transpose(input_tensor, 1, 1)
print(transposed_tensor)