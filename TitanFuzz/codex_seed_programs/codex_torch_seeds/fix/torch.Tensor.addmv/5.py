'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
print(torch.Tensor.addmv(torch.randn(4, 3), torch.randn(3, 2), torch.randn(2)))
print(torch.Tensor.addmv(torch.randn(4, 3), torch.randn(3, 2), torch.randn(2), alpha=2))
print(torch.Tensor.addmv(torch.randn(4, 3), torch.randn(3, 2), torch.randn(2), beta=2))
print(torch.Tensor.addmv(torch.randn(4, 3), torch.randn(3, 2), torch.randn(2), beta=2, alpha=2))