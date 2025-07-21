'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
import torch
input_tensor = torch.randn(4, 3)
vec = torch.randn(3)
output_tensor = input_tensor.mv(vec)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
import torch
input_tensor = torch.randn(4, 3)
mat2 = torch.randn(3, 4)
output_tensor = input_tensor.mm(mat2)
print(output_tensor)