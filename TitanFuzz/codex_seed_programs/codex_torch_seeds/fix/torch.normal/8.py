'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.normal(mean=input_data, std=torch.ones(2, 3))
print(output_data)
'\nTask 4: Call the API torch.randn\ntorch.randn(size, *, out=None)\n'
print(torch.randn(2, 3))
'\nTask 5: Call the API torch.rand\ntorch.rand(size, *, out=None)\n'
print(torch.rand(2, 3))