'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
input_data = torch.rand(4, 5)
print(input_data)
print(torch.argmax(input_data, dim=1))
print(torch.argmax(input_data, dim=1, keepdim=True))
print(torch.max(input_data, dim=1))
print(torch.max(input_data, dim=1, keepdim=True))