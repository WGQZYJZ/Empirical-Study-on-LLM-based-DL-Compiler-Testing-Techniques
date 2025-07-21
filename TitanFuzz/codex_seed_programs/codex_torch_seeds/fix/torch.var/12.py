'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
print('Input data: ', input_data)
output = torch.var(input_data, dim=1, unbiased=False, keepdim=False)
print('Output: ', output)