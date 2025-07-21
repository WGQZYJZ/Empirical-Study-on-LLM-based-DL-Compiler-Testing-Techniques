'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
data = torch.rand(2, 3)
print('data: ', data)
data_rand = torch.rand(2, 3)
print('data_rand: ', data_rand)