'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(10, 5)
print(input_data)
print(torch.std(input_data))
print(torch.std(input_data, dim=0))
print(torch.std(input_data, dim=1))
print(torch.std(input_data, dim=1, unbiased=False))
print(torch.std(input_data, dim=1, keepdim=True))
print(torch.std(input_data, dim=(0, 1)))
print(torch.std(input_data, dim=(0, 1), unbiased=False))
print(torch.std(input_data, dim=(0, 1), keepdim=True))