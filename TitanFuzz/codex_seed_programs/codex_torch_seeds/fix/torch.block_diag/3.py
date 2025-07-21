'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
t1 = torch.randn(2, 3)
t2 = torch.randn(4, 3)
t3 = torch.randn(3, 2)
result = torch.block_diag(t1, t2, t3)
print('The result is: ', result)