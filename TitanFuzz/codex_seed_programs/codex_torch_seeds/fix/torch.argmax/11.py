'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.argmax(x, dim=1)
print('y = ', y)
y = torch.argmax(x, dim=1, keepdim=True)
print('y = ', y)
y = torch.argmax(x, dim=0)
print('y = ', y)
y = torch.argmax(x, dim=0, keepdim=True)
print('y = ', y)