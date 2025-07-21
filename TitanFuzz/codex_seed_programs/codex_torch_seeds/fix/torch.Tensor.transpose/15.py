'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
output_tensor = input_tensor.transpose(1, 2)
print(input_tensor)
print(output_tensor)