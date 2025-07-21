'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
import torch
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 5)
torch.Tensor.mm(mat1, mat2)
torch.mm(mat1, mat2)