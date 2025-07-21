'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addbmm_\ntorch.Tensor.addbmm_(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
batch1 = torch.rand(10, 2, 3)
batch2 = torch.rand(10, 3, 4)
torch.Tensor.addbmm_(input_tensor, batch1, batch2)
print(input_tensor)