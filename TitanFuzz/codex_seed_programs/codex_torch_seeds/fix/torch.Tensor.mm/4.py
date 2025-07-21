'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
input_tensor = torch.randn(2, 3)
mat2 = torch.randn(3, 2)
print(input_tensor.mm(mat2))
'\nTask 4: Call the API torch.mm\ntorch.mm(input_tensor, mat2)\n'
print(torch.mm(input_tensor, mat2))