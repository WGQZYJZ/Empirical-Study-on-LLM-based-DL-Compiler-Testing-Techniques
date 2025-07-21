'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
if True:
    x = torch.randn(3, 4)
    y = torch.randn(4, 5)
    print(torch.matmul(x, y))