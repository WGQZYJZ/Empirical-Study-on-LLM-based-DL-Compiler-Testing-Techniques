'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input_data = torch.randn(10, 5)
print(input_data)
print(torch.tan(input_data))
output_data = torch.randn(10, 5)
print(torch.tan(input_data, out=output_data))