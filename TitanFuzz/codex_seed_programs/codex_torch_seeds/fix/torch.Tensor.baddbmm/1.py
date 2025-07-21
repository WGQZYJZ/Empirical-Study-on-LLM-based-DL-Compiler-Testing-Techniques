'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.baddbmm\ntorch.Tensor.baddbmm(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.empty(2, 3)
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)
torch.Tensor.baddbmm(input_tensor, batch1, batch2)
print(input_tensor)