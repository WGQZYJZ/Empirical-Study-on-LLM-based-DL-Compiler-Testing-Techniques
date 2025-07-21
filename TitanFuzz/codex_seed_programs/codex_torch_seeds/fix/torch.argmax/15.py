'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('a:', a)
print('torch.argmax(a, dim=1):', torch.argmax(a, dim=1))
print('torch.argmax(a, dim=0):', torch.argmax(a, dim=0))
print('torch.argmax(a):', torch.argmax(a))
print('torch.argmax(a, keepdim=True):', torch.argmax(a, keepdim=True))