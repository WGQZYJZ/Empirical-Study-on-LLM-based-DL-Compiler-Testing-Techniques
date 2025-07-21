'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 4)
transpose_input = input_tensor.t()
print(input_tensor)
print(transpose_input)
'\nTask 4: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
transpose_input = input_tensor.transpose(0, 1)
print(transpose_input)