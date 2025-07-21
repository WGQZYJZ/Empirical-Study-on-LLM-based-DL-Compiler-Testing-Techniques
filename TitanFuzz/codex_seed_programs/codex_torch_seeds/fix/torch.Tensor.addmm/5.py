'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm\ntorch.Tensor.addmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
import torch
tensor_A = torch.randn(2, 3)
tensor_B = torch.randn(2, 3)
tensor_C = torch.randn(2, 3)
torch.Tensor.addmm(tensor_A, tensor_B, tensor_C)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import torch
tensor_A = torch.randn(2, 3)
tensor_B = torch.randn(2, 3)
tensor_C = torch.randn(2, 3)