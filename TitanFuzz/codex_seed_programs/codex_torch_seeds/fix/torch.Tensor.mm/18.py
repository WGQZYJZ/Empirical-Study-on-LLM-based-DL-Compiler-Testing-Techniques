'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
input_tensor = torch.ones(size=(1, 5))
mat2 = torch.randn(size=(5, 3))
output = torch.Tensor.mm(input_tensor, mat2)
print(output)