'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
x = torch.tensor([(- 1), 0, 1, 2, 3, 4], dtype=torch.float32)
y = torch.tensor([(- 1), 0, 1, 2, 3, 4], dtype=torch.float32)
print(torch.less_equal(x, y))
print(torch.le(x, y))
print((x <= y))
print(torch.less_equal(x, 0))
print(torch.le(x, 0))
print((x <= 0))