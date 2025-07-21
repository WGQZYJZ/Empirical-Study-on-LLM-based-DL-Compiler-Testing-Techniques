'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.randn(20, 5)
print(input_data)
print(torch.std(input_data))
print(torch.std(input_data, dim=0))
print(torch.std(input_data, dim=1))
print(torch.std(input_data, dim=1, unbiased=False))
print(torch.std(input_data, dim=1, unbiased=True))
print(torch.std(input_data, dim=1, unbiased=True, keepdim=True))
print(torch.var(input_data))
print(torch.var(input_data, dim=0))
print(torch.var(input_data, dim=1))
print(torch.var(input_data, dim=1, unbiased=False))