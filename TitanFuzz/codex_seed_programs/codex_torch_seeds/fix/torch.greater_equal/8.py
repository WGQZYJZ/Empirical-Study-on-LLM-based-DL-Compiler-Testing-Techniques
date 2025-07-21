'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater_equal\ntorch.greater_equal(input, other, *, out=None)\n'
import torch
import torch
x = torch.tensor([(- 1), 0, 1, 2])
y = torch.tensor([(- 2), 0, 1, 2])
z = torch.greater_equal(x, y)
print('The input tensor x:', x)
print('The input tensor y:', y)
print('The result tensor z:', z)
print('The result tensor z elements:', z.tolist())