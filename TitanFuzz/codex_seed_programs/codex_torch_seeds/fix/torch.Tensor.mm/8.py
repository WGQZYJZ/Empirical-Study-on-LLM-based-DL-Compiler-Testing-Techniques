'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
_input_tensor = torch.rand(2, 3)
mat2 = torch.rand(3, 2)
output_tensor = torch.Tensor.mm(_input_tensor, mat2)
print(output_tensor)