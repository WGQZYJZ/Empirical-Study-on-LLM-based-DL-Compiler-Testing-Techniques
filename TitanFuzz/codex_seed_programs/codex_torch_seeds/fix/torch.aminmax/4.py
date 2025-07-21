'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input_data = torch.randn(100, 100)
print(input_data)
print(torch.aminmax(input_data, dim=0, keepdim=True))
print(torch.aminmax(input_data, dim=1, keepdim=False))
print(torch.aminmax(input_data, dim=None, keepdim=False))