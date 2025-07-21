'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
max_index = torch.argmax(x, dim=1)
print(max_index)