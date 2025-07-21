'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.baddbmm\ntorch.Tensor.baddbmm(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.Tensor.baddbmm(batch1, batch2, beta=0.5, alpha=0.5)
print(result)