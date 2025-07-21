'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.baddbmm_\ntorch.Tensor.baddbmm_(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.empty(10, 3, 5)
torch.Tensor.baddbmm_(result, batch1, batch2)
print(result)