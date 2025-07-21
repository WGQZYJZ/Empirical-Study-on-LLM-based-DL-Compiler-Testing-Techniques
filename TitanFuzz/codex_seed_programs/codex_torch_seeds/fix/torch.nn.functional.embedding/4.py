'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding\ntorch.nn.functional.embedding(input, weight, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False)\n'
import torch
input = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]])
weight = torch.randn(10, 3)
output = torch.nn.functional.embedding(input, weight, padding_idx=0, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False)
print('input: ', input)
print('weight: ', weight)
print('output: ', output)