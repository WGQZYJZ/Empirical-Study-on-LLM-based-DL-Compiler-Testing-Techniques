'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
print('Task 1: import PyTorch')
print(torch.__version__)
print()
print('Task 2: Generate input data')
x = torch.tensor([[1, 2], [3, 4]])
print(x)
print()
print('Task 3: Call the API torch.clone')
y = torch.clone(x)
print(y)
print()