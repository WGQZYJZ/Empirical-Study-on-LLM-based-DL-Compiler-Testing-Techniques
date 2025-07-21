'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
(min_value, max_value) = torch.aminmax(input_data, dim=1, keepdim=True)
print(min_value)
print(max_value)