'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addbmm\ntorch.Tensor.addbmm(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
import torch
batch1 = torch.rand(10, 3, 4)
batch2 = torch.rand(10, 4, 5)
torch.Tensor.addbmm(batch1, batch2, beta=1, alpha=1)