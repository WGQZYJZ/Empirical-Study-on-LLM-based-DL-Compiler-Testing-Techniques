'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.rand(3, 4)
print(input_tensor)
transposed_tensor = input_tensor.transpose(0, 1)
print(transposed_tensor)