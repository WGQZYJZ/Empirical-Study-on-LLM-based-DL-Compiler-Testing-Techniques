'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input = torch.randn(3, 5)
print('Input Data:', input)
print('Result:', torch.aminmax(input, dim=0, keepdim=False))
print('Result:', torch.aminmax(input, dim=0, keepdim=True))
print('Result:', torch.aminmax(input, dim=1, keepdim=False))
print('Result:', torch.aminmax(input, dim=1, keepdim=True))
print('Result:', torch.aminmax(input, dim=None, keepdim=False))
print('Result:', torch.aminmax(input, dim=None, keepdim=True))