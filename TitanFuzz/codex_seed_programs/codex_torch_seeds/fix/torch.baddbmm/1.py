'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.baddbmm\ntorch.baddbmm(input, batch1, batch2, *, beta=1, alpha=1, out=None)\n'
import torch
import torch.nn.functional as F
batch_size = 10
input = torch.randn(batch_size, 10)
batch1 = torch.randn(batch_size, 10, 10)
batch2 = torch.randn(batch_size, 10, 10)
output = torch.baddbmm(input, batch1, batch2)
print(output)