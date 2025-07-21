'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.baddbmm\ntorch.baddbmm(input, batch1, batch2, *, beta=1, alpha=1, out=None)\n'
import torch
batch_size = 5
n_row = 4
n_col = 3
input = torch.randn(batch_size, n_row, n_col)
batch1 = torch.randn(batch_size, n_row, n_row)
batch2 = torch.randn(batch_size, n_row, n_col)
output = torch.baddbmm(input, batch1, batch2)
print(output)