'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randperm\ntorch.randperm(n, *, generator=None, out=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = torch.ones(5, 3)
print('Input data: ', input_data)
random_permutation = torch.randperm(5)
print('Random permutation: ', random_permutation)
random_permutation = torch.randperm(10)
print('Random permutation: ', random_permutation)