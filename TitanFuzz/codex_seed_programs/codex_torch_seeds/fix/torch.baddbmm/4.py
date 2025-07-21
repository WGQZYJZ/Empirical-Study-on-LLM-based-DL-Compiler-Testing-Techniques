'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.baddbmm\ntorch.baddbmm(input, batch1, batch2, *, beta=1, alpha=1, out=None)\n'
import torch
batch_size = 3
n = 4
m = 5
p = 6
input = torch.ones(batch_size, n, p)
batch1 = torch.ones(batch_size, n, m)
batch2 = torch.ones(batch_size, m, p)
res = torch.baddbmm(input, batch1, batch2, beta=0.5, alpha=0.5)
print(res)