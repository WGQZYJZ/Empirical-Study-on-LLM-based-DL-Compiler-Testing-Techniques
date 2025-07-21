'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
print(torch.amax(input_data, 0))
print(torch.amax(input_data, 1))
print(torch.amax(input_data, 0, keepdim=True))
print(torch.amax(input_data, 1, keepdim=True))
print(torch.argmax(input_data, 0))
print(torch.argmax(input_data, 1))
print(torch.argmax(input_data, 0, keepdim=True))
print(torch.argmax(input_data, 1, keepdim=True))