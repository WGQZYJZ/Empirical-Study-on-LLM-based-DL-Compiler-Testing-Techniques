'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr\ntorch.Tensor.addr(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
vec1 = torch.tensor([1, 2])
vec2 = torch.tensor([3, 4])
torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addbmm\ntorch.Tensor.addbmm(beta=1, mat, alpha=1, batch1, batch2)\n'
import torch
import torch
batch1 = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])