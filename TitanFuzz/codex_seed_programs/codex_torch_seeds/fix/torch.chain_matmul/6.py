'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chain_matmul\ntorch.chain_matmul(*matrices, out=None)\n'
import torch
a = torch.randn(10, 10)
b = torch.randn(10, 10)
c = torch.randn(10, 10)
d = torch.randn(10, 10)
e = torch.randn(10, 10)
torch.chain_matmul(a, b, c, d, e)