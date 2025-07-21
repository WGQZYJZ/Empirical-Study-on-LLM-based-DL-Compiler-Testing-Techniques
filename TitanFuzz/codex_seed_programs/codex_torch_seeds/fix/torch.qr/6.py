'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
input = torch.rand(2, 3)
print(input)
print(torch.qr(input))
input = torch.rand(3, 2)
print(input)
print(torch.qr(input))
input = torch.rand(3, 3)
print(input)
print(torch.qr(input))
input = torch.rand(3, 3, 3)
print(input)
print(torch.qr(input))