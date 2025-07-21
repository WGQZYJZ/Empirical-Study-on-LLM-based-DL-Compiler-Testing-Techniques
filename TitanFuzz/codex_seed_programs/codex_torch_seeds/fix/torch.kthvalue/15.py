'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
k = 2
print('2nd largest element: ', torch.kthvalue(input_data, k))