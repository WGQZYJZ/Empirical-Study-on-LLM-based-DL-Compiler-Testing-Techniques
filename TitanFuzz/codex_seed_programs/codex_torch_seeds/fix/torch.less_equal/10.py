'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([5, 4, 3, 2, 1])
z = torch.less_equal(x, y)
print(z)
print(z.dtype)