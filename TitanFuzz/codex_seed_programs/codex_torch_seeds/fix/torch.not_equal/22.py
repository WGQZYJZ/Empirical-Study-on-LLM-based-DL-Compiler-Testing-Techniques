'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.not_equal(x, y)
print('output = ', output)