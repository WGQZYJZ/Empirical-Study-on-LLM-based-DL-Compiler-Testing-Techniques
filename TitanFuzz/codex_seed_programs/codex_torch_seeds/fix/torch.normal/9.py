'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.normal(0, 1, size=(2, 3))
print(output_data)
output_data = torch.rand(size=(2, 3))
print(output_data)
output_data = torch.randn(size=(2, 3))
print(output_data)