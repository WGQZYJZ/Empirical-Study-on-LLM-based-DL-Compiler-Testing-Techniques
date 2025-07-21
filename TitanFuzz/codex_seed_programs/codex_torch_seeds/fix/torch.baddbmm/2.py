'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.baddbmm\ntorch.baddbmm(input, batch1, batch2, *, beta=1, alpha=1, out=None)\n'
import torch
batch_size = 3
n = 4
m = 5
p = 6
input = torch.randn(batch_size, n, p)
batch1 = torch.randn(batch_size, n, m)
batch2 = torch.randn(batch_size, m, p)
output = torch.baddbmm(input, batch1, batch2)
print('input:', input)
print('batch1:', batch1)
print('batch2:', batch2)
print('output:', output)