'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[2, 2, 2], [4, 4, 4]], dtype=torch.float32)
out = torch.greater(x, y)
print(out)
out = torch.greater_equal(x, y)
print(out)
out = torch.less(x, y)
print(out)
out = torch.less_equal(x, y)
print(out)
out = torch.equal(x, y)
print(out)
out = torch.equal(x, x)