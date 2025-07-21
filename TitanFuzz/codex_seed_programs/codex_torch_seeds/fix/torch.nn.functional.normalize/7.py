'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
input_data = torch.randn(5, 3)
output_data = torch.nn.functional.normalize(input_data, dim=1)
print(input_data)
print(output_data)