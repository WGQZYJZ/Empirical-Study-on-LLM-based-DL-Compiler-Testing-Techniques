'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([4, 5, 6, 7, 8])
z = torch.greater(x, y)
print('The result of torch.greater: ', z)