"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
input_data = torch.randn(3, 5)
print('Input data: \n', input_data)
output = torch.norm(input_data, p=2, dim=1, keepdim=False, out=None, dtype=None)
print('Output: \n', output)
output = torch.norm(input_data, p=2, dim=0, keepdim=False, out=None, dtype=None)
print('Output: \n', output)
output = torch.norm(input_data, p=2, dim=None, keepdim=False, out=None, dtype=None)
print('Output: \n', output)